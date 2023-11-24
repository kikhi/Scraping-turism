"""
    Captcha problems, cant fix whit:
        - vpn
        - random sleep times 
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager
from selenium.webdriver.common.keys import Keys


# Selenium configuration
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
driver = webdriver.Chrome(
    service=Service('C:\\Users\\catg_\\OneDrive\\Desktop\\OTBC\\Generador Expedia\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'),
    options=opts
)


# Start web page
"""
driver.get('https://www.expedia.com/ -Search?EGDSDatePickerFlexibilityCalendarContent-SelectedOption-date_form_nested_flexible_field=0_DAY&EGDSDateRangePicker-EndDate-date_form_field=2023-11-10&EGDSDateRangePicker-StartDate-date_form_field=2023-11-06&EGDSSearchFormLocationField-AirportCode-destination_form_field=&EGDSSearchFormLocationField-Lat-destination_form_field=&EGDSSearchFormLocationField-Location-destination_form_field=&EGDSSearchFormLocationField-Long-destination_form_field=&EGDSSearchFormLocationField-Selected-destination_form_field=&EGDSSearchFormTravelersField-Adult-Room1=2&EGDSSoftPackagesPackageType=&destination=Tijuana%2C%20Baja%20California%2C%20Mexico&destination_form_field=tijuana&endDate=2023-11-21&regionId=6143239&semdtl=&sort=RECOMMENDED&startDate=2023-11-20&theme=&useRewards=false&userIntent=')
driver.get('https://www.expedia.mx/')
driver.get('https://www.hoteles.com/en/?locale=en_US&pos=HCOM_LATAM&siteid=300400003')
"""
driver.get('https://www.expedia.mx/')
sleep(12)


# Actions
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="lodging_search_form"]/div/div/div[1]/div/div[2]/div[1]/button')))\
    .click()

sleep(5)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="destination_form_field"]')))\
    .send_keys('Tijuana')

sleep(3)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="destination_form_field"]')))\
    .send_keys(Keys.ENTER)

sleep(2)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="search_button"]')))\
    .click()

sleep(5)


# Document builder
#titulos = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div[2]')
titulos = driver.find_elements(By.XPATH, '//h3[@class="uitk-heading uitk-heading-5 overflow-wrap uitk-layout-grid-item uitk-layout-grid-item-has-row-start"]')


for titulo in titulos:
    print(titulo.text)
