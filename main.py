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
    d.get('https://www.etuovi.com/')

    time.sleep(3)

    submitbutton = d.find_element_by_xpath("//button[@type='submit']")
    location = d.find_element_by_name("location")
    location.click()
    location.send_keys(city  +"\n")


    #submitbutton = d.find_element_by_xpath("/div[1]/div/div[2]/div/form/div/div[2]/div[2]/button")

    #submitbutton = d.findElement(By.cssSelector("theme__button__1YqFK.theme__raised__1PjP0.theme__button__1YqFK.theme__squared__17Uvn.theme__solid__1imrK.theme__primary__2-g8T.Button__button__3K-jn.Button__fullWidth__1t757"));

    #// *[ @ id = "frontpage"]
   # submitbutton = d.find_element_by_class_name("theme__button__1YqFK theme__raised__1PjP0 theme__button__1YqFK theme__squared__17Uvn theme__solid__1imrK theme__primary__2-g8T Button__button__3K-jn Button__fullWidth__1t757")
    submitbutton.click()




get_city("Tampere")
