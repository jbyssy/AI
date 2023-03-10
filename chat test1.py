import openai

import json



# 目前需要设置代理才可以访问 api

os.environ["HTTP\_PROXY"] = "自己的代理地址"

os.environ["HTTPS\_PROXY"] = "自己的代理地址"




def get\_api\_key():

    # 可以自己根据自己实际情况实现

    # 以我为例子，我是存在一个 openai\_key 文件里，json 格式

    '''

    {"api": "你的 api keys"}

    '''

    openai\_key\_file = '../envs/openai\_key'

    with open(openai\_key\_file, 'r', encoding='utf-8') as f:

        openai\_key = json.loads(f.read())

    return openai\_key['api']



openai.api\_key = get\_api\_key()



q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"

rsp = openai.ChatCompletion.create(

  model="gpt-3.5-turbo",

  messages=[

        {"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"},

        {"role": "user", "content": q}

    ]

)
