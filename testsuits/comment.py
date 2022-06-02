import unittest
from unittest import TestCase

from locators.drivers import Drivers
from locators.locator import locator1
from locators.locator import locator2
from locators.locator import locator3
from pages.commentlinksearch import Pythonorgs
class Mytestcase(unittest,TestCase):
    def setUp(self) -> None:
        dr= Drivers()
        self.driver=dr.driver
        chrome= Pythonorgs(self.driver)
        chrome.starting()
    def test_commenton(self):
        comm= Pythonorgs(self.driver)
        comm.comments()
    def test_joblinkk(self):
        comm= Pythonorgs(self.driver)
        comm.joblink()
    def test_searchlink(self):
        comm=Pythonorgs(self.driver)
        comm.searchbutton()
    def tearDown(self) -> None:
        self.driver.close()
if __name__=='__main__':
    unittest.main()


