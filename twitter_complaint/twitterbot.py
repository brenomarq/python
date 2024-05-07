import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TWITTER_URL = "https://twitter.com/home"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetComplaintTwitterBot:
    def __init__(self) -> None:
        self._driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0
        self.promised = [10, 10]

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

        self.down = download_speed
        self.up = upload_speed
        self.promised = speeds

        if download_speed < speeds[0] or upload_speed < speeds[1]:
            return True

        return False

    def twitter_login(self, email: str, password: str, user: str) -> None:
        self._driver.get(url=TWITTER_URL)
        time.sleep(5)

        email_input = self._driver.find_element(By.NAME, value="text")
        email_input.send_keys(email, Keys.ENTER)
        time.sleep(5)

        user_input = self._driver.find_element(By.NAME, value="text")
        user_input.send_keys(user, Keys.ENTER)
        time.sleep(5)

        password_input = self._driver.find_element(By.NAME, value="password")
        password_input.send_keys(password, Keys.ENTER)
        time.sleep(10)

        return None

    def send_tweet(self) -> None:
        """This method must be called only after twitter login."""
        compose_btn = self._driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
        )
        compose_btn.click()
        time.sleep(3)

        text_area = self._driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span'
        )
        text_area.send_keys(f"[This a bot text]\nHey Internet Provider! Why is my internet speed {self.down}down/\
        {self.up}up, when I pay for {self.promised[0]}down/{self.promised[1]}up?")

        post_btn = self._driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]'
        )
        post_btn.click()
