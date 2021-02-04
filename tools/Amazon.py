# -*- coding: utf-8 -*-

import requests
import sys
import io
import re


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
#Amazon愿望单页面
url = 'https://www.amazon.cn/gp/registry/wishlist?ie=UTF8'

#浏览器登录后得到的cookie，可以通过Fiddle获取.(不要用我的)
cookie_str = 'session-id=461-3297493-78711471147; ubid-acbcn=458-5048738-7391249; lc-acbcn=zh_CN; session-token="JB6tC6EJB6tC6E/J/ZSqjo4CaaR5fOQA85e0SjYo01isXJWUG+VtdoNOpyRGos2j8yJGdBhMMe06USduY0X+Vg6PjTF3TtZJYENJIqnQUed9w9FUp79N7036MetG3Lb3JF5FK3wTqupuzxQOGJM/pEP73+rfCGySpnnInsVoyBn0LYyhzfV/jsmTMn/tvg7M6WJea+HNiJePYgdS9PApemBLl+VOmgRXdU4TCd9YAqe2PKUilE="; x-acbcn="7LPgsSqrifoccEbY6I8kQyzjZ5kiMy3?xMJTJI4?sPYvZODUzXDKcfWlX1sX84z7"; at-main=Atza|IwEBICmMcbKkGdCkaDclgM2mU1mA87Y9Z_YA_YCdKVp_bG41dZWky9DfG5bEs-V2LmDIcOdryEZ8B1eJRkyHnw5sVAHWsbjYu8Q0YxCTcyX-ZsHX96GMa-2O_NjEvRYjJrp6mcWs5Fi3kY9jssQxOz7HfY89-W4CPhrEMj4SIgWhwHQY1YlVAWQtwN3pY-QufuT4LieANTKFLdJKkMBgc6s7pAoU; sess-at-main="SDja+Jz/9ufxl/v53V8f25aAZ6ROJpD8gE32fq5EPcI="; sst-main=Sst1|PQHD7FhGACBMBQrTpyLkXyG4CeYwUahrg_RULPB6n3Fcpi7SkqNRqkQrDY7yV6j1m5p0SP8SFRfIRwwigcXnxyvGhUQozjYo4rH4IKiDS_MW8w45UNigyzASQtBv9RcbziMF8LgdilXHHDzkwznU24IKRPqZoB3ymi6rI-vWfAYbA1C4OVxRiCwgcT6to3R_niN10DC18Vs6qMXwkaxLiWloJBEaDV7al0thVEOA8fPZVe0qJpQeaLh7JW2j9C9XeizurzI5Nl-sp-9Kk3K-2bUf-CCUSWX5y5cd_XdFnNpaKk8; csm-hit=tb:s-E4NB30CH2AK8DN40463Y|1609750987095&t:1609750987525&adb:adblk_no; session-id-time=2082787201l; i18n-prefs=CNY'
#从原始cookie中提取出以字典形式存放的cookie信息
cookies = {}
for cookie in cookie_str.split(';'):
    #cookie的值中可能含有等号，所以这里需要从第一个等号处split
    key, value = cookie.split('=', 1)
    cookies[key] = value

response = requests.get(url, headers=headers, cookies=cookies).text

#提取愿望单中的书名
p_title = '<a class="a-link-normal" title="(.*?)" href="/dp/'
title = re.findall(p_title,response,re.S)

#提取书名的链接
p_href = '<a class="a-link-normal" title=.*?href="(.*?)/\?coliid='
href = re.findall(p_href,response,re.S)

for i in range(len(href)):
    href[i] = "https://www.amazon.cn" + href[i]

print(title)
print(href)

