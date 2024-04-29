import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

def check_time(time: datetime.datetime) -> bool:
    """Check if 5 seconds has passed since the last action."""
    pass

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

while True:
    cookie.click()
