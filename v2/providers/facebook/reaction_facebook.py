'''
Created on  16/11/2018
@author: hamdi elhamdi
'''
from time import strftime

from bs4 import BeautifulSoup as bs
import json
from datetime import datetime

from vanilla.v2.utils.tools import clean
from vanilla.v2.providers.facebook.login import create_logged_driver
from vanilla.v2.db.database import insert, connect

with open('config.json') as file:
    config = json.load(file)


def scroll_down(driver):
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    """last_height = driver.execute_script("return document.body.scrollHeight")

    this dowsnt work due to floating web elements on youtube
    """

    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    i = 0
    while i < 11:
        i = i + 1
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
        import time
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            print("break")
            break
        last_height = new_height


def extarct_facebook():
    driver = create_logged_driver()

    # Click on Profile Name
    driver.get("https://www.facebook.com/pg/mosaiquefm/posts/?ref=page_internal")

    scroll_down(driver)
    data = driver.page_source

    soup = bs(data, 'lxml')
    a = soup.find_all('div', {'class': '_5pcr userContentWrapper'})
    list_post = list()
    for i in a:
        try:
            post_content = i.find('div', {'data-testid': 'post_message'}).text
        except Exception as e:
            post_content = ""
        try:
            post_creation_date = i.find('div', {'data-testid': 'story-subtitle'}).find('abbr', {'class': '_5ptz'})[
                'title']
        except Exception as e:
            post_creation_date = ""
        # TODO : fetch all comment in post if exist
        try:
            post_comments = i.find('div', {'data-testid': 'fbFeedStoryUFI/feedbackSummary'}).find('a', {
                'data-testid': 'UFI2CommentsCount/root'}).text
        except Exception as e:
            post_comments = "0"
        try:
            post_partage = i.find('div', {'data-testid': 'fbFeedStoryUFI/feedbackSummary'}).find('a', {
                'data-testid': 'UFI2SharesCount/root'}).text
        except Exception as e:
            post_partage = "0"
        """all possible likes type"""
        try:
            post_likes_wow = i.find('span', {'data-testid': 'UFI2TopReactions/tooltip_WOW'}).find('a')['aria-label']
        except Exception as e:
            post_likes_wow = "0"
        try:
            post_likes_love = i.find('span', {'data-testid': 'UFI2TopReactions/tooltip_LOVE'}).find('a')['aria-label']
        except Exception as e:
            post_likes_love = "0"
        try:
            post_likes_like = i.find('span', {'data-testid': 'UFI2TopReactions/tooltip_LIKE'}).find('a')['aria-label']
        except Exception as e:
            post_likes_like = "0"
        try:
            post_likes_triste = i.find('span', {'data-testid': 'UFI2TopReactions/tooltip_SORRY'}).find('a')[
                'aria-label']
        except Exception as e:
            post_likes_triste = "0"

        try:
            post_likes_anger = i.find('span', {'data-testid': 'UFI2TopReactions/tooltip_ANGER'}).find('a')['aria-label']
        except Exception as e:
            post_likes_anger = "0"
        try:
            post_likes_haha = i.find('span', {'data-testid': 'UFI2TopReactions/tooltip_HAHA'}).find('a')['aria-label']
        except Exception as e:
            post_likes_haha = "0"
        if post_content is not None:
            now = datetime.now()

            user_post = {'post': clean(post_content),
                          'date': post_creation_date,
                          'post_comment': clean(post_comments),
                          'post_partage': clean(post_partage),
                          'nrb_rct_like': clean(post_likes_like),
                          'post_happy': clean(post_likes_haha),
                          'post_anger': clean(post_likes_anger),
                          'post_triste': clean(post_likes_triste),
                          'post_love': clean(post_likes_love),
                          'post_wow': clean(post_likes_wow),
                          'script_ex_day': now.strftime("%d/%m/%Y %H:%M:%S"),
                          'provider': 'facebook'}
            list_post.append(user_post)

            insert(connect('', ''), user_post)
            print(user_post)
    driver.quit()
    return 'ok'


extarct_facebook()
