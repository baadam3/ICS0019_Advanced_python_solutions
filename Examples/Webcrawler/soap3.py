# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:16:14 2019

@author: eikivi
"""

from bs4 import BeautifulSoup
import requests

start_url = 'http://brickset.com/sets/year-2021'
page = requests.get(start_url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)

brics_list = soup.find_all("article", class_ = 'set')
#print(brics_list)
for brick in brics_list:
    data = {'name':'', 'pieces':'', 'minifigs':'', 'image':'',}
    
    data['name'] = brick.h1.get_text()
#    print(data['name'])

    data['pieces'] = brick.find('div', class_='col').dd.text   
    try:
        dataminif = brick.find('dt', string='Minifigs').find_next('dd').text
        for minif in dataminif:
            data['minifigs'] = minif
    except AttributeError:
        data['minifigs'] = "No minifigs"    
    data['image'] = brick.a['href']  
    print(data)