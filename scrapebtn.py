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

url = "https://www.facebook.com/?stype=lo&jlou=Afc3Y-f70LiqVGDJfVtYWYmlq_rU41EVFNcl4zSAHKgLQW7So7oHE8iJ95WoB-RWBj8bNo-Z7UYkga7TMQnekvgbhZ0xYszRvzEYu160WuxebA&smuh=53604&lh=Ac8CfIZ3fj4ZLn71Cl4"



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(10)

name = driver.find_element(By.XPATH,'//*[@id="email"]')
name.send_keys("kevinangas@gmail.com")

passw = driver.find_element(By.XPATH,'//*[@id="pass"]') 
passw.send_keys("Mikey131998x4")

#enter = driver.find_element(By.XPATH,'//*[@id="u_0_b_D4"]')
#enter.submit()

driver.get("https://shopee.co.th/%E0%B9%80%E0%B8%84%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B9%83%E0%B8%99%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99-cat.11044956?is_from_login=true")
time.sleep(5)
current_url = driver.current_url
page_content = driver.page_source

soup = BeautifulSoup(page_content,'html.parser')
lisa = soup.find_all('div',{'data-sqe':'name'})
for item in lisa: 
    print(item.text)
    print()
print("Done")
#input('Press anything to quit')
#driver.quit()
print("Finished")



