# -*- coding: utf-8 -*-

import requests
import sys
import io
import re
import xlwings as xw


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
#Amazon愿望单页面
url = 'https://www.amazon.cn/gp/registry/wishlist?ie=UTF8'
#url = 'https://www.amazon.cn/hz/wishlist/ls/2TQ7U13SV3MOD?ie=UTF8'

#浏览器登录后得到的cookie，可以通过Fiddle或者BurpSuite获取.(不要用我的)
cookie_str = 'session-id=462-0320008-3932010; session-id-time=2082729601l; ubid-acbcn=461-5754544-3434431; session-token="AkkRc2jTehRPcZw6Hk38C2s1tt6RBQ+UDgOpZ2lTBVs2JpgRjm3rbF/rqGGHAYdgnoV6NbLytYtaJ7g4T/Wl+0HAJ1LwduFTgE6oiP7i2sfJJEADSNxkKA+dXJ5D8/ZEvgvVo1Wv7LxEgOY45LnRyrl8RVNJgO3Dwq5An1h+7Oq52NCFXYCFyHjExWoKz6LGwV8k9zmTfdk4KPzg7JD/5A=="; x-acbcn="s77nGLsOtbcM5gruGxHj7ZP5RG8Zxq0t5hCbLSj3XRkufCznTOE5ZKeculR@MGsz"; at-main=Atza|IwEBIATyXPtTneQJgOYUwl9oV0Hlrdu8fEh9ZQ_e_g4w0BQDxzEySYVHroc4DsbupuefWyCZ0DNS_wmoN88tgH8q3-rka03-zr21Zh6FItHOHk8Od3Tiq29l-jLIVgzZ0hjmVyVmLl0D_ekinaG5n-y_PltY0i6W3zsp1F0hwiHLcAc_WP86JNqSgQqFhiOFFGwAUH90UKVYB2bv9e9jPcHAy4yh; sess-at-main="4rQqZL/b4Bh12A+QJFpa2NQWwIEe4gX08T6dOUBq9vw="; sst-main=Sst1|PQGkY0KpizPe-lIZ-FKD0D3uCWFFVPdTLo9D2gRD8ReiBmEIdpIjLKRnf390OKMyrI02iHhMSVvOSel7u8qtmuXrot37_KIt91GhFL3k_YAKsXvHR_V6GhAilrHUWmJwUfFi1-mcnKf52KHYfy35xSnr-G3U3uT61it-PNVGOS3zwC77vhHCoKgeJzJYn6oWCGPc1gJplzp_l2kYDuvlSxS16duLeW-0uAfvHDT-YhGx24InGQwGxSdUr_bfwn2Z7_-3zsS7X7gXXKiT-Xmxp0xUgOuT5nr1VCswil18bG3FyRk; lc-acbcn=zh_CN; i18n-prefs=CNY'
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

#提取书的链接
p_href = '<a class="a-link-normal" title=.*?href="(.*?)/\?coliid='
href = re.findall(p_href,response,re.S)

#提取书的价格
p_price = '<span class="a-offscreen">(.*?)</span>'
price = re.findall(p_price,response,re.S)

info = []
for i in range(len(href)):
    #构造完整的链接地址
    href[i] = "https://www.amazon.cn" + href[i]
    #将一本书的书名，地址，价格合并到一起
    info.append(title[i] + '+' + href[i] + ' ' + price[i])

app = xw.App(visible = True, add_book = False)
workbook = app.books.add()
worksheet = workbook.sheets.add('书单')

for i in range(len(href)):
    worksheet.range('A' + str(i + 1)).value = title[i]
    worksheet.range('B' + str(i + 1)).value = href[i]
    worksheet.range('C' + str(i + 1)).value = price[i]

workbook.save('amzaon.xlsx')
workbook.close()
app.quit()

#print(info)
#print(title)
#print(href)
#print(price)

