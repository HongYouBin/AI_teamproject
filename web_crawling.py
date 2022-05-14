#출처) 야구기록실 케이비리포트 KBReport.com

import requests #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
import re
import xml.etree.ElementTree as ET
import sys

#sys.stdout = open('output.txt', 'w') 

lst = []

for i in range(1335, 1340):
    url = f"http://www.kbreport.com/player/detail/{i}"
    res = requests.get(url)
    if res.status_code != 200:
        continue
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml") #pip install lxml


    tr = soup.find("tr", attrs={"class": "even"})
    year = str(tr.find("td").get_text())
    if tr == None or year != "2021":
        continue
    stat = tr.find_all("td", attrs={"class": "data"})

    tmp = {}

    ageLst = soup.find_all("span", attrs={"class":"player-info-1"})
    age = ageLst[1].get_text()
    age = age[3:5]
    money = str(soup.find("span", attrs={"class":"player-info-8"}).get_text())
    if money == ' ':
        money = 3000
    else:
        idx = money.find('\r')
        money = money[5:idx]
        # money = int(re.sub(",", "", money))
        money = money.replace(',',"")
    position = str(soup.find("span", attrs={"class":"player-info-4"}).get_text())
    position = position[3:]
    position = position.replace('\n',"")
    position = position.replace('\r',"")
    position = position.replace('\t',"")
    
    tmp['position'] = position
    tmp['money'] = money
    tmp['age'] = age

    if position == "투수 ":
        numOfGames = stat[6].get_text()
        era = stat[13].get_text()
        win = stat[0].get_text()
        save = stat[2].get_text()
        hold = stat[3].get_text()
        tmp['numOfGames'] = numOfGames
        tmp['era'] = era
        tmp['win'] = win
        tmp['hold'] = hold
        tmp['save'] = save
    else:
        numOfGames = stat[0].get_text()
        hit = stat[3].get_text()
        homerun = stat[4].get_text()
        stealing = stat[9].get_text()
        tmp['numOfGames'] = numOfGames
        tmp['hit'] = hit
        tmp['homerun'] = homerun
        tmp['stealing'] = stealing
    lst.append(tmp)
    #print(tmp)
    
#print(lst)
        
#sys.stdout.close()





