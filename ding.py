# 1、导包
import json
import requests


# 2、钉钉机器人的调用
def dd_robot(msg):
    HEADERS = {"Content-Type": "application/json;charset=utf-8"}
    key = "8451e700bf0dbe296de271fe5bdd5de5be9207326565e51dc0e2d418ea4ade6d"
    url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % key
    data_info = {
        "msgtype": "text",
        "text": {
            "content": "设计" + msg
        },
        "isAtAll": True
    }
    # 转化成自己需要的数据格式:转换成python格式的数据
    # value = bytes(json.dumps(data_info,ensure_ascii=False,indent=4),"utf-8")
    value = json.dumps(data_info)
    response = requests.post(url, data=value, headers=HEADERS)


# 3、程序主入口
if __name__ == '__main__':
    msg = '测试'
    dd_robot(msg)
