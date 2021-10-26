import scrapy
from scrapy.http.request import Request
from ..items import FlipkartScraperItem
import sys
import time
from flipkart_scraper import urls
import re


class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    allowed_domains = ['flipkart.com']
    # Enter product type
    page_number = 2
    url_count = 1
    start_urls = urls.url_list



    # def get_data(response):
    #     product_name = response.css('._4rR01T')
    #     product_features = response.css('.rgWa7D')
    #     product_price = response.css('._1_WHN1')
    #     # product_image = response.css('._2QcLo- ._3exPp9')
    #     # product_rating = response.css('._1lRcqv ._3LWZlK')
    #     return [product_name, product_features, product_price, product_name]

    def get_grid_data(response):

        """
            method scrapes the html elements specified with css selectors
            params:
                response (str): response from the requested url
            return:
                (list): returns product_name, product_features, product_price, product_name
        """

        product_name = response.css('._2WkVRV')
        product_features = response.css('.IRpwTa')
        product_price = response.css('._30jeq3')
        # product_image = response.css('._2QcLo- ._3exPp9')
        # product_rating = response.css('._1lRcqv ._3LWZlK')
        return [product_name, product_features, product_price, product_name]


    def parse(self, response):

        """
            parses the data in response
            params:
                self (class instance)
                response (str): response from the requested url
            yield:
                item (list); yields product_name, product_features, product_price, product_type
        """

        items = FlipkartScraperItem()
        data = FlipkartSpiderSpider.get_grid_data(response)
        
        
        items['product_name'] = data[0].css('::text').extract() if data[0]  else None
        items['product_features'] = data[1].css('::text').extract() if data[1] else None
        items['product_price'] = data[2].css('::text').extract() if data[2] else None
        # items['product_image'] = data[3].css('::attr(src)').extract() if data[3] else None
        # items['product_rating'] = data[4].css('::text').extract() if data[4] else None
        starts_with = (response.url).index('=')
        ends_with = (response.url).index('&')
        string = (response.url)[starts_with + 1: ends_with]
        # items['product_type'] = re.search(r'^=.&$', response.url)
        print(string)
        items['product_type'] = string
        # time.sleep(5)
        yield items
        
        # time.sleep(3)
        
        # Terminate if no data found
        # if (len(data[0]) == 0 and len(data[1]) == 0 and len(data[2]) == 0):
        #     next_url = FlipkartSpiderSpider.start_urls[1]
            
        #     FlipkartSpiderSpider.page_number = 2
        #     if FlipkartSpiderSpider.url_count == len(FlipkartSpiderSpider.start_urls):
        #         print("EXIT:", FlipkartSpiderSpider.url_count)
        #         sys.exit()
        #     FlipkartSpiderSpider.url_count += 1
            # print("sfggfg",next_url)
            # yield Request(next_url, callback=self.parse)

        index = None
        
        try:
            index = (response.url).index('&page')
        except ValueError:
            pass
        if index:
            print("INDEXES: ", index)
            substr = response.url[:index]
            next_page = substr + '&page=' + str(FlipkartSpiderSpider.page_number)
            print("jdskhfjkdhksjgkjsfdshkj")
            print(next_page)
            FlipkartSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        else:
            next_page = response.url + '&page=' + str(FlipkartSpiderSpider.page_number)
            FlipkartSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
            


        

