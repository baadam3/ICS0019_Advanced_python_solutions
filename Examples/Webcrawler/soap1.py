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
print(brics_list)