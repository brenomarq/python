from price_tracker import PriceTracker
from notification_manager import NotificationManager

MY_PRICE = 2000

price_tracker = PriceTracker()
notification_manager = NotificationManager()

price = price_tracker.search_price()

if price < MY_PRICE:
    notification_manager.send_mail(price)

