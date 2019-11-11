from datetime import datetime
import requests
import re
from bs4 import BeautifulSoup as bs



#########################################################

######### used to extract national news #################

#########################################################

def conect(deep=1):
    base_url = 'https://www.babnet.net'
    context = '/regions.php?p='
    complete_url = '{0}{1}{2}'.format(base_url, context, deep)
    print(complete_url)
    re = requests.get(complete_url, allow_redirects=True)
    soup = bs(re.content, 'lxml')
    container = soup.find_all('div', {'class': 'block arabi'})

    return container


def create_json_poyload(list_posts):
    container = conect()

    for index in [21, 31, 61, 91]:
        for component in container:
            # datetime object containing current date and time
            link = component.find('h2').find('a')['href']
            re_ = requests.get('https://www.babnet.net/' + link)
            soup = bs(re_.content, 'lxml')

            now = datetime.now()

            new = []
            for line in soup.find('div', {'class': 'article_ct arabi'}).text.split('\n'):
                if ('CriteoAdblock' not in line) and ('googletag.cmd.push' not in line):
                    new.append(line.strip())
            post = ' '.join(new)

            payloyd = {'title': soup.find('h1', {'class': 'titrexx arabi'}).text.strip(),
                       'date': soup.find('div', {'class': 'art-datte arabi'}).text,
                       'post': post.replace('  ', ''),
                       'provider': 'bebnet',
                       "script_ex_day": now.strftime("%d/%m/%Y %H:%M:%S"),
                       'extent': 'r'}
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
