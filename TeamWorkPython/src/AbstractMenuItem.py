'''
Created on Feb 22, 2016

@author: haim
'''
from AbstractPageObject import AbstractPageObject
from abc import ABCMeta

class AbstractMenuItem(AbstractPageObject):
    __metaclass = ABCMeta
    
    def __init__(self, driver_):
        AbstractPageObject.__init__(self, driver_)
        
    def clickOnTasksItem(self):
        from TasksPage import TasksPage
        self._m_driver.find_element_by_id("tab_tasks").click()
        return TasksPage(self._m_driver)
    
    def clickOnMilestones(self):
        from Milestones import Milestones
        self._m_driver.find_element_by_id("tab_milestones").click()
        return Milestones(self._m_driver)