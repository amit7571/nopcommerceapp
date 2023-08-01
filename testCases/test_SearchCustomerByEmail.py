import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddcustomerPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test004_SearchCutomerByEmail:
    baseurl = ReadConfig.getApplicationURL()
    usename = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    email = ReadConfig.getEmail()
    fname = ReadConfig.getFirstName()
    lname = ReadConfig.getLastName()


    @pytest.mark.regression
    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("***************Test004_searchCustomerByEmail Starts***************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("***************Creating class objects ***************")
        self.lp=LoginPage(self.driver)
        self.addcust = AddcustomerPage(self.driver)
        searchcust=SearchCustomerPage(self.driver)

        self.logger.info("**** Starting Login **********")
        self.lp.setUserName(self.usename)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successfully Done ****")

        self.logger.info("******************starting customer module*******************")
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()
        self.logger.info("******************Customer module Done*******************")

        self.logger.info("*********Starting Email to search*****")
        searchcust.setEmail(self.email)
        searchcust.clickSearchBtn()
        time.sleep(3)
        status=searchcust.searchCustomerByEmail(self.email)
        assert True == status
        self.driver.close()
        self.logger.info("**********Search By email Test Done***********************")
        self.logger.info("**********Test004_searchCustomerByEmail Finished***********************")








