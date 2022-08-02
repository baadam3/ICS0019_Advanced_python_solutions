# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:37:10 2019
@author: eikivi
"""
import scrapy
import string

class OrdiSpider(scrapy.Spider):
    name = "ordi_spider"
    #a list of URLs that you start to crawl from. We'll start with one URL.
    url = "https://ordi.eu/sulearvutid?___store=en&___from_store=et"
    headers =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
            }

    def start_requests(self):  
        # Set the headers here.
        yield scrapy.http.Request(self.url, headers=self.headers) 

    def parse(self, response):

        SET_SELECTOR = '.item'
        for computer in response.css(SET_SELECTOR):
           
            NAME_SELECTOR = 'h2 ::text'
            IMAGE_SELECTOR = 'img ::attr(src)'
            PRICE_SELECTOR = '.price ::text'
            price = str(computer.css(PRICE_SELECTOR).getall())
            price = price.encode("ascii", "ignore")
            price = str(price)
            list=['b','\'','[',']','\"'] 
            price="".join(i for i in price if i not in list)
            yield {
                'name': computer.css(NAME_SELECTOR).getall(),
                'price': price,
                'image': computer.css(IMAGE_SELECTOR).getall(),
            }
        # define a selector for the "next page" link
        NEXT_PAGE_SELECTOR = '.next ::attr(href)' 
        # extract the first match, and check if it exists
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()        

        if next_page:
             url = response.urljoin(next_page)
             yield scrapy.Request(url, self.parse,  headers=self.headers)