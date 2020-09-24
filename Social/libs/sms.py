import time
import json
import random
import requests
from hashlib import md5
from Social import config as conf

def text_send(phonenum,code):
    args = {
        'appid': conf.SD_APPID,     # APPID
        'to': phonenum,  # 手机号
        'project': conf.SD_PROJECT,  # 短信模板的 ID
        'vars': json.dumps({'code': code}),
        'timestamp': int(time.time()),
        'sign_type': conf.SD_SIGN_TYPE,
    }
    # 计算参数的签名
    sorted_args = sorted(args.items())  # 提取每一项
    args_str = '&'.join(
        [f'{key}={value}' for key, value in sorted_args])  # 对参数排序、组合
    sign_str = f'{conf.SD_APPID}{conf.SD_APPKEY}{args_str}{conf.SD_APPID}{conf.SD_APPKEY}'.encode(
        'utf8')  # 拼接成待签名字符串
    signature = md5(sign_str).hexdigest()  # 计算签名
    args['signature'] = signature

    response = requests.post(conf.SD_API, data=args)
    if response.status_code == 200:
        result = response.json()
        print('短信结果：', result)
        if result.get('status') == 'success':
            return True
    return False
