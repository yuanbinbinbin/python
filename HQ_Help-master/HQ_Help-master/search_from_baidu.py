# coding: utf-8

import time
import json
import requests
import webbrowser
import sys
reload(sys)
sys.setdefaultencoding('utf8')
questions = []

def open_webbrowser(question):
    webbrowser.open('https://baidu.com/s?wd=' + question.decode("utf-8"))


def open_webbrowser_count(question,choices):
    print('-- 方法2： 题目+选项搜索结果计数法 --')
    print('Question: ' + question)
    if '不是' in question:
        print('**请注意此题为否定题,选计数最少的**')

    counts = []
    for i in range(len(choices)):
        # 请求
        req = requests.get(url='http://www.baidu.com/s', params={'wd': question + choices[i]})
        content = req.text
        index = content.find('百度为您找到相关结果约') + 11
        content = content[index:]
        index = content.find('个')
        count = content[:index].replace(',', '')
        counts.append(count)
        print(choices[i] + " : " + count)


def count_base(question,choices):
    print('-- 方法3： 题目搜索结果包含选项词频计数法 --')
    # 请求
    req = requests.get(url='http://www.baidu.com/s', params={'wd':question})
    content = req.text
    #print(content)
    counts = []
    print('Question: '+question)
    if '不是' in question:
        print('**请注意此题为否定题,选计数最少的**')
    for i in range(len(choices)):
        counts.append(content.count(choices[i]))
        print(choices[i] + " : " + str(counts[i]))


def get_answer():
  #  resp = requests.get('http://htpmsg.jiecaojingxuan.com/msg/current',timeout=4).text
    resp = requests.get('http://htpmsg.jiecaojingxuan.com/msg/current',timeout=4).text
    resp_dict = json.loads(resp)
    if resp_dict['msg'] == 'no data':
        return 'Waiting for question...'
    else:
        resp_dict = eval(str(resp))
        question = resp_dict['data']['event']['desc']
        question = question[question.find('.') + 1:question.find('?')]
        if question not in questions:
            questions.append(question)
            print('问题:'+question)
            choices = eval(resp_dict['data']['event']['options'])
            open_webbrowser(question)
          #  open_webbrowser_count(question, choices)
           # count_base(question, choices)
            time.sleep(5)
        else:
            return 'Waiting for new question...'


def main():
    while True:
        try:
            print(time.strftime('%H:%M:%S',time.localtime(time.time())))
            print(get_answer())
        except Exception, e:
            print("error")
        time.sleep(1)


if __name__ == '__main__':
    # question = '一下诗句与"杨家有女初长成,养在深闺人未识"描写的不是同一人物的是?'
    # choices = ['一枝红艳露凝香','名花倾国两相欢','秀色掩今古']
    question = '第一个登陆NBA的中国篮球运动员是?'
    choices = ['王治郅','姚明','易建联']
    open_webbrowser_count(question, choices)
