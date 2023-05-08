import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
from bs4 import BeautifulSoup 
import schedule
import requests 
import time 

url = "https://shopee.co.th/buyer/login?next=https%3A%2F%2Fshopee.co.th%2F%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2583%25E0%25B8%258A%25E0%25B9%2589%25E0%25B9%2583%25E0%25B8%2599%25E0%25B8%259A%25E0%25B9%2589%25E0%25B8%25B2%25E0%25B8%2599-cat.11044956"



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

name = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input')
name.send_keys("kevinangas@gmail.com")

passw = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div[1]/input') 
passw.send_keys("asdasd")

enter = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button')
enter.click()

time.sleep(5)