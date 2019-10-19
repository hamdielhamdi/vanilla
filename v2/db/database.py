import logging

from datetime import datetime
from pymongo import MongoClient

LOG_FILENAME = 'log.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)


def connect(host, port):
    client = MongoClient(host, port)
    db = client['prod_db_news']
    return db


def insert(db, post_data):
    posts = db.posts
    result = posts.insert_one(post_data)
    logging.info('One post: {0}'.format(result.inserted_id))


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


def increment_data(bulk, provider):
    """
    insert new rows filtered by title
    :param bulk: list of new row
    :param provider: website
    :return: //
    """
    db = connect('localhost', 27017)
    logging.info('INFO : --> CONNECT TO DATABASE @ {}'.format(datetime.now()))
    # get the existing data
    exit_collection = get(db, provider)
    logging.info('INFO : --> FETCH EXISTING DATA @ {}'.format(datetime.now()))
    exist_title = [row['title'] for row in exit_collection]
    logging.info('INFO : --> START INSERTING OBJECTS @ {0}'.format(datetime.now()))
    for row in bulk:
        if row['title'] not in exist_title:
            insert(db, row)
    logging.info('INFO : --> FINISH INSERTING OBJECTS @ {0}'.format(datetime.now()))
