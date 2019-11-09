from pymongo import MongoClient


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


db =connect('localhost', 27017)
l = len(get(db, 'jawhrafm'))
print(l)
a=[]
for i in get(db, 'jawhrafm'):
    if i['polarity'] == '-1':
        a.append((i['title'],'neg'))
    if i['polarity'] == '1':
        a.append((i['title'],'pos'))
print(a)
train = a[:int(l*0.8)]
test = a[int(l*0.8):]
print(train)
from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(train)
print(cl.accuracy(test))

print(cl.classify('تعرضت للإعتداء  '))


