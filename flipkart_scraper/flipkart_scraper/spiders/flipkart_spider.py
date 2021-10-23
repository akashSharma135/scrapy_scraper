import scrapy
from ..items import FlipkartScraperItem
import sys


class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    allowed_domains = ['flipkart.com']
    # Enter product type
    product_type = 'laptop'
    page_number = 2
    start_urls = [f'https://www.flipkart.com/search?q={product_type}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']


    def parse(self, response):
        items = FlipkartScraperItem()
        product_name = response.css('._4rR01T')
        product_features = response.css('.rgWa7D')
        product_price = response.css('._1_WHN1')
        product_image = response.css('._2QcLo- ._3exPp9')
        product_rating = response.css('._1lRcqv ._3LWZlK')
        
        
        
        items['product_name'] = product_name.css('::text').extract() if product_name  else None
        items['product_features'] = product_features.css('::text').extract() if product_features else None
        items['product_price'] = product_price.css('::text').extract() if product_price else None
        items['product_image'] = product_image.css('::attr(src)').extract() if product_image else None
        items['product_rating'] = product_rating.css('::text').extract() if product_rating else None
        items['product_type'] = FlipkartSpiderSpider.product_type

        yield items

        # Terminate if no data found
        if (len(product_name) == 0 and len(product_features) == 0 and len(product_rating) == 0):
            sys.exit()
            

        next_page = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + str(FlipkartSpiderSpider.page_number)


        # Go to next page
        
        FlipkartSpiderSpider.page_number += 1
        yield response.follow(next_page, callback=self.parse)

