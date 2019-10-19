import requests
import time
from bs4 import BeautifulSoup as bs
from datetime import datetime


def conect(deep=1):
    base_url = 'https://www.nessma.tv/ar/'
    context = '%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1-%D9%88%D8%B7%D9%86%D9%8A%D8%A9/30?page='
    complete_url = '{0}{1}{2}'.format(base_url, context, deep)
    print(complete_url)
    re = requests.get(complete_url)
    soup = bs(re.text, 'lxml')
    container = soup.find_all('div', {'class': 'post'})
    return container


def create_json_poyload(list_posts):
    global container
    container = conect()
    for index in list(range(2, 5)):
        for component in container:
            try :
                time.sleep(0.5)
                link = component.find('h2', {'class': 'entry-title'}).find('a')['href']
                re = requests.get(link)
                soup = bs(re.text, 'lxml')

                # notes : need to be supervised
                content = soup.find('div',{'id':'site-content'}).find('div',{'class':'entry-content'})

                content = (str(content)[0:str(content).find('<ul class="rrssb-buttons">')]+'<div/>')
                content = " ".join((bs(content,'lxml').text).split())

                # datetime object containing current date and time
                now = datetime.now()
                payloyd = {'title': component.find('h2', {'class': 'entry-title'}).text,
                           'date': component.find('div', {'class': 'entry-meta'}).text,
                           'post': content,
                           'provider': 'nesmatv',
                           "script_ex_day":now.strftime("%d/%m/%Y %H:%M:%S"),
                           'extent':'n'}

                list_posts.append(payloyd)
            except:
                pass
        container = conect(index)
    return list_posts


def calling_method():
    """
    call recursive method
    :return: list all post 2 days delta-time
    """
    list_posts = list()
    return create_json_poyload(list_posts)


