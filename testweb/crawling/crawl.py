import requests
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('db.sqlite3')
query = 'CREATE TABLE economic (title TEXT, link TEXT)'
conn.execute(query)
conn.commit(); conn.close()
res = requests.get('http://media.daum.net/economic/')
if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.find_all('a', class_='link_txt')
    with sqlite3.connect("db.sqlite3") as con:
        cur = con.cursor()
        title = str(); link = str()
        for link in links:
            title = str.strip(link.get_text())
            link = link.get('href')
            cur.execute("INSERT INTO economic (title,link) VALUES (?,?)",(title,link))
        con.commit()
        print('task_crawling_daum : ', type(links), len(links))