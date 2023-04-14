'''构建一些小工具，用于辅助其他模块的功能实现，如：读取数据集、计算准确率等、处理答案，将答案转换为标准格式等。'''

import json
import pandas as pd
import random

# 固定随机种子，保证每次运行结果一致
random.seed(42)
def read_data(path):
    # 读入csv文件，返回一个DataFrame
    data = pd.read_csv(path)
    return data
def shuffle_data(data,colomn='Diag_Set'):
    # 打乱dataframe中的colomn列，生成新的一列'choices'
    # 先去除两边的[]，最后再加上去
    data['choices'] = data[colomn].apply(lambda x: x[1:-1].split(','))
    data['choices'] = data['choices'].apply(lambda x: random.sample(x, len(x)))
    data['choices'] = data['choices'].apply(lambda x: '[' + ','.join(x) + ']')
    return data

def read_json(path):
    #把key转成小写，并且类似
    ddx_search = {}
    try:
        with open('path', 'r', encoding='utf-8') as f:
            ddx_search = json.load(f)
            #把key转成小写，并且类似
            ddx_search = {k.lower(): v for k, v in ddx_search.items()}
    except:
        print('json文件读取失败')
        
    return ddx_search


def list2str(rank_list):
    # 将列表转换为字符串['pulmonary embolism', 'localized edema', 'sle', 'chagas', 'anaphylaxis']---->'1. pulmonary embolism; 2. localized edema; 3. sle; 4. chagas; 5. anaphylaxis'
    rank_str = ''
    for i in range(len(rank_list)):
        rank_str += str(i+1) + '. ' + rank_list[i] + '; '
    return rank_str

def str2list(rank_str):
   # 把string变成list,如"['viral pharyngitis', 'urti', 'tuberculosis', 'bronchitis', 'acute laryngitis', 'possible nstemi / stemi', 'influenza', 'epiglottitis', 'unstable angina', 'stable angina']"--->['acute otitis media', 'urti', 'chagas']

    rank_str = rank_str.replace("'",'').replace('[','').replace(']','')
    rank_list = rank_str.split(',')
    rank_list = [x.strip() for x in rank_list]
    # 去除每个字符串元素里面的
    rank_list = [x.strip("'") for x in rank_list]
    return rank_list