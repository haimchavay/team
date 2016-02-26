'''
Created on Feb 23, 2016

@author: haim
'''
from AbstractPageObject import AbstractPageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewTaskListModule(AbstractPageObject):
    def __init__(self, driver_):
        AbstractPageObject.__init__(self, driver_)
        
    def assertInPage(self):
        try:
            WebDriverWait(self._m_driver, 10).until(
                EC.presence_of_element_located((By.ID, "btnCreateTaskList")))
        except:
            assert False, "don't found the NewTaskLoginModule"
            
    def setListName(self, name_):
        self._m_driver.find_element_by_id("newTaskListName").clear()
        self._m_driver.find_element_by_id("newTaskListName").send_keys(name_)
        
    def clickOnAddThisTaskListBtn(self):
        from TasksPage import TasksPage
        self._m_driver.find_element_by_id("btnCreateTaskList").click()
        return TasksPage(self._m_driver)