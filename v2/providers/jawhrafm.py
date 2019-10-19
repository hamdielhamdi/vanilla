from datetime import datetime

import requests
from bs4 import BeautifulSoup as bs


def conect(deep=1):
    base_url = 'https://www.jawharafm.net/ar'
    context = '/articles/%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1/%D9%88%D8%B7%D9%86%D9%8A%D8%A9/90/'
    complete_url = '{0}{1}{2}'.format(base_url, context, deep)
    print(complete_url)
    re = requests.get(complete_url)
    soup = bs(re.text, 'lxml')
    container = soup.find_all('div', {'class': 'elem_ev'})
    return container

def create_json_poyload(list_posts):
    container = conect()
    for index in list(range(2, 5)):
        for component in container:
            # datetime object containing current date and time
            now = datetime.now()
            payloyd = {'title': component.find('h2', {'class': 'titr_ev'}).text,
                       'date': component.find('span', {'class': 'dat_ev'}).text,
                       'post': component.find('p', {'class': 'disc_ev'}).text,
                       'provider': 'jawhrafm',
                       "script_ex_day": now.strftime("%d/%m/%Y %H:%M:%S"),
                       'extent': 'n'}

            list_posts.append(payloyd)
        container = conect(index)
    return list_posts


def calling_method():
    """
    call recursive method
    :return: list all post 2 days delta-time
    """
    list_posts = list()
    return create_json_poyload(list_posts)


