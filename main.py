import requests
from selenium import webdriver
import webdriver_manager
import sys

last_messageID = 'ID du dernier message dans le channel entretien'
token = 'TOKEN'
username = 'PSEUDO'
password = 'MOT DE PASSE'


def launchWebBot():
    browser = webdriver.Chrome(webdriver_manager.ChromeDriverManager().install())
    browser.get('https://panel.gtaliferp.fr/login')
    username = browser.find_element_by_name('username')
    username.send_keys(username)
    password = browser.find_element_by_name('password')
    password.send_keys(password)
    button = browser.find_element_by_css_selector(
        'body > div > div > div > div > div > div.p-4.card > div > form > div.row.mt-3 > div > button')
    button.click()
    session = browser.find_element_by_css_selector('body > div > aside > section > ul > li:nth-child(5) > a')
    session.click()
    register = browser.find_element_by_css_selector('#main > div.content-body > div > table > tbody > tr > td.actions > button')
    register.click()

def launchApp(messageID):
    running = True
    while running == True:

        try:
            response = requests.post(
                'https://discordapp.com/api/v6/channels/3393371044945264651/messages',
                headers={ 'authorization': token
                })

            json_response = response.json()

            for i, element in enumerate(json_response):
                if int(element['id']) > messageID:
                    print(element)
                    launchWebBot()
                    running = False
            sys.exit()

        except:
            continue

launchApp(last_messageID)
