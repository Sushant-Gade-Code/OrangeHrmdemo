import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.LogInPage1 import   loginpage

from Utilities.Readproperties import Readproperties


class Test_Login_Params:
    Url = Readproperties.getUrl()
    # username = Readproperties.username()
    # password = Readproperties.password()

    def test_login_params_004(self, Setup, getDataforlogin):
        self.driver = Setup
        self.driver.get(self.Url)
        self.driver.implicitly_wait(10)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(getDataforlogin[0])
        self.lp.Enter_Password(getDataforlogin[1])
        self.lp.Click_Login()
        act_title = self.driver.title
        exp_title = 'OrangeHRM'
        if act_title == exp_title:
            self.lp.Click_MenuButton()
            self.lp.Click_Logout()
            assert True
        else:
            assert False
        self.driver.close()
