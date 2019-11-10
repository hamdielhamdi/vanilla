from pymongo import MongoClient


def connect(host, port):
    client = MongoClient(host, port)
    db = client['prod_db_news']
    return db


def insert(db, post_data):
    posts = db.posts
    result = posts.insert_one(post_data)


def get_all(db):
    return db.posts.find()


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
    # get the existing data
    exit_collection = get(db, provider)
    exist_title = [row['title'] for row in exit_collection]
    for row in bulk:
        if row['title'] not in exist_title:
            insert(db, row)

