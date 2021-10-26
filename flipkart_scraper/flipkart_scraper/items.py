# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartScraperItem(scrapy.Item):
    product_name = scrapy.Field()
    # product_image = scrapy.Field()
    # product_rating = scrapy.Field()
    product_features = scrapy.Field()
    product_price = scrapy.Field()
    product_type = scrapy.Field()