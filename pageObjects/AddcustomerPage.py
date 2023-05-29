import time
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element("xpath",self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element("xpath","//p[text()=' Customers']").click()

    def clickOnAddnew(self):
        self.driver.find_element("xpath","//a[@class='btn btn-primary']").click()

    def setEmail(self, email):
        self.driver.find_element("xpath","//input[@id='Email']").send_keys(email)

    def setPassword(self, password):
        self.driver.find_element("xpath","//input[@id='Password']").send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element("xpath","//div[@class='k-multiselect-wrap k-floatwrap']").click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element("xpath","//li[contains(text(),'Registered')]")
        elif role == 'Administrators':
            self.listitem = self.driver.find_element("xpath","//li[contains(text(),'Administrators')]")
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element("xpath","//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element("xpath","//li[contains(text(),'Guests')]")
        elif role == 'Registered':
            self.listitem = self.driver.find_element("xpath","//li[contains(text(),'Registered')]")
        elif role == 'Vendors':
            self.listitem = self.driver.find_element("xpath","//li[contains(text(),'Vendors')]")
        else:
            self.listitem = self.driver.find_element("xpath","//li[contains(text(),'Guests')]")
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element("xpath","//*[@id='VendorId']"))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element("id","Gender_Male").click()
        elif gender == 'Female':
            self.driver.find_element("id","Gender_Male").click()
        else:
            self.driver.find_element("id","Gender_Male").click()

    def setFirstName(self, fname):
        self.driver.find_element("xpath","//input[@id='FirstName']").send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element("xpath","//input[@id='LastName']").send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element("xpath","//input[@id='DateOfBirth']").send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element("xpath","//input[@id='Company']").send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element("xpath","//textarea[@id='AdminComment']").send_keys(content)

    def clickOnSave(self):
        self.driver.find_element("xpath","//button[@name='save']").click()
