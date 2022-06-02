import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.locator import locator1
from locators.locator import locator2
from locators.locator import locator3
from locators.locator import baseurl

class Pythonorgs:
    def __init__(self, driver):
        self.l1=locator1()
        self.l2=locator2()
        self.l3=locator3()
        self.u= baseurl()
        self.driver = driver
    def starting(self):
        self.driver.maximize_window()
        self.driver.get(self.u.baseURL)
    def comments(self):
        self.driver.find_element(By.XPATH,self.l1.news_xpath).click()
        self.driver.find_element(By.XPATH,self.l1.pycon_xpath).click()
        self.driver.execute_script('window.scrollBy(0,800)','')
        time.sleep(5)
        self.driver.find_element(By.ID,self.l1.commentwritebox_id).send_keys('Hi iam automation tester')
        self.driver.find_element(By.ID,self.l1.recapcha_id).click()
        self.driver.find_element(By.ID,self.l1.publish_id).click()
        time.sleep(3)
    def joblink(self):
        self.driver.find_element(By.XPATH,self.l2.jobsearchlink_xpath).click()
        self.driver.find_element(By.XPATH,self.l2.job_xpath).click()
        self.driver.find_element(By.CLASS_NAME,self.l2.jobcompany_class).click()
        time.sleep(3)
    def searchbutton(self):
        self.driver.find_element(By.NAME,self.l3.searchbox_name).click().send_keys('download python')

        self.driver.find_element(By.ID,self.l3.submit_id).click()
        time.sleep(5)






