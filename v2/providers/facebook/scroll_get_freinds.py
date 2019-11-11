'''
Created on  15/08/2018
@author: hamdi elhamdi
'''

import json
import pandas as pd
from vanilla.v2.providers.facebook.login import create_logged_driver


with open('config.json') as file:
    config = json.load(file)


def standalone_friends_getter():
    driver = create_logged_driver()

    # Click on Profile Name
    driver.get("https://www.facebook.com/mosaiquefm/")
    print(driver.find_element(#js_l6))




    driver.quit()
    return 'ok'

standalone_friends_getter()
