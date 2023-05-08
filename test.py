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

url = "https://shopee.co.th/"



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

prod_xpath = '//*[@id="main"]/div/div[2]/div/div/div[3]/div[2]/div[7]/div/div/div/div[2]/section/div/div[1]/a/div[2]'

soup = BeautifulSoup(driver.page_source,'html.parser')
print(soup.prettify())
time.sleep(3)
lis = soup.find_all('a',{'class':'LYwNSg'})
for i in lis: 
    print(i)

