from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager
from selenium.webdriver.common.keys import Keys
import pandas as pd


opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
driver = webdriver.Chrome(
    service=Service('C:\\Users\\catg_\\OneDrive\\Desktop\\OTBC\\Generador Expedia\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'),
    options=opts
)

driver.get("https://www.booking.com/hotel/mx/hacienda-del-rio.es-mx.html?aid=2369661&label=msn-g8oUdDjZhFsaZPM5Pleo8A-80127097831937%3Atikwd-80127272512999%3Aloc-119%3Aneo%3Amte%3Alp151132%3Adec%3Aqsbooking&sid=416a71d6a9f86581f6f89a55142a27a4&all_sr_blocks=41776801_369885614_2_0_0;checkin=2024-01-17;checkout=2024-01-18;dest_id=-1705741;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=41776801_369885614_2_0_0;hpos=1;matching_block_id=41776801_369885614_2_0_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=41776801_369885614_2_0_0__208250;srepoch=1705530009;srpvid=21419d06cb57014b;type=total;ucfs=1&#tab-reviews")
driver.maximize_window()

titulos_texto_total = []
ratings_texto_total = []
personal_texto_total = []
instalaciones_texto_total = []

sleep(5)

# START
driver.execute_script("window.scrollBy(0, 5000);")

titulos = driver.find_elements(By.XPATH, '//*[@class="d2fee87262 pp-header__title"]')
ratings = driver.find_elements(By.XPATH, '//*[@data-testid="review-score-component"]')

titulos_texto_total.extend([titulo.text for titulo in titulos])
ratings_texto_total.extend([rating.text for rating in ratings])

print("Longitud de titulos_texto:", len(titulos_texto_total))
print("Longitud de titulos_texto:", len(ratings_texto_total))
    

sleep(5)
WebDriverWait(driver, 5)\
.until(EC.element_to_be_clickable((By.XPATH,
                                  '//*[@data-testid="review-score-component"]')))\
.click()

sleep(5)

personals = driver.find_elements(By.XPATH, '//*[@id=":r1o:-label"]')
instalaciones = driver.find_elements(By.XPATH, '//*[@id=":r1p:-label"]')

personal_texto_total.extend([personal.text for personal in personals])
instalaciones_texto_total.extend([instalacion.text for instalacion in instalaciones])

print("Longitud de titulos_texto:", len(titulos_texto_total))

sleep(100000)