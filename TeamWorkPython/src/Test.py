'''
Created on Feb 22, 2016

@author: haim
'''
from LoginPage import LoginPage
from selenium import webdriver
import unittest

class Test(unittest.TestCase):      
    def setUp(self):
        # setUp variables to the test
        self.taskListName = "list1"
        self.task1 = "buy lamborghini"
        self.task2 = "buy coat"       
        self.driver = webdriver.Firefox()
        self.driver.get("https://topq.teamwork.com/")  
        self.driver.implicitly_wait(3)                   

    def runTest(self):  
        # login    
        loginPage = LoginPage(self.driver)
        loginPage.setUserName("fake08@fake.com")
        loginPage.setPassword("fake")
        overviewPage = loginPage.clickOnLoginBtn()
    
        # create taskList
        tasksPage = overviewPage.clickOnTasksItem()
        newTaskListModule = tasksPage.clickOnAddTaskListBtn()
        newTaskListModule.setListName(self.taskListName) 
        tasksPage = newTaskListModule.clickOnAddThisTaskListBtn()
        addTaskModule = tasksPage.addTheFirstTaskBtnByNameList(self.taskListName)
    
        # add tasks to the taskList that we create
        addTaskModule.setWhatNeedsToBeDone(self.task1)
        addTaskModule.setWhoShouldDoThis()
        addTaskModule.clickOnSaveMyChanges()  
        addTaskModule.setWhatNeedsToBeDone(self.task2)
        addTaskModule.setWhoShouldDoThis()
        addTaskModule.clickOnSaveMyChanges()
    
        # check that evriting fine
        milestones = addTaskModule.clickOnMilestones()
        tasksPage = milestones.clickOnTasksItem()
        tasksPage.verifyTaskList(self.taskListName)
        tasksPage.verifyTasksListInTaskList(self.taskListName, [self.task1, self.task2])
        
        # delete taskList
        tasksPage.clickOnNameOfTaskList(self.taskListName)
        tasksPage.clickOnOptions()
        tasksPage.clickOnDelete()
        
    def tearDown(self):
        self.driver.close()    
    