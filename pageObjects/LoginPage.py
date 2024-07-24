from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    textbox_username_xpath = (By.XPATH, "//input[@id='Email']")
    textbox_password_xpath = (By.XPATH,"//input[@id='Password']")
    button_login_xpath = (By.XPATH,"//button[@type='submit']")
    button_logout_xpath = (By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(*LoginPage.textbox_username_xpath).clear()
        self.driver.find_element(*LoginPage.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*LoginPage.textbox_password_xpath).clear()
        self.driver.find_element(*LoginPage.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*LoginPage.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(*LoginPage.button_logout_xpath).click()









