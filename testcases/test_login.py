import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pageObjects.LoginPage import LoginPage
from utilites.readProperities import ReadConfig
from utilites.customlogger import LogGen


class Test_01_login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homepageTitle(self, setup):

        self.logger.info("**********************************Testing homepage title***********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**********************************Testing test_login Page***********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        time.sleep(5)
        assert "Dashboard / nopCommerce administration" in self.driver.page_source
        if "Dashboard / nopCommerce administration" in self.driver.page_source:
            assert True
            self.driver.close()
        else:
            self.logger.info(
                "**********************************Else condition fail and saving screenshot of the failure***********************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False


