import datetime
from decimal import Decimal
from re import sub

import scrapy

from scrapy_dell_monitor.data.price import Price
from scrapy_dell_monitor.data.price_repository import PriceRepository
from scrapy_dell_monitor.helpers.email import Email


class DellMonitorSpider(scrapy.Spider):
    name = "dell-monitor"
    dell_shop_url = 'https://www.dell.com/en-ca/shop'
    monitor_url = '/dell-ultrasharp-27-infinityedge-monitor-u2717d/apd/210-ahgv'
    start_urls = [dell_shop_url + monitor_url]
    allowed_domains = ['www.dell.com/en-ca/shop']

    def __init__(self, *args, **kwargs):
        self.price_repo = PriceRepository()

    def parse(self, response):
        detailed_price = response.css("div.uDetailedPrice span.pull-right")
        original_dollar_price = detailed_price.css(
            "small::text").extract_first().strip()
        featured_dollar_price = detailed_price[1].css(
            "::text").extract_first().strip()

        original_price = self._get_price_number(original_dollar_price)
        featured_price = self._get_price_number(featured_dollar_price)

        self.logger.info("original_price=%s, feature_price=%s" %
                         (original_price, featured_price))

        price = Price(original_price, featured_price, datetime.datetime.now())
        # save price_log into the memory
        self.price_repo.add(price)

        yield price

    def _get_price_number(self, price):
        return str(Decimal(sub(r'[^\d\-.]', "", price)))

    def _send_email(self, original_price, feature_price):
        text = """original price = %s,feature price = %s""" % (original_price,
                                                               feature_price)
        email = Email()
        email.send("kuanghaochina@gmail.com", "Latest Dell price", text)
