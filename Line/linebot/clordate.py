# -*- coding: utf-8 -*-
import requests
import re
import MySQLdb
from bs4 import BeautifulSoup

con = MySQLdb.connect('localhost', 'root', 'kshksh3236', 'MakeIt',use_unicode = True, charset = "utf8")
cur = con.cursor()

def spider(page, max_pages):
    while page < max_pages:
        url = "http://www.detizen.com/contest/?Idx=" + str(page)
        source_code = requests.get(url)

        soup = BeautifulSoup(source_code.text, 'html.parser')
        find = soup('h3')

        title = find[6].get_text()
        print('=======================================================================================')
        if title == 'QUESTION & ANSWER':
            print('event not in' + str(page))
        else:
            # this title set
            print(title+"set up.")
            tname = soup('th')
            tsum = soup('td')

            t_area = tsum[0].get_text().strip()
            # this title set
            print(t_area)
            print("C_area set up")

            t_host = tsum[1].get_text().strip()
            # this title set
            print(t_host)
            print("C_host set up")

            t_institute = tsum[2].get_text().strip()
            # this title set
            print(t_institute)
            print("C_institute set up")

            t_period = tsum[3].get_text().strip()
            cmd = re.compile(r"(\w).*")
            matchobj = cmd.search(t_period)
            tt_period = matchobj.group(0)
            # this title set
            print(tt_period)
            print("C_period set up")

            t_target = tsum[4].get_text().strip()
            # this title set
            print(t_target)
            print("C_area set up")

            try:
                t_link = tsum[8].find('a')['href']
            # this title set
            except:
                t_link = ""
            print(t_link)
            print("C_link set up")

            try:
                cho  = soup.find_all("ul",{"class":"summary-info"})
                t_all = cho[0].get_text().strip()
            except:
                cho = soup.find_all("pre",{"class":"old-summary"})
                t_all = cho[0].get_text().strip()
            
            #t_all = cho[0].get_text().strip()
            
            print("C_all set up")

            sql = """insert into competition(C_title,C_area,C_host,C_institute,C_period,C_target,C_link,C_all)
                     values (%s, %s, %s,%s, %s, %s,%s,%s)"""
            cur.execute(sql, (title,t_area,t_host,t_institute,t_period,t_target,t_link,t_all))
            con.commit()

        page = page + 1
        print('=======================================================================================')
    return None


spider(8342,55800)

