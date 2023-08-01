import string
import time

from selenium import webdriver
from pageObjects.AddcustomerPage import AddcustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
import pytest
import random

class Test_003_AddCustomer():
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("******Start Test_003_AddCustomer*****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.logger.info("**********Login start*************")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**********Login Finish*************")

        self.logger.info("**********Starting AddCustomer*************")

        self.addcust = AddcustomerPage(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(1)
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickAddNewButton()

        self.logger.info("**********AddCustomer Form Open*************")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setFirstName("lion")
        self.addcust.setLastName("tiger")
        self.addcust.setPassword("test123")
        self.addcust.setGender("Male")
        self.addcust.setDOB("6/23/2023") #mm/dd/yyyy format
        self.addcust.setCompanyName("Yaman Pvt ltd")
        self.addcust.setCustomerRole("Registered")
        self.addcust.setAdminContent("this is testing")
        self.addcust.clickOnSave()


        self.logger.info("***************Save customer info************")

        self.logger.info("*******************Add customer validation starts************")
        time.sleep(5)

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("*************Add Custmer Case Pass********** ")
        else:

            self.driver.save_screenshot("./Screenshots/" + "test_addCustomer_scr.png") # Screenshot
            self.logger.error("********* Add customer Test Failed ************")

            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")




def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



