import openai
import json


import pandas as pd

df = pd.read_csv('ddxplux.csv')


openai.api_key = "YOUR_API_KEY"
import pandas as pd


MAX_EPOCH = 2
K = 5
MODE = 'baseline'
system_prompt = f'You are an auxiliary diagnostic system, and you will answer question based on the dialogue information.'
corret = 0



# 载入ddx_search.json文件 作为知识库
with open('ddx_search.json', 'r', encoding='utf-8') as f:
    ddx_search = json.load(f)

def generate_knowledge(diagnosis):
    # 从ddx_search中找到对应的疾病的知识
    # 要先查看疾病名字是否在ddx_search中，如果不在，就返回空字符串
    if diagnosis not in ddx_search:
        return ''
    # 如果在，就返回对应的知识
    else:
        return ddx_search[diagnosis]['source_text']

# 定义一个函数，用来生成对话，减少重复代码
def generate_dialogue(prompt,histories=None):
    # 如果有知识，就把知识加到prompt中
    # 从histories中拆解出对话信息，加入到message中
    if histories:
        message = [{"role": "system", "content": system_prompt}]
        # 除了system_prompt，第一个为用户的输入，第二个为系统的回复，以此类推，轮流加入message建立完整的message
        for i in range(len(histories)):
            if i % 2 == 0:
                message.append({"role": "user", "content": histories[i]})
            else:
                message.append({"role": "assistant", "content": histories[i]})
    else:
        message = [{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}]
    
    # 调用openai的api生成对话
    response =  response = openai.ChatCompletion.create(
                engine="gpt-3.5-turbo",
                messages=message,
                temperature= 0,
                max_tokens= 2048

              )
    return response

def score_prompt(prompt, histories=None):
    # 读入prompt模板，根据占位符替换成对应的内容
    pass



one_shot_prompt = ''
with open('output.json', 'w') as f:
    # 处理每一个病人
    for index, row in df.iterrows():
        # 跳过第一个病人，因为他的信息要作为例子
        if index == 0:
            one_shot_prompt += 'Here is the information of the patient: ' + row['Infomation'] + 'Imagine you are an intern doctor. Based on the previous dialogue, what is the diagnosis? Select one answer among the following lists:'+ row['Diag_set'] +'\nANSWER:'+ row['Diagnosis'] +'\n'
            continue
        
        # 按照处理的模式生成对话，如果模式是'baseline'，则只生成一次对话，如果模式是'self-consistency'，则生成五次对话,如果模式是'knowledge'，则生成五次对话加上知识对话
        histories = []
        if MODE == 'baseline':
            # baseline不需要记录history
            # 调用chatGPT，生成对话
            # 生成提问的prompt
            prompt = ''
            prompt += one_shot_prompt
            prompt = 'Here is the information of the patient: ' + row['Infomation'] + 'Imagine you are an intern doctor. Based on the previous dialogue, what is the diagnosis? Select one answer among the following lists:'+ row['Diag_set']
            
            response = generate_dialogue(prompt)
            # 处理结果
            # 从结果中找到ANSWER:，然后找到下一个换行符，中间的内容就是答案
            answer = response['choices'][0]['message']['content'].split('ANSWER:')[1].split('\n')[0]
        elif MODE == 'self-consistency':
            # 对一个病人询问五次，并统计这些答案的相对频率，以频率最高的答案作为最终的答案
            answer_list = []
            for i in range(K):
                # 调用chatGPT，生成对话
                # 生成提问的prompt
                prompt = ''
                prompt += one_shot_prompt
                prompt = 'Here is the information of the patient: ' + row['Infomation'] + 'Imagine you are an intern doctor. Based on the previous dialogue, what is the diagnosis? Select one answer among the following lists:'+ row['Diag_set']
                
                response = response = generate_dialogue(prompt)
                # 处理结果
                # 从结果中找到ANSWER:，然后找到下一个换行符，中间的内容就是答案
                answer = response['choices'][0]['message']['content'].split('ANSWER:')[1].split('\n')[0]
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
            prompt += one_shot_prompt
            prompt = 'Here is the information of the patient: ' + row['Infomation'] + 'Imagine you are an intern doctor. Based on the previous dialogue, what is the diagnosis? Select one answer among the following lists:'+ row['Diag_set']
            # 建立字典来记录每一个对话的历史
            K_history = {}
            for i in range(K):
                # 调用chatGPT，生成对话
                # 生成提问的prompt
                
                response = response = generate_dialogue(prompt)
                # 处理结果
                # 从结果中找到ANSWER:，然后找到下一个换行符，中间的内容就是答案
                answer = response['choices'][0]['message']['content'].split('ANSWER:')[1].split('\n')[0]
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
                histories = []
                histories.append(prompt)
                histories.append('ANSWER:'+answer)
                knolege_prompt = generate_knowledge(answer)
                prompt = 'The evidence of' + answer + 'is' + knolege_prompt + 'You should rethink the answer whether it is correct. You should ANSWER:YES/NO and your RATIONALE.\n' + 'ANSWER:\nRATIONALE:\n'
                response = generate_dialogue(prompt,histories=histories)
                # 处理结果
                response = response['choices'][0]['message']['content']
                # 从结果中找到ANSWER:，然后找到下一个换行符，中间的内容就是答案
                answer = response.split('ANSWER:')[1].split('\n')[0]
                # 从结果中找到RATIONALE:，然后找到下一个换行符，中间的内容就是答案
                rationale = response.split('RATIONALE:')[1].split('\n')[0]

        # 保存结果
        
        
# 输出正确率
print(f"Accuracy: {correct/len(df)}")
        

        



