from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

INSTA_URL = "https://www.instagram.com"

class InstagramBot:
    def __init__(self) -> None:
        self._driver = webdriver.Chrome(options=chrome_options)

    def login(self, user: str, password: str) -> None:
        self._driver.get(url=INSTA_URL)

        user_input = self._driver.find_element(By.NAME, value="username")
        user_input.send_keys(user)

        password_input = self._driver.find_element(By.NAME, value="password")
        password_input.send_keys(password, Keys.ENTER)
