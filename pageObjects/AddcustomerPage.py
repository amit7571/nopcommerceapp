import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddcustomerPage():
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[@class='btn btn-primary']"
    textEmail_ID = "Email"
    textPassword_ID = "Password"
    textFirstName_ID = "FirstName"
    textLastName_ID = "LastName"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFemaleGender_xpath = "//input[@id='Gender_Female']"
    textDOB_id = "DateOfBirth"
    textCompanyName_id = "Company"
    txtCustomerRole_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdminstator_xpath = "//li[@id='32c7d3e8-811e-4e97-a4f8-7a359e811793']"
    lstitemForumModerators_xpath= "//li[@id='32c7d3e8-811e-4e97-a4f8-7a359e811793']"
    lstitemGuests_xpath = "//li[@id='32c7d3e8-811e-4e97-a4f8-7a359e811793']"
    lstitemtRegistered_xpath = "//li[normalize-space()='Registered']"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpManagerOfVendor_xpath = "//select[@id='VendorId']"
    textAdmincomment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menuitem_xpath).click()

    def clickAddNewButton (self):
        self.driver.find_element(By.XPATH,self.btnAddNew_xpath).click()

    def setEmail (self,email):
        self.driver.find_element(By.ID,self.textEmail_ID).send_keys(email)

    def  setPassword (self,password):
        self.driver.find_element(By.ID,self.textPassword_ID).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.ID,self.textFirstName_ID).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.ID,self.textLastName_ID).send_keys(lastname)

    def setGender (self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()
        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdFemaleGender_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element(By.ID,self.textDOB_id).send_keys(dob)

    def setCompanyName(self,company):
        self.driver.find_element(By.ID,self.textCompanyName_id).send_keys(company)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerRole_xpath).click()

        if role == "Adminstator":
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemAdminstator_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemForumModerators_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemtRegistered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        elif role == "Guest":
            time.sleep(3)
            self.driver.find_element(By.XPATH,"span[title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemtRegistered_xpath)

        time.sleep(3)
        #self.listitem.click() Click icon is not working on these list items so we will exexute the below java script

        self.driver.execute_script("arguments[0].click();",self.listitem)


    def setAdminContent (self,content):
        self.driver.find_element(By.XPATH,self.textAdmincomment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()















