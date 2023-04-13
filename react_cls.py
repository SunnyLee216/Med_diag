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
from prompts import rank_agent_prompt,rethink_agent_prompt,score_agent_prompt,summarize_prompt,REFLECTION_HEADER
from fewshots import  REFLECTIONS,RANK_FEW_SHOTS,RETHINK_FEW_SHOTS,SCORE_FEW_SHOTS
import json

    
class Rank_agent:
    def __init__(self):
        self.llm = OpenAI(
            temperature=0,
            max_tokens=1000,
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
            max_tokens=4096,
            model_name="gpt-3.5-turbo",
            model_kwargs={"stop": "\n"},
        )
        self.score_prompt = score_agent_prompt
        self.examples = SCORE_FEW_SHOTS
    def score(self,row,previous_rank,top1_knwledge,rationale):
        return self.llm(self.build_agent_prompt(row,previous_rank,top1_knwledge,rationale)).strip('\n').strip()
    def build_agent_prompt(self,row,previous_rank,top1_knwledge,rationale):
        return self.score_prompt.format(
                            examples = self.examples,
                            information = row['Information'],
                            previous_rank = previous_rank,
                            top1_knowledge = top1_knwledge,
                            Rationale = rationale
                            )
class Rethink_agent:
    def __init__(self) -> None:
        self.llm = OpenAI(
            temperature=0,
            max_tokens=1000,
            model_name="gpt-3.5-turbo",
            model_kwargs={"stop": "\n"},
        )
        self.rethink_prompt = rethink_agent_prompt
        self.examples = RETHINK_FEW_SHOTS
    def rethink(self,row,previous_rank,top1_knwledge):
        return self.llm(self.build_agent_prompt(row,previous_rank,top1_knwledge)).strip('\n').strip()
    def build_agent_prompt(self,row,previous_rank,top1_knwledge):
        return self.rethink_prompt.format(
                            examples = self.examples,
                            diag_list = row['Information'],
                            previous_rank = previous_rank,
                            top1_knowledge = top1_knwledge)
        
class Knowledge_agent:
    def __init__(self,url='http://127.0.0.1:3000/search', path="dis_responses.json",max_steps = 6):
        self.url = url
        self.llm = OpenAI(
            temperature=0,
            max_tokens=1000,
            model_name="gpt-3.5-turbo",

        )
        self.max_steps = max_steps  
        self.step_n = 1
        self.knowledge = self.load_local_knowledge(path)
        self.summarize_prompt = summarize_prompt
    def serach(self, question):
        '''根据问题，返回答案'''
        # question = "The evidence of Pnuemonia?"
        if question.lower() in self.knowledge:
            return self.knowledge[question.lower()]['response_text']
        else:
            question = "The evidence of "+question+"?"
            response = requests.post(self.url, data={'query': question})
            response_text = response.json()['response_text']
            # source_text = response.json()['source_text']
            return response_text
    
    def summarize(self, text):
        '''对文本进行摘要'''
        try:
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
        except Exception as e:
            print(e)
            print('加载本地知识库失败')
            self.knowledge = {}
        return self.knowledge

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

