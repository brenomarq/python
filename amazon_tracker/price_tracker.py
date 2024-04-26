import requests
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.com.br/Smartphone-Samsung-Galaxy-C%C3%A2mera-Tripla/dp/B0BXB6QPH8/ref=sr_1_4?__mk_pt\
_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-4&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"

class PriceTracker:
    def __init__(self) -> None:
        response = requests.get(url=PRODUCT_URL)
        self.website = BeautifulSoup(response.text, "html.parser")

    def search_price(self) -> float:
        whole_price = self.website.select(".a-price-whole")[0].get_text()\
            .replace(".", "").replace(",", ".")
        decimal_price = self.website.select(".a-price-fraction")[0].get_text()

        total_price = float(whole_price + decimal_price)
        return total_price
