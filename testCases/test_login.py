import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import allure
from allure_commons.types import AttachmentType


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)

    def test_homePageTitle(self,setup):
        self.logger.info('*******Test_001_Login*****')
        self.logger.info("**************Verifying Home Page Title*************")
        self.driver= setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.save_screenshot('./Screenshots/test_homePageTitle_pass.png')
            self.driver.close()
            self.logger.info("****************Home page title test is pass************")
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="hometitlefail",attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("./Screenshots/test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****************Home page title test is Failed************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**************** Verifying the Loggin Test************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******Login test is pass*******")
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="logintestfail",attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("./Screenshots/test_login.png")
            self.driver.close()
            self.logger.error("*********Login Test if Failed**********")
            assert False



