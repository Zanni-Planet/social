import time
import json
from hashlib import md5
import random

import requests

def text_send(phonenum):
    appid = '54750'
    appkey = 'a71e88a7ab4c03625a04a77dcd094aa4'
    # 生成验证码
    code = ''
    for i in range(6):
        code += str(random.randint(0,9))
    
    args = {
        'appid': appid,     # APPID
        'to': phonenum,  # 手机号
        'project': 'lEwKz2',  # 短信模板的 ID
        'vars': json.dumps({'code': code}),
        'timestamp': int(time.time()),
        'sign_type': 'md5',
    }

    api = 'https://api.mysubmail.com/message/xsend.json'

    # 计算参数的签名
    sorted_args = sorted(args.items())  # 提取每一项
    args_str = '&'.join(
        [f'{key}={value}' for key, value in sorted_args])  # 对参数排序、组合
    sign_str = f'{appid}{appkey}{args_str}{appid}{appkey}'.encode(
        'utf8')  # 拼接成待签名字符串
    signature = md5(sign_str).hexdigest()  # 计算签名
    args['signature'] = signature

    response = requests.post(api, data=args)
    print('状态码：', response.status_code)

    result = response.json()
    print('短信结果：', result)
    return code