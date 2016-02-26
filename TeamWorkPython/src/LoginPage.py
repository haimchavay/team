'''
Created on Feb 22, 2016

@author: haim
'''

from AbstractPageObject import AbstractPageObject
from OverviewPage import OverviewPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(AbstractPageObject):

    def __init__(self, driver_):
        AbstractPageObject.__init__(self, driver_)
            
    def assertInPage(self):
        try:
            WebDriverWait(self._m_driver, 10).until(
                EC.presence_of_element_located((By.ID, "ordLoginSubmitBtn")))
        except:
            assert False, "don't found the LoginPage"
        
    def setUserName(self, userName_):
        self._m_driver.find_element_by_id("userLogin").clear()
        self._m_driver.find_element_by_id("userLogin").send_keys(userName_)
        
    def setPassword(self, password_):
        self._m_driver.find_element_by_id("password").clear()
        self._m_driver.find_element_by_id("password").send_keys(password_)
        
    def clickOnLoginBtn(self):
        self._m_driver.find_element_by_id("ordLoginSubmitBtn").click()
        return OverviewPage(self._m_driver)
        
        