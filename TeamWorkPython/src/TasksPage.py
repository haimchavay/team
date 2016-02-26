'''
Created on Feb 23, 2016

@author: haim
'''
from AbstractMenuItem import AbstractMenuItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TasksPage(AbstractMenuItem):
    def __init__(self, driver_):
        AbstractMenuItem.__init__(self, driver_)
        
    def assertInPage(self):
        try:
            WebDriverWait(self._m_driver, 10).until(
                EC.presence_of_element_located((By.ID, "tab_overview")))
        except:
            assert False, "don't found the TasksPage"
            
    def clickOnAddTaskListBtn(self):
        from NewTaskListModule import NewTaskListModule
        self._m_driver.find_element_by_id("liBFOATL").click()
        return NewTaskListModule(self._m_driver)
    
    def addTheFirstTaskBtnByNameList(self, nameList_):
        from AddTaskModule import AddTaskModule
        path = "//a[text()='"+nameList_+"']/../../div/div/div/div/div/button"
        try:
            WebDriverWait(self._m_driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
        except:
            assert False, "don't found the '"+nameList_+"' tasks"            
        self._m_driver.find_element_by_xpath(path).click()
        return AddTaskModule(self._m_driver)
    
    def verifyTaskList(self, nameOfTaskList_):
        self._m_driver.find_element_by_xpath("//a[text()='"+nameOfTaskList_+"']")
        
    def verifyTasksListInTaskList(self, nameOfTaskList_, listOfTasks_):
        self.clickOnNameOfTaskList(nameOfTaskList_)
        for txt in listOfTasks_:
            self._m_driver.find_element_by_xpath("//span[text()='"+txt+"']")
        self.clickOnTasksItem()
        
    def clickOnNameOfTaskList(self, nameOfTaskList_):
        self._m_driver.find_element_by_xpath("//a[text()='"+nameOfTaskList_+"']").click()
        
    def clickOnOptions(self):
        self._m_driver.find_element_by_xpath("//button/i/..").click()
        time.sleep(0.5)
        
    def clickOnDelete(self):
        idToDelete = ""
        for tmp in self._m_driver.current_url:
            if tmp.isdigit():
                idToDelete += tmp
                            
        self._m_driver.find_element_by_xpath(
            "//a[@href='javascript:tw.DeleteTaskList( "+idToDelete+" , true )']").click() 
        