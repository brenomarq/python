import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv, find_dotenv
from twitterbot import InternetComplaintTwitterBot
load_dotenv(find_dotenv())

SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/home"
TWITTER_EMAIL = os.environ.get("EMAIL")
TWITTER_PASSWORD = os.environ.get("PASSWORD")
PROMISED_DOWNLOAD = 150
PROMISED_UPLOAD = 50

twitter_bot = InternetComplaintTwitterBot()

is_slow = twitter_bot.is_internet_slow(url=SPEED_URL, speeds=[PROMISED_DOWNLOAD, PROMISED_UPLOAD])

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get(url=SPEED_URL)

# # Test the internet speed
# button = driver.find_element(By.CLASS_NAME, value="js-start-test")
# button.click()

# time.sleep(45)

# # Get the results and compare to the promised by the provider
# download_speed: float = float(driver.find_element(By.CLASS_NAME, value="download-speed").text)
# upload_speed: float = float(driver.find_element(By.CLASS_NAME, value="upload-speed").text)

# if download_speed < PROMISED_DOWNLOAD or upload_speed < PROMISED_UPLOAD:
#     driver.get(url=TWITTER_URL)
#     time.sleep(3)

#     # Logs into twitter
#     login_btn = driver.find_element(By.CLASS_NAME, value="nsm7Bb-HzV7m-LgbsSe")
#     login_btn.click()

#     email_input = driver.find_element(By.CSS_SELECTOR, value="input.whsOnd")
#     email_input.send_keys(TWITTER_EMAIL)
