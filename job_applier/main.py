import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keyword\
s=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redire\
ct=false&position=1&pageNum=0"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

# This logs into my linkedin profile
login_btn = driver.find_element(By.LINK_TEXT, value="Entrar")
login_btn.click()

email_session = driver.find_element(By.NAME, value="session_key")
password_session = driver.find_element(By.NAME, value="session_password")

email_session.send_keys(EMAIL)
password_session.send_keys(PASSWORD, Keys.ENTER)

time.sleep(2)  # Prevent crashing due to loading page

job_offers = driver.find_elements(By.CLASS_NAME, value="jobs-search-results__list-item")

for job in job_offers:
    job.click()

    # This saves all the jobs offers and follows the companies
    save_btn = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
    save_btn.click()

    follow_btn = driver.find_element(By.CLASS_NAME, value="follow")
    print(follow_btn.text)
    follow_btn.click()


