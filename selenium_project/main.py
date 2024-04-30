from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

def check_time(last_time: datetime) -> datetime:
    time_now = datetime.now()
    diff_seconds = (time_now - last_time).seconds

    if diff_seconds >= 5:
        print("5 seconds have passed.")
        buy_stuff()
        return time_now

    return last_time


def buy_stuff() -> None:
    money = int(driver.find_element(By.CSS_SELECTOR, "#money").text)
    items = driver.find_elements(By.CSS_SELECTOR, ".grayed")
    prices = driver.find_elements(By.CSS_SELECTOR, ".grayed b")

    print(len(items))
    print(len(prices))

    costs = []
    for price in prices:
        cost = int(price.text.split(" ")[-1].replace(",", ""))
        costs.append(cost)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

last_time = datetime.now()
while True:
    last_time = check_time(last_time)
    cookie.click()
