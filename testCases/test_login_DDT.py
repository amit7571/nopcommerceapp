import logging
import time

import pytest
from selenium import webdriver
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import XLUtilities

class Test_001_DDT():
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen() #logger
    path = ".//TestData/LoginData.xlsx"

    @pytest.mark.regression
    def test_loggin_ddt(self,setup):
        self.logger = logging.info("********Test_001_DDT*********")
        self.logger = logging.info("********loggin ddt test start******")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)

        self.rows=XLUtilities.getRowCount(self.path,'Sheet1')
        lst_status =[]

        for r in range(2,self.rows+1):
            self.username = XLUtilities.readData(self.path,'Sheet1',r,1)
            self.password = XLUtilities.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtilities.readData(self.path,'Sheet1',r,3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger = logging.info ("************Passed****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger=logging.info("*****Failed*****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger=logging.info("****Failed****")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger=logging.info("********Passed*****")
                    lst_status.append("Pass")
        print(lst_status)

        if "Fail" not in lst_status:
            assert True
            self.logger=logging.info("****DDT Login Test Case is Pass****")
            self.driver.close()
        else:
            assert False
            self.logger=logging.info("*****DDT login test case is failed*****")
            self.driver.close

        self.logger=logging.info("*******End of DDT login Test")
        self.logger=logging.info("********Completed Test_001_DDT*****")














