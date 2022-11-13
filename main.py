from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

df = pd.read_csv("StockX-Data-Contest-2019-3.csv")
allnames = [x.replace("-", " ") for x in df["Sneaker Name"].unique()]
with open('saved_dictionary.pkl', 'rb') as f:
    final_dict = pickle.load(f)

try:
    for name in allnames:
        if name not in list(final_dict.keys()):
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome()
            driver.get('https://stockx.com/fr-fr/search?s='+name)
            sleep(2)
            accept_cookies = driver.find_element(By.ID,'onetrust-accept-btn-handler')
            accept_cookies.click()
            #sleep(3)
            click_item = driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div/a')
            click_item.click()
            sleep(2)
            new_url = driver.current_url
            driver.close()
            #sleep(3)
            driver = webdriver.Chrome()
            driver.get(new_url)
            sleep(2)
            accept_cookies = driver.find_element(By.ID,'onetrust-accept-btn-handler')
            accept_cookies.click()
            color = driver.find_element(By.XPATH,"//*[contains(text(), 'Coloris')]/following-sibling::p").text
            #sleep(2)
            driver.close()
            final_dict[name] = color
except:
    with open('saved_dictionary.pkl', 'wb') as f:
        pickle.dump(final_dict, f)

with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(final_dict, f)