from langchain.prompts import PromptTemplate

# DDX
RANK_PROMPT ="""Imagine you are an senior doctor. Based on the previous dialogue, what is the diagnosis? Based on the above conversation, rank the following diseases according to their likelihood of diagnosis. For example, patients are more likely to be diagnosed with disease A than disease B, and disease A should be ranked first in disease B, and so on. 
Here are some examples:
{examples}
(END OF EXAMPLES)

Here is the information of a new patient:
{information}
The list of diseases is as follows:
{diag_list}
RANK:
"""


# Here are some examples:
# {examples}
# (END OF EXAMPLES)
## TODO add examples
RETHINK_PROMPT ="""You are an advanced medical reasoning agent that can improve based on self refection. You will be given a previous ranking of diseases and the knowledge of the top 1 disease. You need to reconsider whether the top 1 disease is the most likely diagnosis based on the patient's information and the knowledge of the top 1 disease.
Here is the information of a new patient:
{information}
Based on the above conversation, rank the following diseases according to their likelihood of diagnosis. For example, patients are more likely to be diagnosed with disease A than disease B, and disease A should be ranked first in disease B, and so on.
The previous ranking of diseases is as follows:
{previous_rank}
This is the knowledge of the top 1 diseases:
{top1_knowledge}
You previously thought that {top1_diag} was the most likely diagnosis, but now you need to combine the patient's condition and knowledge to determine whether this disease is the most likely diagnosis.
Regardless of whether external information exists, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid(if valid:YES; unvalid:NO). You can change your answer at any point.
You should ANSWER:YES/NO and your EXPLANATION for the ANSWER you output.
-output format:
ANSWER:(YES/NO)
EXPLANATION:(Your explanation for whether the {top1_diag} is valid.)

ANSWER:
"""



SCORE ="""You are a medical score agent. You need to score based on Patient's condition and Explanation. Regardless of any other thing, you just need to socre. Learn from the Examples to rate new patients.
Example1: /start
Patient condition: Age: 26; Sex: M; Initial evidence: Do you constantly feel fatigued or do you have non-restful sleep? Yes; Evidence: ; Do you have a poor diet? Yes; Do you have any family members who have been diagnosed with anemia? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: tugging; Characterize your pain: a cramp; Characterize your pain: exhausting; Do you feel pain somewhere? forehead; How intense is the pain? 5; Does the pain radiate to another location? nowhere; How precisely is the pain located? 2; How fast did the pain appear? 0; Are you experiencing shortness of breath or difficulty breathing in a significant way? Yes; Do you feel lightheaded and dizzy or do you feel like you are about to faint? Yes; Do you constantly feel fatigued or do you have non-restful sleep? Yes; Do you have chronic kidney failure? Yes; Have you recently had stools that were black (like coal)? Yes; Are you taking any new oral anticoagulants ((NOACs)? Yes; Is your skin much paler than usual? Yes; Have you traveled out of the country in the last 4 weeks? N; Is your BMI less than 18.5, or are you underweight? Yes.
Diagnostic result: urti.
Explanation: Based on the patient's symptoms of diffuse muscle pain, increased sweating, pain in the back of head, side of neck, and temple, along with fatigue, chills, and a rash on the forehead, it is more likely that the patient is suffering from influenza rather than urti. Cluster headache and anemia do not align with the patient's symptoms.
Give your score. output the format:
[
Scores(range: [1 - 5]): 
,Consistency: Diagnosis result consistent with the Explanation. score:1
,Explanation's valid. score:5
,adequacy of Explanation for Diagnosis result. score:1
]
TOTAL_SCORE: 7
Example1: /end

Example2: /start
Patient condition: Age: 6; Sex: M; Initial evidence: Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; Evidence: ; Do you have a known severe food allergy? Yes; Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: sharp; Do you feel pain somewhere? flank(L); Do you feel pain somewhere? iliac fossa(R); Do you feel pain somewhere? iliac fossa(L); Do you feel pain somewhere? hypochondrium(R); How intense is the pain? 4; Does the pain radiate to another location? nowhere; How precisely is the pain located? 1; How fast did the pain appear? 8; Are you experiencing shortness of breath or difficulty breathing in a significant way? Yes; Do you feel lightheaded and dizzy or do you feel like you are about to faint? Yes; Do you have any lesions, redness or problems on your skin that you believe are related to the condition you are consulting for? Yes; What color is the rash? pink; Do your lesions peel off? N; Is the rash swollen? 4; Where is the affected region located? back of the neck; Where is the affected region located? biceps(R); Where is the affected region located? biceps(L); Where is the affected region located? mouth; Where is the affected region located? thyroid cartilage; How intense is the pain caused by the rash? 1; Is the lesion (or are the lesions) larger than 1cm? Y; How severe is the itching? 8; Do you have swelling in one or more areas of your body? Yes; Where is the swelling located? nose; Have you noticed a high pitched sound when breathing in? Yes; Have you traveled out of the country in the last 4 weeks? N; Have you noticed a wheezing sound when you exhale? Yes; Are you more likely to develop common allergies than the general population? Yes.
Diagnostic result: Anaphylaxis.
Explanation: The patient's symptoms, including skin rash, difficulty breathing, throat swelling, and low blood pressure, are consistent with anaphylaxis. The presence of a known severe food allergy further supports this diagnosis. Immediate medical attention is required, and epinephrine is the primary treatment for anaphylaxis.
Give your score. output the format:
[Scores(range: [1 - 5]): 
,Consistency: Diagnos is result consistent with the Explanation. score:5  
,Explanation's valid. score:5
,adequacy of Explanation for Diagnosis result. score:5 
]
TOTAL_SCORE: 15
Example2: /end 

NEW PATIENT:
Patient condition: {information}
Diagnostic result: {disease}
Explanation: {explanation}
Give your score. output the format:
[
Scores(range: [1 - 5]): 
,Consistency: Diagnos is result consistent with the Explanation.  score:
,Explanation's valid.  score:
,adequacy of Explanation for Diagnosis result. score:
]
TOTAL_SCORE:
"""

SUMMARIZE ="""Summarize important symptoms that are helpful for doctor to diagnose based on the paragraph. Brief in 3-4 sentences.
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
                        input_variables=["information","previous_rank", "top1_knowledge","top1_diag"],
                        template = RETHINK_PROMPT,
                        )
score_agent_prompt = PromptTemplate(
                        input_variables=["information", "disease",  "explanation"],
                        template=SCORE,
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
