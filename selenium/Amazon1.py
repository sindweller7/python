from selenium import webdriver
from selenium.webdriver import ActionChains

url = "https://www.amazon.cn"

# 打开浏览器
browser = webdriver.Chrome()

# 需要先进入登录的页面，再添加Cookie，否则不能用
browser.get(url)

# 手动添加cookie,不同的浏览器好像值不一样，所以直接在chrome中登录，看cookie的值，就可以在chrome中登录
browser.add_cookie({'name': 'session-id', 'value': '461-8282735-0442849'})
browser.add_cookie({'name': 'session-id-time', 'value': '2082787201l'})
browser.add_cookie({'name': 'ubid-acbcn', 'value': '459-2109021-8458964'})
browser.add_cookie({'name': 'session-token', 'value': 'rqNJsHExqr4kM4viQsZHqekP+/JJ9/gZlIa+w8WY438Bt/lAHov5jVUoGQBeg/UkZZw7GIAmX/IMOkVqwMyZ7RWpBgSguJrRyUZT09Kn6nJD8w1RwdWtkmp/PSvvcq5JXGK7D4sP7lrvweL/nkDBx4alH43yLTYL+glmf2gth0WQrLVJPJgYczZx0carWOjl7xOxdOa+P9BPa1WqTDz+B+VBdeyD10BSMPPdWSxO9gDjz3ooIDAgj9OYruthzIvebcbtG57rfiY/XhjvUP1HGA=='})
browser.add_cookie({'name': 'x-acbcn', 'value': 'BCr8qbQAwvPBL0w83KWvBCrTvHL7LATfctGVIwbA5uckxGUJ4aOGRiKfu@?PpX7E'})
browser.add_cookie({'name': 'at-main', 'value': 'Atza|IwEBIEZOXEEU3Q5lLQaOG9yv7b_LNrataOqQy4MioxTXiWerI5iWn1iyLFGXdlxtD-f3esHPniSDHf_aHYfuDqpeDzv_--pZjFdp4MELkWKym4lmvPEWiohzEXBBf7rmHBQOuEJLcCJzBkfOvU3lCy8Gi_l3B4nvYTJ5Kty7VW-flPcIKYXUon2wqeWOpDHhmY7x0vqVFb_WnnSQX8QZxcE6zqdY'})
browser.add_cookie({'name': 'sess-at-main', 'value': 'FDxbCXalFIj9j/SsgN3ei1cBPfvUD6dlGrqqxBjy2GM='})
browser.add_cookie({'name': 'sst-main', 'value': 'Sst1|PQHMESwc8oV3AmJ-Qvcj0OyqCY3G-yUse5dPgdfA6v0jTgIpSuKsZUvy9Vn7SjaE7mmJ8T5HJg5w43kR3J3ptrQtS75CW2EEUxQol-G_XPttgQghuymM4OKhItBBAXPuCeyiMboPEIvvAPGBNzpkDe8vuDWzPJXRNX1mJZ-cY2f4llUgcKBqEwahdKAYycryX1r4SduTcwlbdc38hux0v2ETXsSGOEwHHpJMZEQbQIfHtxchZNqUPw8FIyEurSQkXq3Ma1Lol8pt0rW7ks_p6yHtQ2xgIYZcRmmHuy-9I14xz5g'})
browser.add_cookie({'name': 'lc-acbcn', 'value': 'zh_CN'})
browser.add_cookie({'name': 'i18n-prefs', 'value': 'CNY'})
browser.add_cookie({'name': 'csm-hit', 'value': 'tb:JK62XS34RKAW9Z5P7HVE+client_socket-NTE56JKCB9AASG7T25C0|1609646784560&t:1609646784560&adb:adblk_no'})

browser.refresh()  # 刷新页面

#打开我的心愿单
browser.get("https://www.amazon.cn/gp/registry/wishlist?ie=UTF8&ref_=nav_gno_listpop_wi&requiresSignIn=1")
