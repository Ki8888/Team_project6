import pymysql

db = pymysql.connect(host='localhost', port=3306, user='scott', passwd='tiger', db='yojulabdb', charset='utf8', autocommit=True)
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute('creat table economic (release_data text, title text, link text')
cursor.execute('select * from economic')
data = cursor.fetchall()
