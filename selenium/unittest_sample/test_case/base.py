from time import sleep

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def by_id(self,id_):
        return self.driver.find_element_by_id(id_)

    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def by_css(self, css_name):
        return self.driver.find_element_by_css_selector(css_name)

    def get_title(self):
        return self.driver.title

    def get_text(self, xpath):
        return self.by_xpath(xpath).text

    def js(self, scrpit):
        return self.driver.excute_script(scrpit)
