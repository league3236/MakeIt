# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def spider(page,max_pages):

    while page < max_pages:
        url = "http://www.detizen.com/contest/?Idx=" + str(page)
        source_code = requests.get(url)
        
        soup = BeautifulSoup(source_code.text, 'html.parser')
        find = soup('h3')

        title = find[6].get_text()
        print('=======================================================================================')
        if title == 'QUESTION & ANSWER':
            print('event not in'+page)
        else:
            print(title)
            tname = soup('th')
            tsum = soup('td')
            number=0
            for number in range(0,9):
                print(tname[number].get_text()+" : "+tsum[number].get_text())
                number = number + 1
            cho  = soup.find_all("ul",{"class":"summary-info"})
            print(cho[0].get_text().strip())
            
        page = page+1
        print('=======================================================================================')
    return None

spider(55504,55505)
