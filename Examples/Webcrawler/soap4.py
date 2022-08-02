# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:49:20 2019

@author: eikivi
"""

import requests
from bs4 import BeautifulSoup

   
start_url = 'http://brickset.com/sets/year-2021'

#print(page)
def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')
#    print (soup)
    
    brics_list = soup.find_all("article", class_ = 'set')
    #print(brics_list)
    
    for brick in brics_list:
        data = {'name':'', 'pieces':'', 'minifigs':'', 'image':'',}
        
        data['name'] = brick.h1.get_text()

        data['pieces'] = brick.find('div', class_='col').dd.text   
        try:
            dataminif = brick.find('dt', string='Minifigs').find_next('dd').text
            for minif in dataminif:
                data['minifigs'] = minif
        except AttributeError:
            data['minifigs'] = "No minifigs"    
        data['image'] = brick.a['href']  
        print(data)
    
    try:    
        next_page = soup.find("li", class_ = 'next').a['href']
        if next_page:
            print(next_page)
            parse(next_page)
    except:
        print("No more pages")        

if __name__ == '__main__':
    parse(start_url)