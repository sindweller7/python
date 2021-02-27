# _*_ coding=utf-8 _*_
import requests
import re
import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}

def sina(company):
    url = "https://search.sina.com.cn/?q=" + company + '&c=news'
    response = requests.get(url, headers=headers, timeout=10)
    content = response.text
    # with open('a.html', 'a', encoding='utf-8') as f_obj:
    #     f_obj.write(content)

    p_title = '<h2>\s*?<a href.*?target="_blank">(.*?)</a>'
    title = re.findall(p_title, content, re.S)

    p_href = '<h2>\s*?<a href="(.*?)" target="_blank">'
    href = re.findall(p_href, content, re.S)

    p_source = '<span class="fgray_time">(.*?)</span>'
    source = re.findall(p_source, content, re.S)

    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])
        news = str(i + 1) + '.' + title[i] + '(' + source[i] + ')' + '\n' + href[i] + '\n'
        with open('a.txt', 'a', encoding='utf-8') as f_obj:
            f_obj.write(news)

companys = ['华能信托',' 阿里巴巴',' 百度集团']
for company in companys:
    sina(company)

