import pymongo

from vanilla.v2.db.database import connect, get_all


def providers():
    conn = connect('localhost', 27017)
    all = get_all(conn)
    pro = set([prov['provider'] for prov in all])
    return [{'count': conn.posts.find({'provider': p}).count(), 'provider': p, 'last':
        [date['script_ex_day'] for date in conn.posts.find({'provider': p}).sort('script_ex_day', pymongo.ASCENDING)][
            0]} for p in pro]
