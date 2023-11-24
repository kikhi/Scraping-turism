from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager
from selenium.webdriver.common.keys import Keys


opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
driver = webdriver.Chrome(
    service=Service('C:\\Users\\catg_\\OneDrive\\Desktop\\OTBC\\Generador Expedia\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'),
    options=opts
)


# Start web page
driver.get('https://www.booking.com/index.es-mx.html?aid=2369661&pagename=es-mx-booking-desktop&label=msn-g8oUdDjZhFsaZPM5Pleo8A-80127097831937:tikwd-80127272512999:loc-119:neo:mte:lp151132:dec:qsbooking&utm_campaign=Spanish_Mexico%20ES%20MX&utm_medium=cpc&utm_source=bing&utm_term=g8oUdDjZhFsaZPM5Pleo8A&msclkid=850613ec8b5e1e15119b76a758db412b&utm_content=Booking%20-%20Desktop')
sleep(10)


# Actions
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561"]')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@class="eb46370fe1"]')))\
    .send_keys('Tijuana')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@class="a83ed08757 c21c56c305 a4c1805887 f671049264 d2529514af c082d89982 cceeb8986b"]')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 a16ddf9c57"]')))\
    .click()

paginas = driver.find_elements(By.XPATH, '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[4]/div[2]/nav/nav/div/div[2]/ol/li[7]')

for x in range(1, paginas + 1):
    print("Pagina ", x)

"""
a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 a16ddf9c57



WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[4]/button/span')))\
    .click()
"""




sleep(50000)

# Document builder
titulos = driver.find_elements(By.XPATH, '//div[@class="aca0ade214 aaf30230d9 cd2e7d62b0 b0db0e8ada')


for titulo in titulos:
    print(titulo.text)