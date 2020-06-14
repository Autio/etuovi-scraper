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

def save_data(data, outputfile):
    with open(outputfile + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


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

    # Get the current URL so can go through it to get new pages
    current_url = d.current_url

    i = 1
    while i < 1000:
        # Find all property cards
        cards = d.find_elements_by_class_name("ListPage__cardContainer__39dKQ")
        # Cycle through cards and get data
        for card in cards:
            card_keytext = card.find_element_by_class_name("styles__cardTitle__14F5m")
            listing_id = card.find_element_by_class_name("styles__cardLink__2Oh5I").get_attribute("id")

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
            row_data.append(listing_id)
            row_data.append(desc)
            row_data.append(address)
            row_data.append(price)
            row_data.append(size)
            row_data.append(year)

            data.append(row_data)

        # Next page
        i += 1
        d.get(current_url + "&sivu=" + str(i))
        time.sleep(0.3)

        # If there is no next page button, we know we are on the last page of results
        try:
            d.find_element_by_id("paginationNext")
        except:
            i = 1000

    # Find all property cards
    #cards = d.find_elements_by_class_name("ListPage__cardContainer__39dKQ")
    # Save the data to a file
    save_data(data, city)

    x = 1



get_city("Tampere")
