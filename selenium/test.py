














"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

subject = "python email test"

msg = MIMEText("<html><h1>你好</h1>/html>", "html", "utf-8")
msg["Subject"] = Header(subject,"utf-8")

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com:465")
smtp.login("77577915@qq.com","abievhhzemjlcabc")
smtp.sendmail("77577915@qq.com", "hxjun7@126.com", msg.as_string())
smtp.quit()    

import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt, data, file_data, unpack


class BaiduPage:
    def __init__(self, driver):
        self.driver = driver

    def search_input(self, search_keys):
        self.driver.find_element_by_css_selector(".s_ipt").send_keys(search_keys)

    def search_click(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
    
@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.baseUrl = "https://www.baidu.com"

    def baidu_search(self, search_keys):
        self.driver.get(self.baseUrl)
        BaiduPage.search_input(self, search_keys)
        BaiduPage.search_click(self)
        sleep(2)

    @file_data("ddt_data_file.json")
    def test_search3(self, search_keys):
        print("第四组测试用例: ")
        self.baidu_search(search_keys)
        self.assertEqual(self.driver.title, search_keys + "_百度搜索")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        

unittest.main(verbosity=2) 

import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt, data, file_data, unpack


class BaiduPage:
    def __init__(self, driver):
        self.driver = driver

    def search_input(self, search_keys):
        self.driver.find_element_by_css_selector(".s_ipt").send_keys(search_keys)

    def search_click(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
    
@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.baseUrl = "https://www.baidu.com"

    def baidu_search(self, search_keys):
        self.driver.get(self.baseUrl)
        BaiduPage.search_input(self, search_keys)
        BaiduPage.search_click(self)
        sleep(2)
      
    @data(
        ["case1", "selenium"],
        ["case2", "ddt"],
        ["case3", "python"],
        )
    @unpack
    def test_search1(self, case, search_keys):
        print("第组测试用例: ", case)
        self.baidu_search(search_keys)
        self.assertEqual(self.driver.title, search_keys + "_百度搜索")

    @data(
        ("case1", "selenium"),
        ("case2", "ddt"),
        ("case3", "python"),
        )
    @unpack
    def test_search2(self, case, search_keys):
        print("第二组测试用例: ", case)
        self.baidu_search(search_keys)
        self.assertEqual(self.driver.title, search_keys + "_百度搜索")

    @data(
        {"search_keys": "selenium"},
        {"search_keys":"ddt"},
        {"search_keys": "python"},
        )
    @unpack
    def test_search3(self, search_keys):
        print("第三组测试用例: ")
        self.baidu_search(search_keys)
        self.assertEqual(self.driver.title, search_keys + "_百度搜索")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        

unittest.main(verbosity=2)        
    






from time import sleep
from selenium import webdriver
import unittest
from parameterized import parameterized


class BaiduPage:
    def __init__(self, driver):
        self.driver = driver

    def search_input(self, search_keys):
        self.driver.find_element_by_css_selector(".s_ipt").send_keys(search_keys)

    def search_click(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
    

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.baseUrl = "https://www.baidu.com"

    def baidu_search(self, search_keys):
        self.driver.get(self.baseUrl)
        BaiduPage.search_input(self, search_keys)
        BaiduPage.search_click(self)
        sleep(2)
        
    @parameterized.expand([
        ("case1", "selenium"),
        ("case2", "unittest"),
        ("case3", "parameterized"),
        ])
    def test_search(self, name, search_keys):
        self.baidu_search(search_keys)
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, search_keys + "_百度搜索")

    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        

unittest.main(verbosity=2)        
    




from time import sleep
from selenium import webdriver
import unittest


class BaiduPage:
    def __init__(self, driver):
        self.driver = driver

    def search_input(self, search_keys):
        self.driver.find_element_by_css_selector(".s_ipt").send_keys(search_keys)

    def search_click(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
    

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.baseUrl = "https://www.baidu.com"

    def baidu_search(self,search_keys):
        self.driver.get(self.baseUrl)
        BaiduPage.search_input(self, search_keys)
        BaiduPage.search_click(self)
        

    def test_baidu_selenium(self):
        self.baidu_search("selenium")
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, "selenium_百度搜索")

    def test_baidu_unittest(self):
        self.baidu_search("unittest")
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, "unittest_百度搜索")
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        

unittest.main()     

class Spam:
    number = 0
    def __init__(self):
        self.count()

    def count(cls):
        cls.number += 1

    count = classmethod(count)

class Sub(Spam):
    number = 0

    def __init__(self):
        Spam.__init__(self)

class Other(Spam):
    number = 0




from time import ctime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
#driver.maximize_window()

element = WebDriverWait(driver, 5, 0.5).until(
    EC.visibility_of_element_located((By.ID , "kw1"))
)
print(element)
element.send_keys('selenium')




driver.implicitly_wait(5)
try:
    print(time.ctime())
    driver.find_element_by_id("kw22").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(time.ctime())

try:
    print("----------another------------")
    print(time.ctime())
    driver.find_element_by_id("kw22").send_keys("selenium")
except NoSuchElementException as e:
    print(e)
finally:
    print(time.ctime())


driver.find_element_by_name('wd').send_keys("abc")
driver.find_element_by_id('su').click()

time.sleep(2)
print(driver.title)
print(driver.current_url)

text = driver.find_element_by_class_name("nums_text").text
print(text)


driver.switch_to.frame("login_frame")
#driver.find_element_by_id("switcher_plogin").click()
driver.find_element_by_id("img_out_77577915").click()
driver.switch_to.default_content()

driver.find_element_by_xpath('//*[@id="composebtn"]').click()

driver.switch_to.frame("mainFrame")
#driver.find_element_by_name("UploadFile").send_keys("D:\python\Selenium\test.side")
driver.find_element_by_xpath('//*[@name="UploadFile"]').send_keys("D:\python\Selenium\test.side")

#driver.find_element_by_link_text("Different ID").click()



driver.switch_to.frame("login_frame")
driver.find_element_by_id("switcher_plogin").click()
driver.find_element_by_id("u").send_keys("username")

jt = driver.find_element_by_link_text("简体中文")
ActionChains(driver).context_click(jt).perform()

first_url = "https://www.baidu.com"
driver.get(first_url)

xw = driver.find_element_by_link_text("新闻")
ActionChains(driver).double_click(xw).perform()

above = driver.find_element_by_id("client_socket-usersetting-top")
ActionChains(driver).move_to_element(above).perform()

driver.find_element_by_link_text("搜索设置").click()
time.sleep(1)

driver.find_element_by_id("nr_2").click()

size = driver.find_element_by_id('kw').size
print(size)

text = driver.find_element_by_id('client_socket-bottom-layer-right').text
print(text)

attribute = driver.find_element_by_id('kw').get_attribute('type')
print(attribute)

result = driver.find_element_by_id('kw').is_displayed()
print(result)

second_url = "https://news.baidu.com"
driver.get(second_url)

driver.back()
time.sleep(2)
driver.forward()

time.sleep(2)
driver.refresh()
"""
