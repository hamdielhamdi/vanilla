import pymongo
from vanilla.uix.db.database import connect, get_all


def providers():
    conn = connect()
    all_ = get_all(conn)

    pro = set([prov['provider'] for prov in all_])
    return [{'count': conn.posts.find({'provider': p}).count(), 'provider': p, 'last':
        [date['script_ex_day'] for date in conn.posts.find({'provider': p}).sort('script_ex_day', pymongo.ASCENDING)][
            0]} for p in pro]
