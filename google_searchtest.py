from selenium import webdriver
import unittest
class Amazonsearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:\Users\\Test\\Documents\\devtest1\\src\\chromedriver.exe")
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_serach_drivesearch(self):
        self.driver.get("https://amazon.in")
        self.driver.find_element_by_name("field-keywords").send_keys("ssd external drives offer")
        self.driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
        self.driver.back()

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main()
