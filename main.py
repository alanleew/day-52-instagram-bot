from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from os import getenv
from time import sleep

USERNAME = getenv('USERNAME')
PASSWORD = getenv('PASSWORD')
SEARCH_QUERY = "Apple"

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
        sleep(5)
        self.not_now_button = self.driver.find_element(By.XPATH, '//div[contains(text(), "Not now")]')
        self.not_now_button.click()


    def find_followers(self):
        sleep(5)
        self.search_button = self.driver.find_element(By.XPATH, '//svg[contains(text(), "Search")]')
        self.search_button.send_keys(SEARCH_QUERY)
        sleep(2)
        self.apple_account = self.driver.find_element(By.CSS_SELECTOR, "a[contains(text(), 'Apple')]")
        self.apple_account.click()


    def follow(self):
        ...

bot = InstaFollower()
bot.login()
bot.find_followers()