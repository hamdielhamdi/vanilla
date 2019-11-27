from vanilla.uix._ import providers
import json, time
from threading import Thread as th

def get_meta_data_db():
    meta_data = providers()
    with open('metadata_db.json', 'w') as outfile:
        json.dump(meta_data, outfile)

def whiler():
    while True:
           t=th(target=get_meta_data_db)
           t.start()
           time.sleep(60)
           print('metadata updated!!!')

h=th(target=whiler)
h.start()

