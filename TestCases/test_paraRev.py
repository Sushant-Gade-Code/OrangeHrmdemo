from PageObject.PageObject import LoginPage
from Utilities.Readproperties import Readproperties
from selenium import webdriver
class test_para_rev__01:
    url=Readproperties.getUrl()

    def test__para_rev_001(self,Setup,getDataforlogin):
        self.driver=Setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.lp=LoginPage(self.driver)
        self.lp.getUserName(getDataforlogin[0])
        self.lp.getPassword(getDataforlogin[1])
        self.lp.getLogoutBtn()
        act_title = self.driver.title
        exp_title = 'OrangeHRM'
        if act_title==exp_title:
            self.lp.getmenuButton()
            self.lp.getLogoutBtn()
            assert True
        else :
            assert False

