import unittest
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
base_url = "https://www.baidu.com"

class BaiduPage:
    def __init__(self, driver):
        self.driver = driver

    def baidu_search_input(self,send_keys):
        self.driver.find_element_by_id("kw").send_keys(send_keys)

    def baidu_search_submit(self):
        driver.find_element_by_id("su").click()
        

class TestBaiduPage(unittest.TestCase):
    def setUp(self) :
        driver.get(base_url)
        self.bd = BaiduPage(driver)

    def test_baidu_search_selenium(self):
        self.bd.baidu_search_input("selenium")
        self.bd.baidu_search_submit()
        sleep(2)
        self.assertEqual(driver.title, "selenium_百度搜索")

    def tearDown(self):
        driver.quit()

unittest.main()
