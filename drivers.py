import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Python(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome('D:\selenium softwares\chromedriver_win32\chromedriver.exe')

    def test(self):
        driver=self.driver
        driver.get('http://www.python.org')
        self.assertIn('Python',driver.title)
        elem=driver.find_element_by_name('q')
        elem.clear()
        elem.send_keys('Pycon')
        elem.send_keys(Keys.RETURN)
        assert "No Results Found." not in driver.page_source
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
