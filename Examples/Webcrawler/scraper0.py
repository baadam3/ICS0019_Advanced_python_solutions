# -*- coding: utf-8 -*-
"""
Creating a Basic Scraper
Idea from https://www.digitalocean.com/community/tutorials/how-to-crawl-
a-web-page-with-scrapy-and-python-3
Start your scraper with the following console command:
$ scrapy runspider scraper0.py    
"""

import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider" #just a name for the spider.
    
    def start_requests(self):
        url = "http://brickset.com/sets/year-2021"    
        # Set the headers here
        headers =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
            }
        yield scrapy.http.Request(url, headers=headers)

