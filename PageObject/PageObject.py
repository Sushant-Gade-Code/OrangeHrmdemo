from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    text_Username_name="username"
    text_Password_name= "password"
    btn_login_XPATH='//button[@type="submit"]'
    drp_menu_XPATH='//span[@class="oxd-userdropdown-tab"]'
    btn_logout_COMMON_XPATH='//ul[@class="oxd-dropdown-menu"]/li'

    def __init__(self,driver):
        self.driver=driver

    def getUserName(self,userName):
        self.driver.find_element(By.NAME,self.text_Username_name).clear()
        self.driver.find_element(By.NAME,self.text_Username_name).send_keys(userName)

    def getPassword(self,password):
        self.driver.find_element(By.NAME, self.text_Password_name).clear()
        self.driver.find_element(By.NAME, self.text_Password_name).send_keys(password)

    def getloinButton(self):
        self.driver.find_element(By.XPATH, self.btn_login_XPATH).click()

    def getmenuButton(self):
        self.driver.find_element(By.XPATH, self.drp_menu_XPATH).click()

    def getLogoutBtn(self):
        all_drp=self.driver.find_element(By.XPATH, self.btn_logout_COMMON_XPATH)
        for item in all_drp:
            if item.text=='Logout':
                item.click()










