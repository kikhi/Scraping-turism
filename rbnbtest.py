from time import sleep
from turtle import pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager
from selenium.webdriver.common.keys import Keys
import pandas as pd


# Selenium configuration
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
driver = webdriver.Chrome(
    service=Service('C:\\Users\\catg_\\OneDrive\\Desktop\\OTBC\\Generador Expedia\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'),
    options=opts
)


# START WEB PAGE
driver.get('https://www.airbnb.mx/rooms/15241046?adults=1&category_tag=Tag%3A8678&children=0&enable_m3_private_room=true&infants=0&pets=0&photo_id=1498392381&check_in=2023-11-16&check_out=2023-11-21&source_impression_id=p3_1700160684_bQjdCeUIqZQDfzoz&previous_page_section_name=1000&federated_search_id=7d10e297-f5b7-41b8-8767-2849b809a632')
sleep(3)


titulos_texto_total = []

titulo = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/div/section/div[1]/span[2]/h1')

titulos = titulo.text

titulos_texto_total.append(titulos)

#titulos_texto_total.extend([titulo.text for titulo in titulos])

print("Longitud de titulos_texto:", len(titulos_texto_total))

