import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddcustomerPage
from pageObjects.SearchCustomerPage import SearchCustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_005_SearchCustomerByName:
    baseurl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    fname=ReadConfig.getFirstName()
    lname=ReadConfig.getLastName()
    name= ReadConfig.getName()
    logger=LogGen.loggen() #Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("*************Test_005_SearchCustomerByName Starts**********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.logger.info("***************Login Start*****************")
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("**************Login Successfully*************")

        self.logger.info("**************Starting Customer Module*******")
        addcust=AddcustomerPage(self.driver)
        addcust.clickOnCustomerMenu()
        time.sleep(3)
        addcust.clickOnCustomerMenuItem()
        self.logger.info("************Customer Module Opened Successfully*******")

        self.logger.info("**************Search By Name Starts*********************")
        searchcust=SearchCustomerPage(self.driver)
        searchcust.setFirstName(self.fname)
        searchcust.setLastName(self.lname)
        searchcust.clickSearchBtn()
        time.sleep(3)
        status=searchcust.searchCustomerByName(self.name)
        assert True == status
        self.driver.close()
        self.logger.info("**************Search By Name Successful*********************")
        self.logger.info("**************Test_005_SearchCustomerByName Ends*********************")




