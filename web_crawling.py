#출처) 야구기록실 케이비리포트 KBReport.com

import requests #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
import re
import xml.etree.ElementTree as ET
import sys

#sys.stdout = open('output.txt', 'w') 

hitterInput = []
hitterOutput = []
throwerInput= []
throwerOutput = []

for i in range(1000, 1638):
    if i == 1636: #or 1638:
        continue
    url = f"http://www.kbreport.com/player/detail/{i}"
    res = requests.get(url)
    if res.status_code != 200:
        continue
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml") #pip install lxml


    tr = soup.find("tr", attrs={"class": "even"})
    if tr == None:
        continue
    year = int(tr.find("td").get_text())
    if year != 2021:
        continue
    stat = tr.find_all("td", attrs={"class": "data"})

    tmp = []

    ageLst = soup.find_all("span", attrs={"class":"player-info-1"})
    age = ageLst[1].get_text()
    age = int(age[3:5])
    money = soup.find("span", attrs={"class":"player-info-8"}).get_text()
    money = money.replace('\n', "")
    if money == '':
        money = 30000000
    elif money[3] == '￦':
        idx = money.find('\r')
        money = money[4:idx]
        # money = int(re.sub(",", "", money))
        money = money.replace(',',"")
        money = int(money)
    elif money[3] == '＄':
        continue
    else:
        idx = money.find('\r')
        money = money[3:idx]
        # money = int(re.sub(",", "", money))
        money = money.replace(',',"")
        money = int(money)
    position = str(soup.find("span", attrs={"class":"player-info-4"}).get_text())
    position = position[3:]
    position = position.replace('\n',"")
    position = position.replace('\r',"")
    position = position.replace('\t',"")
    
    tmp.append(age)

    if position == "투수 ":
        numOfGames = int(stat[6].get_text())
        era = float(stat[13].get_text())
        win = int(stat[0].get_text())
        save = int(stat[2].get_text())
        hold = int(stat[3].get_text())
        tmp.append(numOfGames)
        tmp.append(era)
        tmp.append(win)
        tmp.append(hold)
        tmp.append(save)
        throwerInput.append(tmp)
        throwerOutput.append(money)
    else:
        numOfGames = int(stat[0].get_text())
        hit = float(stat[3].get_text())
        homerun = int(stat[4].get_text())
        stealing = float(stat[9].get_text())
        tmp.append(numOfGames)
        tmp.append(hit)
        tmp.append(homerun)
        tmp.append(stealing)
        hitterInput.append(tmp)
        hitterOutput.append(money)
    #lst.append(tmp)
    #print(tmp)
    
#print(lst)
        
#sys.stdout.close()



sys.stdout = open('Input3.txt', 'w') 
print(hitterInput)
print('\n', '\n', '\n')
print(hitterOutput)
print('\n', '\n', '\n')
print(throwerOutput)
print('\n', '\n', '\n')
print(throwerInput)

sys.stdout.close()

# sys.stdout = open('hitterInput.txt', 'w') 
# print(throwerInput)
# sys.stdout.close()

# sys.stdout = open('hitterInput.txt', 'w') 
# print(hitterOutput)
# sys.stdout.close()

# sys.stdout = open('hitterInput.txt', 'w') 
# print(throwerOutput)
# sys.stdout.close()


