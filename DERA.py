import openai
import time


with open('./Med-QA/Dev.jsonl', 'r', encoding='utf-8') as f:
    
    questions = []
    for line in f:
        data = json.loads(line)
        question = data['question_open']
        questions.append(question)
# 读入prompt_tepmplate的json文件
with open('./prompt_template.json', 'r', encoding='utf-8') as f:
    prompt_template = json.load(f)
system_prompt = prompt_template['system']
QA_template = prompt_template['QA']
# 进行对话
# 遍历每一个question
for question in questions:
    # 根据模板，根据占位符'{question}'放入问题
    INIT_prompt = QA_template['INIT']["prompt"].replace('{question}', question)
    # To generate an initial answer for DERA to discuss, we use a single-shot prompt which outputs a short answer,We adopt this approach by running 5 completions of our single-shot prompt and selecting the answer with the most votes as the single-shot answer, and consider this as our baseline,using chatGPT by OpenAI.
    for i in range(5):
        answer_list = []
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # here we use `gpt-3.5-turbo` model, while Stanford-Alpaca uses `text-davinci-003`
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": INIT_prompt},
            ]
        )
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)
        if response:
            generated_text = response.choices[0].text.strip()
            json.dump({'prompt': INIT_prompt, 'generated_text': generated_text}, f)
        else:
            generated_text = ''
        # 储存生成的文本到一个列表里面
        answer_list.append(generated_text)
        # 选择出现次数最多的答案
    answer = max(answer_list, key=answer_list.count)
    # 根据模板DESIDER_INIT = QA_template['DESIDER_INIT']，根据占位符'{question}'放入问题.'{options_filtered_str}'占位符要放入answer_list通过','连接之后的字符串元素，{relative_likelihood}放入对应元素的相对可能性，通过这个元素出现的次数除以answer_list的总长度来计算
    options_filtered_str = ','.join(answer_list)
    relative_likelihood = answer_list.count(answer) / len(answer_list)
    DECIDER_INIT_prompt = QA_template['DECIDER_INIT']["prompt"].replace('{question}', question).replace('{options_filtered_str}', options_filtered_str).replace('{relative_likelihood}', str(relative_likelihood))
    # Starting with the initial Decider message, bothDecider (Prompt 17) and Researcher have access only to the question and their own conversation as they iteratively discuss the problem and attempt to achieve the right answer. The Researcher can stop the dialogue when they have exhausted all relevant information, otherwise, it is set to end after n = 3turns. At each turn, the Decider must state what their current answer is and explain their reasoning, and they may choose to either confirm or change their answer.
    #从初始的Decider消息开始，Decider（提示17）和Researcher都只能访问问题和他们自己的对话，他们迭代地讨论问题并尝试获得正确的答案。当研究人员用尽了所有相关信息时，研究人员可以停止对话，否则，它将在n = 3turns后结束。在每一轮中，Decider必须说明他们当前的答案是什么以及他们的推理，并且他们可以选择确认或更改他们的答案.
    # 进行最多3轮的对话
    CHAT_HISTORY = []
    last_teacher_message = ''
    last_student_message = ''
    # 只有被使用过的last_teacher_message和last_student_message才会被放入到CHAT_HISTORY里面
    for turn in range(3):
        # 根据模板，根据占位符'{question}'和'{answer}'放入问题和答案
        ## 如果是第一轮，DECIDER_TURN_prompt = DECIDER_INIT_prompt
        
        if turn == 0:
            DECIDER_TURN_prompt = DECIDER_INIT_prompt
        ## 否则，DECIDER_TURN_prompt = DECIDER_TURN_prompt.replace('{answer}', answer)
        else:
            DECIDER_TURN_prompt = QA_template['DECIDER']["prompt"].replace('{question}', question).replace('{chat_history}',''.join(CHAT_HISTORY)).replace('{last_teacher_message}', last_teacher_message)
        if last_teacher_message=='STOP':
            DECIDER_TURN_prompt = QA_template['DECIDER_FINAL']["prompt"].replace('{question}', question).replace('{chat_history}',''.join(CHAT_HISTORY)).replace('{last_teacher_message}', last_teacher_message)
        # Decider and Researcher have access only to the question and their own conversation as they iteratively discuss the problem and attempt to achieve the right answer.
        # Decider和Researcher只能访问问题和他们自己的对话，他们迭代地讨论问题并尝试获得正确的答案。使用chatGPT模型
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # here we use `gpt-3.5-turbo` model, while Stanford-Alpaca uses `text-davinci-003`
                messages=[
                    {"role": "system", "content": DECIDER_INIT_prompt},
                    {"role": "user", "content": DECIDER_TURN_prompt},
                ]
            )
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)
        if response:
            generated_text = response.choices[0].text.strip()
        else:
            generated_text = ''
        last_student_message = generated_text

        if last_teacher_message:
            CHAT_HISTORY.append(last_teacher_message)



        DECIDER_message = generated_text
        if last_teacher_message=='STOP':
            break
        # Researcher has access only to the question and their own conversation as they iteratively discuss the problem and attempt to achieve the right answer.
        # Researcher只能访问问题和他们自己的对话，他们迭代地讨论问题并尝试获得正确的答案。使用chatGPT模型
        RESEARCHER_propmt = QA_template['RESEARCHER']["prompt"].replace('{question}', question).replace('{chat_histyory}', '\n'.join(CHAT_HISTORY)).replace('{last_student_message}', DECIDER_message)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # here we use `gpt-3.5-turbo` model, while Stanford-Alpaca uses `text-davinci-003`
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": DECIDER_message},
                ]
            )
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)
        if response:
            generated_text = response.choices[0].text.strip()
        else:
            generated_text = ''
        
        last_teacher_message = generated_text
        RESEARCHER_message = generated_text
        CHAT_HISTORY.append(DECIDER_message)
        
        #进入下一轮对话
            