import requests
from time import sleep
import time
import json


def output_log(ms):
    with open('outms.log', 'a',encoding='utf-8') as file:
        file.write(time.ctime() + ':   ' + ms + '\n')
def begin(id,token):
    url = "http://ncuos.com/api/freshman/learning/" + str(id)
    headers = {
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Authorization': "passport %s" % token,
        'Connection': "keep-alive",
        'Cookie': "_ga=GA1.2.1345916448.1517826665; _gid=GA1.2.1648392086.1517826665; _bl_uid=6bj7qdUwbq92hklgLgCygOhfz1LI",
        'Host': "ncuos.com",
        'Referer': "http://ncuos.com/index/app_rxjyks",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        'Cache-Control': "no-cache",
        'Postman-Token': "be4786b1-ff4a-b95c-d75c-4e90e65c4eee"
        }
    response = requests.request("GET", url, headers=headers)
    res = response.text
    output_log('开始%s' % id)
    print(res)
    return res


def put(id,token):
    url = "http://ncuos.com/api/freshman/learning/" + str(id)
    headers = {
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Authorization': "passport %s" % token,
        'Connection': "keep-alive",
        'Content-Length': "0",
        'Content-type': "application/x-www-form-urlencoded",
        'Cookie': "_ga=GA1.2.1345916448.1517826665; _gid=GA1.2.1648392086.1517826665; _bl_uid=6bj7qdUwbq92hklgLgCygOhfz1LI",
        'Host': "ncuos.com",
        'Origin': "http://ncuos.com",
        'Referer': "http://ncuos.com/index/app_rxjyks",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        'Cache-Control': "no-cache",
        'Postman-Token': "6a8dddd2-cf48-7794-39f1-53a31529cbbc"
    }

    response = requests.request("PUT", url, headers=headers)
    res = response.text
    output_log(res)
    print(res)
    return res



def login():

    url = "http://ncuos.com/api/user/token"

    payload = '{"username":"6103117040","password":"04631X"}'
    headers = {
        'Accept': "*/*",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Connection': "keep-alive",
        'Content-Type': "application/json",

        'Cookie': "_ga=GA1.2.1345916448.1517826665; _gid=GA1.2.1648392086.1517826665; _bl_uid=6bj7qdUwbq92hklgLgCygOhfz1LI",
        'Host': "ncuos.com",
        'Origin': "http://ncuos.com",
        'Referer': "http://ncuos.com/index/app_rxjyks",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    res = json.loads(response.text)
    return  res['token']



token = login()
print(token)
output_log('token获取成功：%s' % token)
for x in range(13,64):
    while True:
        try:
            b = begin(x,token)
            if b == 'Unauthorized Access':
                token = login()
                print(token)
                output_log('token获取成功：%s' % token)
                b = begin(x,token)
            b = json.loads(b)
            t = b['time']*60 +5
            for y in range(1,t):
                print('任务%s正在进行，剩余：%s'% (x, t-y))
                sleep(1)
            if put(x, token) == 'Unauthorized Access':
                continue
            else:
                break
        except:
            output_log('【异常错误】')
            continue

'''
Accept:*/*  
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Authorization:passport eyJleHAiOjE1MTc2Njk4MTksImFsZyI6IkhTMjU2IiwiaWF0IjoxNTE3NjY2ODE5fQ.eyJpZCI6IjQ0NzQwMDIyOTUifQ.RlwRn6kEdhy34Q3T0vLkRcOCL_kMaaNr5wi6EKpLWhY
Connection:keep-alive
Cookie:_ga=GA1.2.426766643.1516590995; _bl_uid=zzjUIcjkp53nFk4eId88kjtx7vzy; _gid=GA1.2.1899689008.1517659218
Host:ncuos.com
Referer:http://ncuos.com/index/app_rxjyks
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36
'''
'''
Cookie:_ga=GA1.2.1950772675.151
7714925; _gid=GA1.2.511832634.1517714925; _bl_uid=4CjdOd3t8bn8UmaCq3m9f8XwhLkz'''