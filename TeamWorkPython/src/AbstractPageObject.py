'''
Created on Feb 22, 2016

@author: haim
'''
from abc import ABCMeta, abstractmethod
class AbstractPageObject:
    __metaclass = ABCMeta
    
    def __init__(self, driver_):
        self._m_driver = driver_
        self.assertInPage()
        
    @abstractmethod
    def assertInPage(self):
        return    