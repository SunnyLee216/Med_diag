from langchain.prompts import PromptTemplate

# DDX
RANK_PROMPT ="""Given the following medical question , respond with the phrase that best answers the question.
Imagine you are an senior doctor. Based on the previous dialogue, what is the diagnosis? Based on the above conversation, rank the following diseases according to their likelihood of diagnosis. For example, patients are more likely to be diagnosed with disease A than disease B, and disease A should be ranked first in disease B, and so on. 
Here are some examples:
{examples}
(END OF EXAMPLES)

Here is the information of a new patient:
{information}
The list of diseases is as follows:
{diag_list}
RANK:
"""
CHOOSE_PROMPT ="""Imagine you are an senior doctor. Based on the previous dialogue, what is the diagnosis? Based on the above conversation, choose the most likely diagnosis from the following list.

"""

# Here are some examples:
# {examples}
# (END OF EXAMPLES)
## TODO add examples
RETHINK_PROMPT ="""You are an advanced medical reasoning agent that can improve based on self refection. 
{examples}
(END OF EXAMPLES)
Here is the information of a new patient:
{information}
Based on the above conversation, rank the following diseases according to their likelihood of diagnosis. For example, patients are more likely to be diagnosed with disease A than disease B, and disease A should be ranked first in disease B, and so on.
The previous ranking of diseases is as follows:
{previous_rank}
This is the knowledge of the {top1_diag}:
{top1_knowledge}
You previously thought that {top1_diag} was one the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is one of the most likely diagnosis.
Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
You should ANSWER:YES/NO and your EXPLANATION for the ANSWER you output.
-output format:
ANSWER:(YES/NO)
EXPLANATION:(Your explanation for whether the {top1_diag} is valid.)

ANSWER:
"""
RERANK_PROMPT ="""You are an advanced medical reasoning agent that can improve based on self refection. 

Here is the information of a new patient:
{information}
Based on the above conversation, rank the following diseases according to their likelihood of diagnosis. For example, patients are more likely to be diagnosed with disease A than disease B, and disease A should be ranked first in disease B, and so on.
The previous ranking of diseases is as follows:
{previous_rank}
This is the knowledge of the {top1_diag}:
{top1_knowledge}
You previously thought that {top1_diag} was one the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is one of the most likely diagnosis.
Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
You should ANSWER:YES/NO and your EXPLANATION for the ANSWER you output.
-output format:
ANSWER:(YES/NO)
EXPLANATION:(Your explanation for whether the {top1_diag} is valid.)

ANSWER:
"""
# top1_diag 不是top1_diag
# You previously thought that {top1_diag} was one of the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is the one of the most likely diagnosis.

RETHINK_PROMPT2 ="""You are an advanced medical reasoning agent that can improve based on self refection. You will be given a previous answer and the knowledge of  disease. You need to reconsider diagnosis based on the patient's information and the knowledge.
Here is the information of a new patient:
{information}
Imagine you are an senior doctor. Based on the previous dialogue, what is the diagnosis? 
Select from the following list:
{diag_set}
Your previous answer for the diagnosis is as follows:
{top1_diag}
This is the knowledge of the {top1_diag}:
{top1_knowledge}
You previously thought that {top1_diag} was one the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is one of the most likely diagnosis.
You should EXPLAIN for the diagnosis you output. You need to focus on the Severity of Symptoms,Diagnostic Coherence,Explanation Comprehensiveness,Alignment with Current Medical Knowledge.
-EXPLANATION should be brief!
-If ANSWER: YES, you must explain the diagnosis:{top1_diag}
-If ANSWER: NO, you must choose ANOTHER DIAGNOSIS(another most likely diagnosis from the list:{diag_set}.)
-THOUGHT : Your reasoning for the current diagnosis and the another diagnosis.
-output format:
'''
TOUGHT:....
ANSWER: YES
EXPLANATION: Your explanation for the diagnosis.
ANOTHER DIAGNOSIS: None
or
TOUGHT:....
ANSWER: NO
EXPLANATION: Your explanation for the diagnosis.
ANOTHER DIAGNOSIS: Your diagnosis(if you think the currtent diagnosis is not valid, you can choose another diagnosis from the list.)
'''
"""


DECIDER_CHOOSE="""Given the following medical question, respond with the phrase that best answers the question.
Imagine you are an senior doctor. Based on the previous dialogue, what is the diagnosis? Select the most likely diagnosis from the following list.
EXAMPLES:
{examples}
(END OF EXAMPLES)
Here is the information of a new patient:
{information}
The list of diseases is as follows:
{diag_list}
Select the most likely diagnosis from the following list.
ANSWER:
"""
DECIDER_INIT="""{question}
{options_filtered_str}
You think the relative likelihood of each option is {relative_likelihood}. Write a 3 -4 sentence message explaining why you rate the options in that way , without taking a decisive stand.
Message:
"""
DECIDER_PROMPT="""You are an expert doctor who is trying to select the answer to a medical question, and is willing to be open - minded about their answer. The questions are taken from a short - answer medical exam , and your role is to arrive at the correct answer.
You are chatting with an expert medical advisor, who will try to help you think through the problem, but will not directly tell you the answer . They will help you by pointing out aspects of the question that are important in finding the answer . Do not assume that the teacher knows the answer ; only that they know how to think through the question. You can change your answer at any point , but do not assume that the expert knows the exact answer and is providing leading questions . Think about their guidance as a whole , and do not only respond to their last message.
Question : {question}
The previous discussion between you and the expert advisor is as follows ;
{chat_history}
{last_teacher_message}
Rethink the question by considering what the teacher pointed out, in light of your original hypothesis. Remember they do not know the answer , but only how to think through the question . You can change your mind on the correct answer, but remember that unless the question explicitly asks for multiple answers , you can only provide a single answer . Respond with the option you believe most likely to be the right answer ("Answer :< SHORT ANSWER >") and a response to that message ("Response :< MESSAGE >")
Answer:
"""
DECIDER_FINAL = """You are an expert doctor who is trying to select the answer to a medical question, and is willing to be open - minded about their answer. The questions are taken from a short - answer medical exam , and your role is to arrive at the correct answer.
You are chatting with an expert medical advisor, who will try to help you think through the problem, but will not directly tell you the answer . They will help you by pointing out aspects of the question that are important in finding the answer . Do not assume that the teacher knows the answer ; only that they know how to think through the question. You can change your answer at any point , but do not assume that the expert knows the exact answer and is providing leading questions . Think about their guidance as a whole , and do not only respond to their last message.
Question : {question}
The previous discussion between you and the expert advisor is as follows ;
{chat_history}
{last_teacher_message}
Rethink the question by considering what the teacher pointed out, in light of your original hypothesis. Remember they do not know the answer , but only how to think through the question . You can change your mind on the correct answer, but remember that unless the question explicitly asks for multiple answers , you can only provide a single answer . Respond with the option you believe most likely to be the right answer (" Answer :< SHORT ANSWER >").
Answer:
"""
TEACHER_PROMPT="""
You are an expert medical doctor who is guiding a medical student through thinking about which of several answers is best for a given question. You cannot give the student the answer. Your role is to help the student think through the question , specifically by pointing out portions of the question that are important in understanding the problem.
Rules ;
- All responses should include a quote from the question.
- Consider what you , as the teacher , have said in the previous conversation , and do not repeat yourself.
- Responses should be at most 4 sentences long .
- Stop only when you , as the teacher , have pointed out all important aspects of the question in the previous discussion. To stop , respond with 'STOP ' at the next turn.
You cannot ;
- Directly give the answer to the student
- Include the correct option in your response , or any paraphrasing of the correct answer.
- Do not narrow down the options in your response.
Question : {question}
The previous discussion between you and the expert advisor is as follows ;
{chat_history}
{last_student_message}
Help the student find the correct answer by pointing out specific parts of the questions they need to think through, but do not include the correct phrase in your response. Your response should be no more than 3 -4 sentences . If you have pointed out all challenging aspects of the question in the previous conversation , respond with " STOP " after the student 's next turn.
Response:
"""
RETHINK_PROMPT_TEST="""You are an advanced medical reasoning agent that can improve based on self refection. You will be given a previous ranking of diseases and the knowledge of the top 1 disease. You need to reconsider whether the top 1 disease is the most likely diagnosis based on the patient's information and the knowledge of the top 1 disease.

Here is the information of a new patient:
{information}
Based on the above conversation, rank the following diseases according to their likelihood of diagnosis. For example, patients are more likely to be diagnosed with disease A than disease B, and disease A should be ranked first in disease B, and so on.
Your previous ranking of diseases is as follows:
{previous_rank}
This is the knowledge of the {top1_diag}:
{top1_knowledge}
You previously thought that {top1_diag} was one of the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is the most likely diagnosis.
Regardless of whether external knowledge exists or not, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
You should ANSWER:YES/NO and your EXPLANATION for the ANSWER you output. 
-EXPLANATION should be brief!
-output format:
ANSWER:(YES/NO)
EXPLANATION:(Your explanation for whether the {top1_diag} is valid.)

ANSWER:
"""


#Provide a brief justification for each assigned score, highlighting the key factors that influenced your evaluation.
SCORE ="""As a medical score agent, please evaluate the following patient's diagnosis and explanation using the provided scoring system. Consider each of the four indicators: Diagnostic Coherence, Severity of Symptoms, Explanation Comprehensiveness, and Alignment with Current Medical Knowledge. Assign a score between 1 and 5 for each indicator, where 1 represents poor performance and 5 represents excellent performance. After evaluating each indicator, calculate the total score by summing the individual scores.
-Diagnostic Coherence: Assess the coherence between the patient's condition and the provided explanation. This includes how well the explanation accounts for the patient's symptoms, medical history, and risk factors. Score range: [1 - 5]
-Severity of Symptoms: Evaluate the severity of the patient's symptoms in comparison to the typical presentation of the diagnosed condition. This helps differentiate between mild, moderate, and severe cases. Score range: [1 - 5]
-Explanation Comprehensiveness: Assess how comprehensive the explanation is in terms of addressing all relevant aspects of the patient's condition, including potential complications, treatment options, and preventive measures. Score range: [1 - 5]
-Alignment with Current Medical Knowledge: Determine how well the diagnosis and explanation align with the current state of medical knowledge and research. Score range: [1 - 5]
Here are some examples:
{examples}
(END OF EXAMPLES)

RATE FOR THE NEW PATIENT,YOU SHOULD BE CRTICAL AND GIVE A SCORE RANGE FROM 0 TO 5:
Patient condition: {information}
Diagnostic result: {disease}
Explanation: {explanation}
Scoring:
"""

SUMMARIZE ="""Summarize important symptoms or other important information that are helpful for doctor to diagnose based on the paragraph. Brief in 3-4 sentences.
Paragraph:
{paragraph}.
"""



# 输入各种prompt
REACT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the last passage successfully found by Search.
(3) Finish[answer], which returns the answer and finishes the task.
You may take as many steps as necessary.
Here are some examples:
{examples}
Question: {question}{scratchpad}"""


REACT_REFLECT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the last passage successfully found by Search.
(3) Finish[answer], which returns the answer and finishes the task.
You may take as many steps as necessary.
Here are some examples:
{examples}
(END OF EXAMPLES)

{reflections}

Question: {question}{scratchpad}"""

REFLECTION_HEADER = 'You have attempted to answer following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'

REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an Docstore API environment and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>], or you used up your set number of reasoning steps. In a few sentences, Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.  
Here are some examples:
{examples}

Previous trial:
Question: {question}{scratchpad}

Reflection:"""

rank_agent_prompt = PromptTemplate(
                        input_variables=["examples", "information", "diag_list"],
                        template = RANK_PROMPT,
                        )
rethink_agent_prompt = PromptTemplate(
                        input_variables=["examples","information","previous_rank", "top1_knowledge","top1_diag"],
                        template = RETHINK_PROMPT,
                        )
rethink_agent_prompt2 = PromptTemplate(
                        input_variables=["information", "diag_set","top1_knowledge","top1_diag"],
                        template = RETHINK_PROMPT2,
                        )
rethink_agent_prompt3 = PromptTemplate(
                        input_variables=["information","previous_rank", "top1_knowledge","top1_diag"],
                        template = RETHINK_PROMPT_TEST,
                        )
score_agent_prompt = PromptTemplate(
                        input_variables=["examples","information", "disease",  "explanation"],
                        template=SCORE,
                        )

decider_init_prompt = PromptTemplate(
                        input_variables=['question','options_filtered_str','relative_likelihood'],
                        template=DECIDER_INIT,
                        )
decider_prompt = PromptTemplate(
                        input_variables=['question','chat_history','last_teacher_message'],
                        template=DECIDER_PROMPT,
                        )
decider_final_prompt = PromptTemplate(
                        input_variables=['question','chat_history','last_teacher_message'],
                        template=DECIDER_FINAL,
                        )
teacher_prompt = PromptTemplate(
                        input_variables=['question','chat_history','last_student_message'],
                        template=TEACHER_PROMPT,
                        )

summarize_prompt = PromptTemplate(
                        input_variables=["paragraph"],
                        template=SUMMARIZE,
)
react_agent_prompt = PromptTemplate(
                        input_variables=["examples", "question", "scratchpad"],
                        template = REACT_INSTRUCTION,
                        )

react_reflect_agent_prompt = PromptTemplate(
                        input_variables=["examples", "reflections", "question", "scratchpad"],
                        template = REACT_REFLECT_INSTRUCTION,
                        )

reflect_prompt = PromptTemplate(
                        input_variables=["examples", "question", "scratchpad"],
                        template = REFLECT_INSTRUCTION,
                        )
