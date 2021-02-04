import requests
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

url = 'https://www.freebuf.com/column/1620'

response = requests.get(url=url, headers=headers).text

with open('a.html', 'w', encoding='utf-8') as f_obj:
    f_obj.write(response)