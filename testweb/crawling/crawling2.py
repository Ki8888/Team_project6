from bs4 import BeautifulSoup as bs4
import sqlite3
import time
import requests
import re
from datetime import datetime

#age 40 top 10 news
url = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=age&subType=40'

con = sqlite3.connect('db1.sqlite3')
query1 = "CREATE TABLE age20 (title TEXT, company TEXT)"
query2 = "CREATE TABLE section (title TEXT, section TEXT)"
con.execute(query1)
con.execute(query2)
con.commit()
con.close()

#for j in i:
  #c = new + str(j)
  #url = requests.get(c)
urls = requests.get(url)
print(urls)
if urls.status_code == 200:
  soup = bs4(urls.content, 'html.parser')
  a = soup.find_all('div', {'class' : 'ranking_text'}) #len 10
  with sqlite3.connect('db1.sqlite3') as con : #with : 자동 close
    cur = con.cursor()
    title = str()
    com = str()
    for loop in a:
      act2 = str(loop)
      cc = bs4(act2, 'html.parser')
      #h_1 = cc.find('a',{'class':'title'}) #제목 title필요
      title = cc.find('a').attrs['title']
      company = cc.find('div',{'class':'ranking_office'}) #언론사
      company = company.get_text()
      cur.execute('INSERT INTO age20(title, company) VALUES (?,?)',(title,company))
    con.commit()
    print('age', type(a), len(a))
  #b = soup.find_all('div', {"class" : 'ranking_office'})

  #section news ranking
qqq = datetime.today().strftime("%Y%m%d")
dic = {100:'정치', 101:'경제', 102:'사회', 103:'생활_문화', 104:'세계', 105:'IT_과학' }

for i in dic:
  qqq = datetime.today().strftime("%Y%m%d")
  url_1 = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId='+str(i)+'&date='+str(qqq) #section id , data변경
  print(url_1)
  urls_1 = requests.get(url_1)
  if urls_1.status_code == 200:
    soup1 = bs4(urls_1.content, 'html.parser')
    d = soup1.find_all('div', {'class' : 'ranking_text'}) #len 10
    for loop in d:
      act3 = str(loop)
      ccc = bs4(act3, 'html.parser')
      title = ccc.find('a').attrs['title']
      section = dic[i]
      cur.execute('INSERT INTO section(title, section) VALUES (?,?)',(title,section))
    con.commit()
    print('section', type(d), len(d))
  #b = soup.find_all('div', {"class" : 'ranking_office'})

# age /section table join
con.execute('create table summ (title TEXT, section TEXT, company TEXT)')
con.execute('insert into summ (title, section, company) select section.title, section.section, age20.company from section inner join age20 on section.title = age20.title')
con.commit()
con.close()


