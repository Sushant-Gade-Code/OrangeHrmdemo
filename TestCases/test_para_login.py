import time

from selenium import webdriver
from Utilities.Readproperties import Readproperties

from PageObject.PageObject import LoginPage


class Test_login_param:
    Url = Readproperties.getUrl()
    # Username = Readproperties.username()
    # Password = Readproperties.password()

    def test_login__001(self,Setup,dataforLogin):
        self.driver=Setup
        self.driver.get(self.Url)
        self.lp=LoginPage(self.driver)
        time.sleep(5)
        self.lp.getUserName(dataforLogin[0])
        time.sleep(5)
        self.lp.getPassword(dataforLogin[1])
        time.sleep(5)
        self.lp.getloinButton()
        time.sleep(5)
        act_title=self.driver.title
        exp_title='OrangeHRM'
        if act_title==exp_title:
            assert True
        else:
            assert False
        time.sleep(5)
        self.lp.getmenuButton()
        time.sleep(5)
        self.lp.getLogoutBtn()
        time.sleep(5)



# from selenium import webdriver
# from Utilities.Readproperties import Readproperties
#
# from PageObject.PageObject import PageObect
#
#
# class Test_login_param:
#     Url = Readproperties.getUrl()
#     Username = Readproperties.username()
#     Password = Readproperties.password()
#
#     def test_login__001(self,Setup):
#         self.driver=Setup
#         self.driver.get(self.Url)
#         self.lp=PageObect(self.driver)
#         time.sleep(5)
#         self.lp.getUserName(self.Username)
#         time.sleep(5)
#         self.lp.getPassword(self.Password)
#         time.sleep(5)
#         self.lp.getloinButton()
#         time.sleep(5)
#         act_title=self.driver.title
#         exp_title='OrangeHRM'
#         if act_title==exp_title:
#             assert True
#         else:
#             assert False

