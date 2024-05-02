import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def search_items() -> list:
    items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")

    store_items = []
    for i, price in enumerate(prices):
        text_price = price.text

        if text_price:
            cost = int(text_price.split("-")[-1].replace(",", ""))
            item = items[i]

            store_items.append({
                "item": item,
                "price": cost,
            })

    return store_items[::-1]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")

timeout = time.time() + 5
five_min = time.time() + 5*60

while True:
    cookie.click()

    if time.time() > five_min:
        cookie_rate = driver.find_element(By.ID, value="cps").text
        print(cookie_rate)
        driver.quit()
        break

    if time.time() > timeout:
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

        store_items = search_items()
        for item in store_items:
            if money >= item["price"]:
                item["item"].click()
                break

        timeout = time.time() + 5
