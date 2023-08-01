from selenium.webdriver.common.by import By


class SearchCustomerPage:
    txtEmail_ID = "SearchEmail"
    txtFirstName_ID = "SearchFirstName"
    txtLastName_ID = "SearchLastName"
    table_xpath = "//div[@class='dataTables_scrollBody']"
    tableRows_xpath = "//div[@class='dataTables_scrollBody']//tbody/tr"
    tableColumns_xpath = "//div[@class='dataTables_scrollBody']//tbody/tr/td"
    btnSearch_xpath = "//button[@id='search-customers']"


    def __init__(self,driver):
        self.driver=driver

    def setEmail (self,email):
        self.driver.find_element(By.ID,self.txtEmail_ID).clear()
        self.driver.find_element(By.ID,self.txtEmail_ID).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFirstName_ID).clear()
        self.driver.find_element(By.ID,self.txtFirstName_ID).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txtLastName_ID).clear()
        self.driver.find_element(By.ID,self.txtLastName_ID).send_keys(lname)

    def clickSearchBtn(self):
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))


    def searchCustomerByEmail(self,email):
        flag=False
        for r in range (1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid =table.find_element(By.XPATH,'''//*[ @ id = "customers-grid"]/tbody/tr["+str(r)+"] / td[2]''').text

            print(emailid)
            if emailid == email:
                flag=True
                print (f"This is {flag} value")
                break
        return flag


    def searchCustomerByName(self,Name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH,'''//*[ @id="customers-grid"]/tbody/tr["+str(r)+"]/td[3]''').text

            if name == Name:
                flag=True
                break
        return flag














