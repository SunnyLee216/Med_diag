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



RETHINK_PROMPT ="""
Here are some examples:
{examples}
(END OF EXAMPLES)

Here is the information of a new patient:
{information}
Imagine you are an senior doctor. Based on the previous dialogue, what is the diagnosis? Based on the above conversation, rank the following diseases according to their likelihood of diagnosis. For example, patients are more likely to be diagnosed with disease A than disease B, and disease A should be ranked first in disease B, and so on.
The previous ranking of diseases is as follows:
{previous_rank}
This is the knowledge of the top 1 diseases:
{top1_knowledge}
Assuming that the top 1 disease is correct
Regardless of whether external information exists, you should reflect on your previous choices. You need to reconsider whether the diagnosis of this disease is valid.You can change your RANK at any point.\nYou should RANK again and your EXPLANATION for the RANK you output.
YES/NO:
Rationale:
"""



SCORE ="""你要给以下的医学推理过程进行打分，分数越高，越有可能是正确的答案。
评分的细则是：
- 
-
-
-
Here are some examples:
{examples}
(END OF EXAMPLES)
Here is a new patient's information:
{information}
{previous_rank}
{top1_knowledge}
{Rationale}
"""

SUMMARIZE ="""Summarize important symptoms that are helpful for doctor to diagnose based on the paragraph. Brief in 3-4 sentences.Paragraph:{paragraph}.
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
                        input_variables=["examples", "information","previous_rank", "top1_knowledge"],
                        template = RETHINK_PROMPT,
                        )
score_agent_prompt = PromptTemplate(
                        input_variables=["examples", "information", "previous_rank", "top1_knowledge", "Rationale"],
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
