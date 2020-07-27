import requests
import re
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient

client = MongoClient('mongodb://172.17.0.3:27017/')
mydb = client.mydb

res = requests.get('http://media.daum.net/economic/')
if res.status_code == 200:
    soup = bs(res.content, 'html.parser')  #parsing1
    links = soup.find_all('div', class_='item_relate')
    for link in links:
      print(link)
      linkstr = str(link)
      linkstr = bs(linkstr, 'html.parser')  #pasrsing2
      title = linkstr.find('a').get_text() #title

      linkori = linkstr.find('a')
      link = linkori.get('href') #link
      #linkad = linkstr.find('a',{'attr':'href'}) ??
      source = linkstr.find('span').get_text() #source
      print(title, link, source)

      data = {'title':title, 'href':link, 'source':source}
      board_info = mydb.board.insert_one(data)
      


print('Data inserted..', res.inserted_ids) #????
board_info = mydb.board.find() #get collection with find()

for info in board_info: #Cursor
    print(info)
client.close()