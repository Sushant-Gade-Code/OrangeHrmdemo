# import pytest
#
# from PageObject.PageObject import LoginPage
# from Utilities.Excelutil import Xluti
# from Utilities.Readproperties import Readproperties
#
# class Test_Login_DDT:
#     Url = Readproperties.getUrl()
#     # username = Readconfig.getusername()
#     # password = Readconfig.getpassword()
#     # log = LogGenerator.loggen()
#     path = 'C:\\Users\\Admin\\Documents\\ddtecel.xlsx'
#
#     @pytest.mark.regression
#     def test_login_ddt_006(self, Setup):
#         self.driver = Setup
#         self.lp = LoginPage(self.driver)
#         self.rows = Xluti.getRow(self.path, 'Sheet1')
#         print("Number of rows are --->", self.rows)
#         # login_stuats=[]
#         for r in range(2, self.rows+1):
#             self.username = Xluti.getRead(self.path, 'Sheet1',r,1)
#             self.password = Xluti.getRead(self.path, 'Sheet1', r, 2)
#             self.exp_reslt = Xluti.getRead(self.path, 'Sheet1', r, 3)
#
#             self.lp.getUserName(self.username)
#             self.lp.getPassword(self.password)
#             self.lp.getloinButton()
#             self.Act_rslt = self.driver.title
#             if self.Act_rslt == self.exp_reslt:
#                         self.lp.getmenuButton()
#                         self.lp.getLogoutBtn()
#                         Xluti.getWright(self.path, 'Sheet1', r, 4,'Pass')
#                         assert True
#             else:
#                         Xluti.getWright(self.path, 'Sheet1', r, 4,'Fail')
#                         assert False
#             self.driver.close()
#
# #             if self.lp.Login_Status() == True:
# #                 if self.Exp_Stauts == "Pass":
# #                     self.driver.save_screenshot(
# #                         "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\"+self.username+self.password+"test_login_ddt_006-pass.png")
# #                     self.lp.Click_MenuButton()
# #                     self.log.info("Click on Menu button")
# #                     self.lp.Click_Logout()
# #                     self.log.info("Click on logout button")
# #                     login_stuats.append("Pass")
# #                     XLutils.writeData(self.path, 'Sheet1', r, 5,"Pass")
# #                 else:
# #                     self.driver.save_screenshot(
# #                         "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\"+self.username+self.password+"test_login_ddt_006-pass.png")
# #                     self.lp.Click_MenuButton()
# #                     self.log.info("Click on Menu button")
# #                     self.lp.Click_Logout()
# #                     self.log.info("Click on logout button")
# #                     login_stuats.append("Fail")
# #                     XLutils.writeData(self.path, 'Sheet1', r, 5,"Fail")
# #
# #
# #             else:
# #                 if self.Exp_Stauts == "Fail":
# #                     login_stuats.append("Pass")
# #                     XLutils.writeData(self.path, 'Sheet1', r, 5, "Pass")
# #                     self.driver.save_screenshot(
# #                         "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\"+self.username+self.password+"test_login_ddt_006-fail.png")
# #                     #assert False
# #
# #                 else:
# #                     login_stuats.append("Fail")
# #                     XLutils.writeData(self.path, 'Sheet1', r, 5, "Fail")
# #                     self.driver.save_screenshot(
# #                         "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\"+self.username+self.password+"test_login_ddt_006-fail.png")
# #                     #assert False
# #
# #
# #         print(login_stuats)
# #         if "Fail" not in login_stuats:
# #             self.log.info("test_login_ddt_006 is Passed")
# #             assert True
# #         else:
# #             self.log.info("test_login_ddt_006 is Failed")
# #             assert False
# #         self.driver.close()
# #         self.log.info("test_login_ddt_006 is Completed")
# #
# #
# # # pytest -v -n=3 --html=Reports/report.html -m sanity -p no:warnings
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
#
#
#
#
# # import time
# #
# # from selenium.webdriver.common.by import By
# #
# # from PageObject.PageObject import LoginPage
# # from Utilities.Excelutil import Xluti
# # from Utilities.Readproperties import Readproperties
# #
# #
# # class Test_Ddt_001:
# #     Url = Readproperties.getUrl()
# #     def test_login_ddt_001(self,Setup):
# #         self.driver=Setup
# #         self.driver.implicitly_wait(10)
# #         self.driver=self.driver.get(self.Url)
# #         self.lp=LoginPage(self.driver)
# #         File = 'C:\\Users\\Admin\\Documents\\ddtecel.xlsx'
# #         sheetname = 'Sheet1'
# #         self.row = Xluti.getRow(File, 'Sheet1')
# #         print(self.row)
# #         for r in range(2,self.row+1):
# #             self.user=Xluti.getRead(File,'Sheet1',row=r,column=1)
# #             print(self.user)
# #             self.passw = Xluti.getRead(File, 'Sheet1', row=r, column=2)
# #             exp_reslt=Xluti.getRead(File,'Sheet1', row=r, column=3)
# #             time.sleep(5)
# #             # self.lp.getUserName(self.user)
# #             # self.driver.find_element(By.NAME,"username").send_keys(self.user)
# #             time.sleep(5)
# #             self.lp.getPassword(self.passw)
# #             # self.driver.find_element(By.NAME,"password").send_keys(self.user)
# #             time.sleep(5)
# #             self.lp.getloinButton()
# #             Act_rslt=self.driver.title
# #             if Act_rslt==exp_reslt:
# #                 self.lp.getmenuButton()
# #                 self.lp.getLogoutBtn()
# #                 Xluti.getWright(File, sheetname, row=r, column=3,data="Pass")
# #                 assert True
# #             else:
# #                 Xluti.getWright(File, sheetname, row=r, column=3,data="Fail")
# #                 assert False
# #             self.driver.close()
# #
# #
# #
# #
