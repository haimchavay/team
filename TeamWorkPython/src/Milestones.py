'''
Created on Feb 24, 2016

@author: haim
'''
from AbstractMenuItem import AbstractMenuItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Milestones(AbstractMenuItem):
    def __init__(self, driver_):
        AbstractMenuItem.__init__(self, driver_)
        
    def assertInPage(self):
        try:
            WebDriverWait(self._m_driver, 10).until(
                EC.presence_of_element_located((By.ID, "tab_overview")))
        except:
            assert False, "don't found the OverviewPage"    