import logging

from pymongo import MongoClient

LOG_FILENAME = 'log.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)


def connect(host, port):
    client = MongoClient(host, port)
    db = client['prod_db_news']
    return db


def get(db, provider):
    """
    get the existing document
    :param db:
    :param provider:
    :return:
    """
    collection = list()
    for row in db.posts.find({'provider': provider}):
        collection.append(row)
    return collection

a,b,c=0,0,0
db =connect('localhost', 27017)
print(db)
for i in get(db,'jawhrafm'):

    if i['polarity'] =='-1':
        a=a+1
    if i['polarity'] == '1':
        b=b+1
    if i['polarity'] =='0':
        c=c+1
    #
    # print(i['title'])
    # c = input(' polarity :: ')
    # db.posts.update({"_id": i["_id"]}, {"$set": {"polarity": c}})

print(a,b,c)