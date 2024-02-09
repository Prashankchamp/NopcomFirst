import time

import allure
from allure_commons.types import AttachmentType

from pageObject.LoginPage import LoginClass
from utilities.Logger import LoggenClass
from utilities.readconfigfile import Readconfig


class Test_UserLogin:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log = LoggenClass.log_generator()

    def test_verify_site_01(self, setup):
        self.log.info("Test_case test_verify_site_01 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo nopcom")
        self.log.info("Page Title is -->" + self.driver.title)
        if self.driver.title == "Your store. Login":
            self.log.info("Test_case test_verify_site_01 is passed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="Test Page Title Pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_verify_site_01_PASS.png")
            assert True
        else:
            self.log.info("Test_case test_verify_site_01 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_verify_site_01_FAIL.png")
            assert False
        self.log.info("Test_case test_verify_site_01 is completed")

    def test_user_login_02(self, setup):
        self.log.info("Test_case test_user_login_02 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demonopcom")
        self.lp = LoginClass(self.driver)
        time.sleep(3)
        self.log.info("Entering email - " + self.Email)
        self.lp.Enter_Email(self.Email)
        time.sleep(3)
        self.log.info("Entering password - " + self.Password)
        self.lp.Enter_Password(self.Password)
        time.sleep(3)
        self.log.info("Click on Login Button")
        self.lp.Click_Login()
        time.sleep(3)
        if self.lp.Verify_Login_Status() == "Great":
            self.log.info("Test_case test_user_login_02 is passed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_02 is passed",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_02_PASS.png")
            self.lp.Click_Logout()
            assert True
        else:
            self.log.info("Test_case test_user_login_02 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_02_FAIL.png")
            assert False
        self.log.info("Test_case test_user_login_02 is completed")
