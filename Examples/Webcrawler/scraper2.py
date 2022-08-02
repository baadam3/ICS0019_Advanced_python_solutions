# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:37:10 2019

@author: eikivi
"""
import scrapy


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    
    
    def start_requests(self):
        #a list of URLs that you start to crawl from. We'll start with one URL.
        url = "http://brickset.com/sets/year-2021"
    
        # Set the headers here.
        headers =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
            }
        yield scrapy.http.Request(url, headers=headers) 

    def parse(self, response):
        """
        We’ll use CSS selectors for now since CSS is the easier option and a
        perfect fit for finding all the sets on the page. If you look at the
        HTML for the page, you'll see that each set is specified with the
        class set. Since we're looking for a class, we'd use .set for our 
        CSS selector. All we have to do is pass that selector into the 
        response object
        """
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            """The brickset object we’re looping over has its own css method, 
            so we can pass in a selector to locate child elements
            """
            NAME_SELECTOR = 'h1 ::text'
            PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
            IMAGE_SELECTOR = 'img ::attr(src)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
                'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
                'image': brickset.css(IMAGE_SELECTOR).extract_first(),
            }