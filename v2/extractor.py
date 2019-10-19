import logging
from threading import Thread
from datetime import datetime

from db.database import increment_data
from providers import mosaiquefm
from providers import nesmatv
from providers import jawhrafm
from providers import sub_mosaiquefm

LOG_FILENAME = 'log.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)
logging.info('INFO : --> PROCESS EXTRACTION START @ {}'.format(datetime.now()))


def process(provider):
    logging.info('INFO : START PROCESSING EXTRACTION {0} @ {1}'.format(list(provider.keys())[0],datetime.now() ))
    bulk = list(provider.values())[0].calling_method()
    increment_data(bulk, '{}'.format(list(provider.keys())[0]))
    logging.info('INFO : FINISH PROCESSING EXTRACTION {0} @ {1}'.format(list(provider.keys())[0], datetime.now()))


def run():
    list_providers = [{'nesmatv':nesmatv}, {'jawhrafm':jawhrafm}, {'mosaiquefm':mosaiquefm},{'sub_mosaiquefm':sub_mosaiquefm}]
    for provider in list_providers :
        task = Thread(target=process, args=(provider,))
        task.start()

run()