import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/feed")

# This logs into my linkedin profile
email_session = driver.find_element(By.NAME, value="session_key")
password_session = driver.find_element(By.NAME, value="session_password")

email_session.send_keys(EMAIL)
password_session.send_keys(PASSWORD, Keys.ENTER)
