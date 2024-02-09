from selenium.webdriver.common.by import By


class LoginClass:
    Text_Email_Xpath = "//input[@id='Email']"
    Text_Password_Xpath = "//input[@id='Password']"
    Click_LoginButton_Xpath = "//button[@type='submit']"
    Click_LogoutButton_Xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def Enter_Email(self, email):
        self.driver.find_element(By.XPATH, self.Text_Email_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_Email_Xpath).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Text_Password_Xpath).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(By.XPATH, self.Click_LoginButton_Xpath).click()

    def Click_Logout(self):
        self.driver.find_element(By.XPATH, self.Click_LogoutButton_Xpath).click()

    def Verify_Login_Status(self):
        try:
            self.driver.find_element(By.XPATH, self.Click_LogoutButton_Xpath)
            return "Great"
        except:
            return "Not Great"
