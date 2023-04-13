import re 
import string
from typing import Tuple

import gym
from langchain import Wikipedia
from langchain.agents.react.base import DocstoreExplorer

class QAEnv(gym.Env):
    def __init__(self,
                 question: str,
                 key: str,
                 max_steps: int = 6,
                 explorer: DocstoreExplorer = DocstoreExplorer(Wikipedia())):
        
        self.question = question
        self.key = key
        self.max_steps = max_steps
        self.explorer = explorer

        self.reset()
    def reset(self):
          self.curr_step = 0
          self.terminated = False
          self.answer = ''
    def step(self, action):
        ## TODO: implement this function
        '''根据action，更新环境状态，返回reward等信息
        '''
        action_type, argument = parse_action(action)
        pass
    def is_correct(self) -> bool:
        return EM(self.answer, self.key)
    def is_terminated(self) -> bool:
        return self.terminated
    def is_truncated(self) -> bool:
        return self.curr_step >= self.max_steps

def parse_action(string):
    pattern = r'^(\w+)\[(.+)\]$'
    match = re.match(pattern, string)
    
    if match:
        action_type = match.group(1)
        argument = match.group(2)
        return action_type, argument
    
    else:
        return None, None
    
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