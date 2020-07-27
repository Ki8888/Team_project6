from pymongo import MongoClient

client = MongoClient('mongodb://172.17.0.3:27017/')
mydb = client.mydb
data = {'title':'mariaDB show', 'tags':['DB service']}
board_info = mydb.board.insert_one(data)
data = [{"name":"Ram", "age":"26", "city":"Hyderabad"}, {"name":"Rahim","age":"27","city":"Bangalore"}]
res = mydb.board.insert_many(data)
print('Data inserted..', res.inserted_ids)
board_info = mydb.board.find() #get collection with find()

for info in board_info: #Cursor
    print(info)
client.close()