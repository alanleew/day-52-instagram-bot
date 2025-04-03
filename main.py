from selenium import webdriver
from selenium.webdriver.common.by import By
from os import getenv
from time import sleep

USERNAME = getenv('USERNAME')
PASSWORD = getenv('PASSWORD')

class InstaFollower:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://www.instagram.com/accounts/login/')

    def login(self):
        sleep(3)
        self.username_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        self.username_field.send_keys(USERNAME)
        self.password_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        self.password_field.send_keys(PASSWORD)
        sleep(2)
        self.login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
        self.login_button.click()
        #TODO - set conditional so that user can proceed if 2FA is prompted
        input('Did you get past the 2FA? Enter return to continue')

    def find_followers(self):
        pass

    def follow(self):
        pass

bot = InstaFollower()
bot.login()