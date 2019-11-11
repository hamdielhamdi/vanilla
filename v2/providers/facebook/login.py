from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options
with open('config.json') as file:
    config = json.load(file)

def create_logged_driver():

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-gpu')
    options.add_argument("--disable-notifications")
    # to open chrome webbrowser and maximize the window
    driver = webdriver.Chrome(executable_path="chromedriver.exe",
                              chrome_options=options)
    # connect to the specific ip address
    driver.get("https://www.facebook.com/")

    # Login to Facebook
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(config['email'])
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys(config['password'])
    try :
        driver.find_element_by_name("login").click()
    except:

        driver.find_element_by_id("loginbutton").click()
    return driver

