import openai
import json
import time
import requests
import pandas as pd

df = pd.read_csv('ddxplus.csv')


openai.api_key = "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"



MAX_EPOCH = 2
K = 5
# 三种模式'baseline','self-consistency','knowledge-consistency'
MODE = 'self-consistency'
url = 'http://127.0.0.1:3000/search'
system_prompt = 'You are an auxiliary diagnostic system, and you will answer question based on the dialogue information.'
corret = 0


ddx_search = {}
# 载入ddx_search.json文件 作为知识库
with open('dis_responses.json', 'r', encoding='utf-8') as f:
    ddx_search = json.load(f)
    # 把所有的疾病名字转换成小写
    ddx_search = {k.lower(): v for k, v in ddx_search.items()}
# 定义一个函数，用来生成知识，减少重复代码，并储存到一个字典中，key是query，value是response_text和source_text，如果有重复的query，就不再请求
def generate_knowledge(query):
    # 先从ddx_search中查找，如果有，就直接返回
    
    if query in ddx_search:
        return ddx_search[query]
    else:
        query = 'the evidence of {dis}'.replace('{dis}',query)
        # 用requests请求searchGPT，得到response_text和source_text
        response = requests.post(url, data={'query': query})
        response_text = response.json()['response_text']
        source_text = response.json()['source_text']
        ddx_search[query] = {'response_text': response_text, 'source_text': source_text}
        return ddx_search[query]

# 定义一个函数，用来生成对话，减少重复代码
def generate_dialogue(prompt,histories=None):
    # 如果有知识，就把知识加到prompt中
    # 从histories中拆解出对话信息，加入到message中
    
    # if histories:
    #     message = [{"role": "system", "content": system_prompt}]
    #     # 除了system_prompt，第一个为用户的输入，第二个为系统的回复，以此类推，轮流加入message建立完整的message
    #     for i in range(len(histories)):
    #         if i % 2 == 0:
    #             message.append({"role": "user", "content": histories[i]})
    #         else:
    #             message.append({"role": "assistant", "content": histories[i]})
    # else:
    #     message = [ {"role": "user", "content": prompt}]
    message = [ {"role": "user", "content": prompt}]
    # 调用openai的api生成对话
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=message,
                temperature= 0,
                max_tokens= 2048,

              )
    return response

def score_prompt(prompt, histories=None):
    # 读入prompt模板，根据占位符替换成对应的内容
    pass

# 读入prompt模板的json文件，根据占位符替换成对应的内容
with open('prompt_template.json', 'r', encoding='utf-8') as f:
    prompt_template = json.load(f)

one_shot_prompt = ''
correct = 0

# 处理每一个病人
for index, row in df.iterrows():
    # 跳过第一个病人，因为他的信息要作为例子
    if index == 0:
        one_shot_prompt += 'Here is the information of the patient: ' + row['Information'] + 'Imagine you are an intern doctor. Based on the previous dialogue, what is the best diagnosis? '+ '\nANSWER:'+ row['Diagnosis'] +'\n'
        continue

    print('Processing patient {}'.format(index))
    # 按照处理的模式生成对话，如果模式是'baseline'，则只生成一次对话，如果模式是'self-consistency'，则生成五次对话,如果模式是'knowledge'，则生成五次对话加上知识对话
    histories = []
    # 为了防止报错，加入一个异常处理，如果出现异常，就休息30秒，然后继续
    # 有选项的问题
    # question= 'Here is the information of the patient: ' + row['Information'] + 'Imagine you are an intern doctor. Based on the previous dialogue, what is the diagnosis? Select one answer among the following lists:'+ row['Diag_Set']
    # 没有选项的问题
    question = 'Here is the information of the patient: ' + row['Information'] + 'Imagine you are an intern doctor. Based on the previous dialogue, what is the best diagnosis?'
    

    if MODE == 'baseline':
        # baseline不需要记录history
        # 调用chatGPT，生成对话
        # 生成提问的prompt
        
        prompt = prompt_template['ddx_plus']['Question']['prompt'].replace('{one_shot_prompt}', one_shot_prompt).replace('{question}', question)
        response = generate_dialogue(prompt)
        print(response['choices'][0]['message']['content'])
        # 处理结果
        # 从结果中找到ANSWER:，然后找到下一个换行符，中间的内容就是答案
        answer = response['choices'][0]['message']['content']

    elif MODE == 'self-consistency':
        # 对一个病人询问五次，并统计这些答案的相对频率，以频率最高的答案作为最终的答案
        answer_list = []
        prompt = ''
        prompt = prompt_template['ddx_plus']['Question']['prompt'].replace('{one_shot_prompt}', one_shot_prompt).replace('{question}', question)
        for i in range(K):
            # 调用chatGPT，生成对话
            # 生成提问的prompt
            # 防止报错，加入异常处理
            try:
                response = generate_dialogue(prompt)
            except:
                print('Error happens, sleep for 30 seconds')

                time.sleep(30)
                response = generate_dialogue(prompt)
            

            # 处理结果
            # 从结果中找到ANSWER:，然后找到下一个换行符，中间的内容就是答案
            answer = response['choices'][0]['message']['content']
            print(answer)
            answer_list.append(answer)
        # 统计答案的相对频率
        answer_dict = {}
        for answer in answer_list:
            if answer not in answer_dict:
                answer_dict[answer] = 1
            else:
                answer_dict[answer] += 1
        # 找到频率最高的答案
        answer = max(answer_dict, key=answer_dict.get)
    
    elif MODE == 'knowledge':
        # 对一个病人询问五次，并统计这些答案的相对频率，以频率最高的答案作为最终的答案
        answer_list = []
        prompt = ''
        prompt = prompt_template['ddx_plus']['Question']['prompt'].replace('{one_shot_prompt}', one_shot_prompt).replace('{question}', question)

        # 建立字典来记录每一个对话的历史
        K_history = {}
        for i in range(K):
            # 调用chatGPT，生成对话
            # 生成提问的prompt
            
            try:
                response = generate_dialogue(prompt)
            except:
                print('Error happens, sleep for 30 seconds')
                time.sleep(30)
                response = generate_dialogue(prompt)
            # 处理结果
            # 从结果中找到ANSWER:，然后找到下一个换行符，中间的内容就是答案
            answer = response['choices'][0]['message']['content'].split('\n')[0]
            answer_list.append(answer)

            # 保存第K次对话的历史，包括用户prompt提问和系统的回复
            
        
        # 统计答案的相对频率
        answer_dict = {}
        for answer in answer_list:
            if answer not in answer_dict:
                answer_dict[answer] = 1
            else:
                answer_dict[answer] += 1
        # 计算每一个答案的相对频率
        for answer in answer_dict:
            answer_dict[answer] = answer_dict[answer]/K

        # 逐一对答案进行验证，把知识加入到对话中，
        for answer in answer_dict:
            # 生成对话历史：
            # histories = []
            # histories.append(prompt)
            # histories.append('ANSWER:'+answer)
            knowlege_prompt = generate_knowledge(answer)
            if knowlege_prompt:
                # 如果知识不为空，就把知识加入到对话中，并且把知识的长度限制在2048以内
                knowlege_prompt= knowlege_prompt[:2048]
                prompt = prompt_template['ddx_plus']['prompt'].replace('{knowledge}', knowlege_prompt).replace('{question}', question).replace('{answer}',answer)
            else:
                print('No knowledge found for answer:{}'.format(answer))
                prompt = prompt_template['ddx_plus']['prompt'].replace('{knowledge}', '').replace('{question}', question).replace('{answer}',answer)

            response = generate_dialogue(prompt)
            # 处理结果
            response = response['choices'][0]['message']['content']
            print(response)


            # 从结果中找到ANSWER:，然后找到下一个换行符，中间的内容就是答案
            answer = response.split('ANSWER:')[1].split('\n')[0]

            # 从结果中找到RATIONALE:，然后找到下一个换行符，中间的内容就是答案
            rationale = response.split('RATIONALE:')[1].split('\n')[0]
            print('answer:{}, rationale:{}'.format(answer, rationale))
            # answer.
            if answer.lower() == 'no':
                answer_dict[answer] = 0
            else:
                # answer_dict[answer] = answer_dict[answer]*float(rationale)
                # TODO:这里可以根据rationale的值来调整答案的相对频率
                pass
        # 找到频率最高的答案
        answer = max(answer_dict, key=answer_dict.get)
        print(answer_dict)
        print(answer)

    else:
        raise ValueError('MODE should be one of baseline, self-consistency, knowledge')

    
        
    time.sleep(3)
    # 保存结果,统计对错
    if answer.lower() == row['Diagnosis'].lower() or row['Diagnosis'].lower() in answer.lower():
        correct += 1

        
        
# 输出正确率
print('correct rate:',correct/(len(df)-1))
        

        



