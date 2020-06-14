from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from functools import reduce
import time

# Initialize Selenium
chrome_options = Options()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
d = webdriver.Chrome(options=chrome_options)
d.get('https://www.etuovi.com/')
d.set_window_size(1200, 920)
#d.maximize_window()

def get_city(city):
    data = []
    d.get('https://www.etuovi.com/')

    time.sleep(3)
    # Handle popups?

    submitbutton = d.find_element_by_xpath("//button[@type='submit']")
    location = d.find_element_by_name("location")
    location.click()
    location.send_keys(city  +"\n")
    time.sleep(2)

    submitbutton.click()

    time.sleep(4)

    # Find all property cards
    cards = d.find_elements_by_class_name("ListPage__cardContainer__39dKQ")


    # Cycle through cards and get data
    for card in cards:
        card_keytext = card.find_element_by_class_name("styles__cardTitle__14F5m")

        # Apartment description, address
        upper_row = card_keytext.find_element_by_class_name("flexboxgrid__col-xs-12__1I1LS")
        upper_row_data = upper_row.text.split("\n")
        desc = upper_row_data[0]
        address = upper_row_data[2]

        # Price, size, year
        lower_row = card_keytext.find_element_by_class_name("styles__itemInfo__oDGHu")
        lower_row_data = lower_row.text.split("\n")
        price = lower_row_data[1]
        size = lower_row_data[3]
        year = lower_row_data[5]

        row_data = []
        row_data.append(desc)
        row_data.append(address)
        row_data.append(price)
        row_data.append(size)
        row_data.append(year)

        data.append(row_data)

    x = 1



get_city("Tampere")
