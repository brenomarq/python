import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetComplaintTwitterBot:
    def __init__(self) -> None:
        self._driver = webdriver.Chrome(options=chrome_options)

    def is_internet_slow(self, url: str, speeds: list[int]) -> bool:
        self._driver.get(url)

        # Initialize speed testing
        init_btn = self._driver.find_element(By.CLASS_NAME, value="js-start-test")
        init_btn.click()

        # Wait for the analyse
        time.sleep(45)

        # Get the true download and upload speeds and compare them
        download_speed: float = float(self._driver.find_element(By.CLASS_NAME, value="download-speed").text)
        upload_speed: float = float(self._driver.find_element(By.CLASS_NAME, value="upload-speed").text)

        if download_speed < speeds[0] or upload_speed < speeds[1]:
            return True

        return False

    def send_tweet(self, url: str) -> None:
        pass




