from threading import Thread


from db.database import increment_data
from providers import mosaiquefm, nesmatv, jawhrafm, sub_mosaiquefm, bebnet



def process(provider):
    bulk = list(provider.values())[0].calling_method()
    increment_data(bulk, '{}'.format(list(provider.keys())[0]))



def run():
    list_providers = [{'nesmatv': nesmatv}, {'jawhrafm': jawhrafm}, {'mosaiquefm': mosaiquefm},
                      {'sub_mosaiquefm': sub_mosaiquefm}, {'bebnet': bebnet}]
    for provider in list_providers:
        task = Thread(target=process, args=(provider,))
        task.start()


