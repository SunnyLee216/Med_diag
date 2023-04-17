import re, string, os
from typing import List
import dotenv
dotenv.load_dotenv()
import requests
import tiktoken
from langchain import OpenAI, Wikipedia
from langchain.llms.base import BaseLLM
from langchain.chat_models import ChatOpenAI
from langchain.agents.react.base import DocstoreExplorer
from langchain.prompts import PromptTemplate
from prompts import rank_agent_prompt,rethink_agent_prompt,score_agent_prompt,summarize_prompt,REFLECTION_HEADER,rethink_agent_prompt2
from fewshots import  REFLECTIONS,RANK_FEW_SHOTS,RETHINK_FEW_SHOTS2,RETHINK_FEW_SHOTS,SCORE_FEW_SHOTS
import json

    
class Rank_agent:
    def __init__(self):
        self.llm = OpenAI(
            temperature=0,
            max_tokens=256,
            model_name="gpt-3.5-turbo",
            model_kwargs={"stop": "\n"},
        )
        self.rank_prompt = rank_agent_prompt
        self.examples = RANK_FEW_SHOTS
    def rank(self,row):
        rank_str =self.llm(self.build_agent_prompt(row)).strip('\n').strip()
        rank_list = self.format_rank(rank_str)
        return rank_str, rank_list
       
    def build_agent_prompt(self,row):
        return self.rank_prompt.format(
                            examples = self.examples,
                            information = row['Information'],
                            diag_list = row['choices'])
    def format_rank(self,rank):
        # 把字符串类似1. tuberculosis; 2. viral pharyngitis; 3. urti; 4. bronchitis; 5. influenza;的字符串变成['tuberculosis','viral pharyngitis','urti','bronchitis','influenza']
        rank = rank.split(';')
        rank = [i.split('.')[-1].strip() for i in rank]
        return rank
class Score_agent:
    def __init__(self):
        self.llm = OpenAI(
            temperature=0,
            max_tokens=1200,
            model_name="gpt-3.5-turbo",
            
        )
        self.score_prompt = score_agent_prompt
        self.examples = SCORE_FEW_SHOTS
    def score(self,row,top1_diag,explanation):
        response =self.llm(self.build_agent_prompt(row,top1_diag,explanation)).strip('\n').strip()
        # 把score是reponse里面的TOTAL_SCORE: 后面的数字
        #print(response)
        score = re.findall(r'TOTAL_SCORE: (\d+)',response)[0]
        score = int(score)
        return score
    def build_agent_prompt(self,row,top1_diag,explanation):
        return self.score_prompt.format(
                            examples = self.examples,
                            information = row['Information'],
                            
                            disease = top1_diag,
                            explanation = explanation
                            )
class Rethink_agent2:
    def __init__(self) -> None:
        self.llm = OpenAI(
            temperature=0,
            max_tokens=600,
            model_name="gpt-3.5-turbo",
            
        )
        self.rethink_prompt = rethink_agent_prompt2
        self.examples = RETHINK_FEW_SHOTS2
    def rethink(self,row,previous_rank,top1_knwledge,top1_diag):
        repsonse=self.llm(self.build_agent_prompt(row,previous_rank,top1_knwledge,top1_diag))
        #print(repsonse)
        # 截取thought,ANSWER和EXPLANATION,Thought是THOUGHT:之后的内容,ANSWER是ANSWER:之后的内容，EXPLANATION是EXPLANATION:之后的内容
        #thougt 是THOUGHT:之后的，ANSWER之前的内容
        thought = repsonse.split('THOUGHT:')[-1].split('ANSWER:')[0].lower().strip('\n').strip()
        answer =repsonse.split('ANSWER:')[-1].split('EXPLANATION:')[0].lower().strip('\n').strip()
        # EXPLANATION是EXPLANATION:之后,ANOTHER DIAGNOSIS:之前的内容
        explanation = repsonse.split('EXPLANATION:')[-1].split('ANOTHER DIAGNOSIS:')[0].strip('\n').strip()
        another_diag = ''
        # 只有当answer是no的时候，才会有another_diag
        
        another_diag = repsonse.split('ANOTHER DIAGNOSIS:')[-1].lower().strip('\n').strip().strip(string.punctuation)
        return  thought,answer,explanation,another_diag
    def build_agent_prompt(self,row,previous_rank,top1_knwledge,top1_diag):
        return self.rethink_prompt.format(
                            
                            information = row['Information'],
                            diag_set = previous_rank,
                            top1_knowledge = top1_knwledge,
                            top1_diag = top1_diag)
class Rethink_agent:
    def __init__(self) -> None:
        self.llm = OpenAI(
            temperature=0,
            max_tokens=600,
            model_name="gpt-3.5-turbo",
            
        )
        self.rethink_prompt = rethink_agent_prompt
        self.examples = RETHINK_FEW_SHOTS2
    def rethink(self,row,previous_rank,top1_knwledge,top1_diag):
        repsonse=self.llm(self.build_agent_prompt(row,previous_rank,top1_knwledge,top1_diag))
        #print(repsonse)
        # 截取ANSWER和EXPLANATION,ANSWER是第一个换行符之前的内容，EXPLANATION是第一个换行符之后的内容
        answer = repsonse.split('\n')[0].lower().strip('\n').strip()
        # EXPLANATION是EXPLANATION:之后的内容
        explanation = repsonse.split('EXPLANATION:')[-1].strip('\n').strip()
    
        return  answer,explanation
    def build_agent_prompt(self,row,previous_rank,top1_knwledge,top1_diag):
        return self.rethink_prompt.format(
                            examples = self.examples,
                            information = row['Information'],
                            
                            previous_rank = previous_rank,
                            top1_knowledge = top1_knwledge,
                            top1_diag = top1_diag)
class Knowledge_agent:
    def __init__(self,url='http://127.0.0.1:3000/search', path="dis_responses.json",max_steps = 6):
        self.url = url
        self.llm = OpenAI(
            temperature=0,
            max_tokens=1024,
            model_name="gpt-3.5-turbo",

        )
        self.max_steps = max_steps  
        self.step_n = 1
        self.knowledge = self.load_local_knowledge(path)
        self.summarize_prompt = summarize_prompt
        self.summarize_pool = {}

    def serach(self, query):
        '''根据问题，返回答案'''
        # question = "The evidence of Pnuemonia?"
        if query.lower() in self.knowledge:
            text = self.knowledge[query.lower()]['response_text'][:2048]
            # 看query是否在summary_pool里面，如果在，就直接返回summary，如果不在，就把text放入summary_pool
            if query.lower() in self.summarize_pool:
                return self.summarize_pool[query.lower()]
            else:
                summary = self.summarize(text)
                self.summarize_pool[query.lower()] = summary
                return summary
            
        else:
            try:
                question = "The evidence of "+query+"?"
                response = requests.post(self.url, data={'query': question})
                response_text = response.json()['response_text']
                source_text = response.json()['source_text']
                # 存入本地知识库
                self.knowledge[query.lower()] = {'response_text':response_text,'source_text':source_text}
                
                # 摘要
                summary = self.summarize(response_text)
                self.summarize_pool[query.lower()] = summary
                # 保存到本地
                with open('dis_responses.json', 'w', encoding='utf-8') as f:
                    json.dump(self.knowledge, f, ensure_ascii=False, indent=4)
                
                return summary
            except Exception as e:
                return ""
    
    def summarize(self, text):
        '''对文本进行摘要'''
        try:
            text = text
            return self.llm(self.build_agent_summarize_prompt(paragraph=text)).strip('\n').strip()
        except Exception as e:
            text = text[:2048]
            return self.llm(self.build_agent_summarize_prompt(paragraph=text)).strip('\n').strip()
        
    
    def build_agent_summarize_prompt(self,paragraph):
        return self.summarize_prompt.format(paragraph = paragraph)
        
    def load_local_knowledge(self, path):
        '''加载本地知识库'''
        try:
            with open(path, 'r', encoding='utf-8') as f:
                self.knowledge = json.load(f)
                #把key转成小写，方便后面匹配
                self.knowledge = {k.lower():v for k,v in self.knowledge.items()}
                print("加载本地知识库成功")
        except Exception as e:
            print(e)
            print('加载本地知识库失败')
            self.knowledge = {}
        return self.knowledge
class DECIDER:
    def __init__(self) -> None:
        self.llm = OpenAI(
            temperature=0,
            max_tokens=1024,
            model_name="gpt-3.5-turbo",
            
        )
        self.decider_init_prompt = decider_init_prompt
        self.decider_prompt = decider_prompt
        self.decier_choose_prompt = decider_choose_prompt
        self.final_prompt = decider_final_prompt
        self.Choose_examples = CHOOSE_FWE_SHOTS
        # 制定模板"Here is the information of a new patient:{information}\nBased on the previous dialogue, what is the diagnosis? Select the most likely diagnosis from the following list.\nThe list of diseases is as follows:{diag_set}.'
        self.question = "Here is the information of a new patient:{information}\nBased on the previous dialogue, what is the diagnosis? Select the most likely diagnosis from the following list.\nThe list of diseases is as follows:{diag_set}."

    def choose(self,row):
        response = self.llm(self.build_agent_choose_prompt(row)).strip('\n').strip()


        return response
    def build_agent_choose_prompt(self,row):
        # 用row填充self.question
        self.question = self.question.format(information = row['Information'],diag_set = row['Diag_Set'])
        return self.decier_choose_prompt.format(
                            information = row['Information'],
                            examples = self.Choose_examples,
                            diagnosis = row['Diagnosis'],
                            )
    def decide_init(self,options_filtered_str,relative_likelihood):
        response = self.llm(self.build_agent_decide_init_prompt(self.question,options_filtered_str,relative_likelihood)).strip('\n').strip()
        return response
    def build_agent_decide_init_prompt(self,options_filtered_str,relative_likelihood):
        return self.decider_init_prompt.format(
                            question = self.question
                            ,options = options_filtered_str
                            ,relative_likelihood = relative_likelihood                                
                            )
    def decide(self,row,chat_history,last_teacher_message):
        response = self.llm(self.build_agent_prompt(row,chat_history,last_teacher_message)).strip('\n').strip()
        return response
    def decide_final(self,row,chat_history,last_teacher_message):
        response = self.llm(self.build_agent_prompt(row,chat_history,last_teacher_message)).strip('\n').strip()
        return response
    def build_agent_prompt(self,question,chat_history,last_teacher_message):
        return self.decider_prompt.format(
                            question= self.question,
                            chat_history = chat_history,
                            last_teacher_message = last_teacher_message,
                            
                            )
### String Stuff ###

def parse_action(string):
    pattern = r'^(\w+)\[(.+)\]$'
    match = re.match(pattern, string)
    
    if match:
        action_type = match.group(1)
        argument = match.group(2)
        return action_type, argument
    
    else:
        return None

def format_step(step: str) -> str:
    return step.strip('\n').strip().replace('\n', '')

def format_reflections(reflections: List[str]) -> str:
    if reflections == []:
        return ''
    else:
        header = REFLECTION_HEADER
        return header + 'Reflections:\n- ' + '\n- '.join([r.strip() for r in reflections])

def normalize_answer(s):
  def remove_articles(text):
    return re.sub(r"\b(a|an|the)\b", " ", text)
  
  def white_space_fix(text):
      return " ".join(text.split())

  def remove_punc(text):
      exclude = set(string.punctuation)
      return "".join(ch for ch in text if ch not in exclude)

  def lower(text):
      return text.lower()

  return white_space_fix(remove_articles(remove_punc(lower(s))))

def EM(answer, key) -> bool:
    return normalize_answer(answer) == normalize_answer(key)


