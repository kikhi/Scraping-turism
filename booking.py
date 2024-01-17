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


"""

Start web page

"""

driver.get('https://www.booking.com/index.es-mx.html?aid=2369661&pagename=es-mx-booking-desktop&label=msn-g8oUdDjZhFsaZPM5Pleo8A-80127097831937:tikwd-80127272512999:loc-119:neo:mte:lp151132:dec:qsbooking&utm_campaign=Spanish_Mexico%20ES%20MX&utm_medium=cpc&utm_source=bing&utm_term=g8oUdDjZhFsaZPM5Pleo8A&msclkid=850613ec8b5e1e15119b76a758db412b&utm_content=Booking%20-%20Desktop')
sleep(10)


"""

Actions

"""
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561"]')))\
    .click()


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@class="eb46370fe1"]')))\
    .send_keys('Tijuana')
print("1 Nombre")
sleep(5)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-testid="date-display-field-start"]')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-date="2024-01-17"]')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-date="2024-01-18"]')))\
    .click()


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@class="a83ed08757 c21c56c305 a4c1805887 f671049264 d2529514af c082d89982 cceeb8986b"]')))\
    .click()
print("2 Marca calendario")
sleep(10)
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/h3/a/div[1]')))\
    .click()

sleep(10)
driver.switch_to.window(driver.window_handles[1])
print("3 Segunda ventana seleccionada")

print("INICIO DE ESCANEO DE PAGINAS DE ENLACES")
sleep(10)
paginas = driver.find_elements(By.XPATH, '//li[@class="b16a89683f"]')
sleep(10)
pagina_texto = [pagina.text for pagina in paginas]
print("PAGINAS COMPLETO")
#numero_mayor = pagina_texto.pop()
numero_mayor = min(pagina_texto)
numero_mayor = int(numero_mayor)
print("Longitud de titulos_texto:", numero_mayor)
enlaces = []
print("TERMINADO ESCANEO DE PAGINAS DE ENLACES")

for x in range(1, numero_mayor + 1):
    print("Pagina ", x)  
    sleep(5)
    for titulos in driver.find_elements(By.XPATH, '//div[@data-testid="property-card-container"]'):
        enlace = titulos.find_element(By.XPATH, './/a').get_attribute('href')
        enlaces.append(enlace)
        print(enlace)
    try:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                          '//*[@class="b16a89683f cab1524053"]')))\
        .click()
    except:
        print("Fin de conteo de paginas")


titulos_texto_total = []
tipo_texto_total = []
ratings_texto_total = []
huespedes_texto_total = []
habitaciones_texto_total = []
camas_texto_total = []
baños_texto_total = []
precios_texto_total = []
conjuntos_texto_total = []
servicios_texto_total = []
limpiezas_texto_total = []
comunicaciones_texto_total = []
llegadas_texto_total = []
presiciones_texto_total = []
ubicaciones_texto_total = []
calidad_precios_texto_total = []
conjuntos2_texto_total = []
links_texto_total = []


print("Click al boton Inicio")
for enlace in enlaces:
    driver.get(enlace)

    sleep(5)
    WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-testid="fr-read-all-reviews"]')))\
    .click()

    sleep(500000)  


    titulos = driver.find_elements(By.XPATH, '//*[@class="d2fee87262 pp-header__title"]')
    ratings = driver.find_elements(By.XPATH, '//*[@data-testid="review-score-right-component"]')

    titulos_texto_total.extend([titulo.text for titulo in titulos])
    ratings_texto_total.extend([rating.text for rating in ratings])

    print("Longitud de titulos_texto:", len(titulos_texto_total))
    print("Longitud de titulos_texto:", len(ratings_texto_total))


print("Fin de recopilacion")
sleep(5)


"""

Document builder

"""
datos = pd.DataFrame({
    'Titulo': titulos_texto_total,
    'Ratings': ratings_texto_total
})

datos.to_csv('booking-data.csv', index=True, na_rep='-')


"""
otbc.datos@gmail.com
"""