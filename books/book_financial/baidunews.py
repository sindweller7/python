# _*_ coding=utf-8 _*_
import requests
import re
import time
import pymysql


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}

def baidu(company):
    url = "https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word=" + company
    response = requests.get(url,headers=headers)
    content = response.text

    p_title = '<h3 class="news-title_1YtI1">.*?<!--s-text-->(.*?)<!--/s-text-->'
    title = re.findall(p_title, content, re.S)

    p_href = '<h3 class="news-title_1YtI1"><a href="(.*?)" target="_blank"'
    href = re.findall(p_href, content, re.S)

    p_date = '<span class="c-color-gray2 c-font-normal">(.*?)</span>'
    date = re.findall(p_date, content, re.S)

    p_source = '<span class="c-color-gray c-font-normal c-gap-right">(.*?)</span>'
    source = re.findall(p_source, content, re.S)

    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])

    #将提取出来的数据写入文本文件
    for i in range(len(title)):
        news = str(i + 1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')' + '\n' + href[i] + '\n'
        with open('a.txt', 'a', encoding='utf-8') as f_obj:
            f_obj.write(news)

    # 将提取出来的数据写入数据库
    db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='pachong', charset='utf8')
    cur = db.cursor()
    for i in range(len(title)):
        sql = 'INSERT INTO test(company, title, href, date, source) VALUES(%s, %s, %s, %s, %s)'
        cur.execute(sql,(company, title[i], href[i], date[i], source[i]))
        db.commit()
    cur.close()
    db.close()

companys = ['华能信托',' 阿里巴巴',' 百度集团']

for company in companys:
    try:
        baidu(company)
        with open('a.txt', 'a', encoding='utf-8') as f_obj:
            f_obj.write('------------ ' + company + ' 搜索结束！！------------\n\n')
        print("获取 " + company + " 搜索结果成功")
    except:
        print("获取 " + company + " 搜索结果失败")