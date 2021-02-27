from time import sleep
from selenium import webdriver
import unittest
from base import BasePage


class BaiduPage(BasePage):
    url = "https://www.baidu.com"

    def search_input(self, search_keys):
        self.by_css(".s_ipt").send_keys(search_keys)

    def search_button(self):
        self.by_xpath("//input[@type='submit']").click()


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()      

    def test_baidu_selenium(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("selenium")
        page.search_button()
        sleep(2)
        title = page.get_title()
        self.assertEqual(title, "selenium_百度搜索")
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        

unittest.main()        
    
