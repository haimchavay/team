'''
Created on Feb 23, 2016

@author: haim
'''
#from AbstractPageObject import AbstractPageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from TasksPage import TasksPage

class AddTaskModule(TasksPage):
    __path = "//input[@class='tt-query' and @placeholder='What needs to be done?']"
    
    def __init__(self, driver_):
        TasksPage.__init__(self, driver_)
        
    def assertInPage(self):      
        try:
            WebDriverWait(self._m_driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.__path)))
        except:
            assert False, "don't found the AddTaskModule"
            
    def setWhatNeedsToBeDone(self, needToBeDone_):   
        self._m_driver.find_element_by_xpath(self.__path).send_keys(needToBeDone_)
        
    def setWhoShouldDoThis(self):
        Select(self._m_driver.find_element_by_xpath(
            "//select[@name='taskAssignedToUserId']")).select_by_visible_text("fake08 fake08 (me)")
            
    def clickOnSaveMyChanges(self):
        self._m_driver.find_element_by_xpath("//input[@value='Save my changes']").click()
        time.sleep(0.3)
        