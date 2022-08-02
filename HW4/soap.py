# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from termcolor import colored
import json
   
start_url = 'https://ordi.eu/sulearvutid?___store=en&___from_store=et#___from_store=et&___store=en'

#print(page)
def parse(start_urls):
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    computers_list = soup.find_all(class_ = 'products-grid')
   # print(computers_list)
    
    for computer in computers_list:
        data = {'name':'', 'pieces':'', 'minifigs':'', 'image':'',}
        for li in computer.findAll('li'):
            data = {'name':'', 'priece':'',  'image':'',}
            
            data['name'] = li.h2.get_text()

            data['priece'] = li.find('span').get_text().replace('\u20ac','')
        
            data['image'] = li.find('img')['src']
            with open('soap.json','a+') as f:
                f.write(json.dumps(data) + ',\n')
            print(data)
   
    

   
    try:    
        next_page = soup.find(class_ = 'next')['href']
        if next_page:
            print(colored(next_page,'red'))
            parse(next_page)
    except:
        print("No more pages")
        with open("soap.json", "r") as file:
            last_line = file.readlines()[-1]
        with open('soap.json','a+') as f:
            last_line = last_line[:-2]
            f.write(last_line)
            f.write('\n]')
            


if __name__ == '__main__':
    with open('soap.json','a+') as f:
        f.write('[\n')
    parse(start_url)