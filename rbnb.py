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
driver.get('https://www.airbnb.mx/')
sleep(5)

# ACTIONS
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@class="l1ovpqvx c1b3fvnw dir dir-ltr"]')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-index="0"]')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-testid="structured-search-input-field-query"]')))\
    .send_keys('Tijuana')


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-testid="structured-search-input-search-button"]')))\
    .click()

sleep(5)

# BUILD DOCUMENT
paginas = driver.find_elements(By.XPATH, '//a[@class="l1ovpqvx c1ackr0h dir dir-ltr"]')
pagina_texto = [pagina.text for pagina in paginas]
numero_mayor = min(pagina_texto)
numero_mayor = int(numero_mayor)
print("Longitud de titulos_texto:", numero_mayor)
enlaces = []

for x in range(1, numero_mayor + 1):
    print("Pagina ", x)

    for titulos in driver.find_elements(By.XPATH, '//div[@data-testid="card-container"]'):
        enlace = titulos.find_element(By.XPATH, './/a').get_attribute('href')
        enlaces.append(enlace)
        print(enlace)

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

for enlace in enlaces:
    driver.get(enlace)
    sleep(5)
    
    titulos = driver.find_elements(By.XPATH, '//*[@class="hpipapi i1pmzyw7 dir dir-ltr"]')
    tipo = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[1]/h1')
    ratings = driver.find_elements(By.XPATH, '//*[@class="r1lutz1s dir dir-ltr"]')
    #ratings = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div[1]/div/section/h2')
    huespedes = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[1]')
    habitaciones = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[2]')
    camas = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[3]')
    baños = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div/section/div[2]/ol/li[4]')
    precios = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div')
    conjuntos = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div')
    servicios = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[3]/div/div[1]/div/div[6]/div/div[2]')#
    limpiezas = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div/section/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/div[2]')
    comunicaciones = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div/section/div[2]/div/div/div[3]/div/div/div/div/div[5]/div/div/div[2]')
    llegadas = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div/section/div[2]/div/div/div[3]/div/div/div/div/div[4]/div/div/div[2]')
    presiciones = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div/section/div[2]/div/div/div[3]/div/div/div/div/div[3]/div/div/div[2]')
    ubicaciones = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div/section/div[2]/div/div/div[3]/div/div/div/div/div[6]/div/div/div[2]')
    calidad_precios = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div/section/div[2]/div/div/div[3]/div/div/div/div/div[7]/div/div/div[2]')
    #conjuntos2 = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div/section/div[2]/div/div/div[3]/div/div/div/div')
    conjuntos2 = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div/section/div[2]/div/div/div[3]')
    #links = driver.find_elements(By.XPATH, '//*[@data-testid="map/GoogleMap"]')
    
    #links_texto_total.extend([Link.text for Link in links])

    titulos_texto_total.extend([titulo.text for titulo in titulos])
    tipo_texto_total.extend([tipos.text for tipos in tipo])
    if ratings:
        ratings_texto_total.extend([rating.text for rating in ratings])
    if ratings:
        ratings = driver.find_elements(By.XPATH, '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/div/section/div[1]/div[1]/div[2]/h2/div')
        ratings_texto_total.extend([rating.text for rating in ratings])
    else:
        ratings_texto_total.append(None) 

    huespedes_texto_total.extend([huesped.text for huesped in huespedes])
    habitaciones_texto_total.extend([habitacion.text for habitacion in habitaciones])
    if camas:
        camas_texto_total.extend([cama.text for cama in camas])
    else:
        camas_texto_total.append(None) 
    if baños:
        baños_texto_total.extend([baño.text for baño in baños])
    else:
        baños_texto_total.append(None) 
    
    precios_texto_total.extend([precio.text for precio in precios])
    conjuntos_texto_total.extend([conjunto.text for conjunto in conjuntos])
    conjuntos2_texto_total.extend([[conjunto2.text for conjunto2 in conjuntos2]])
    servicios_texto_total.extend([[servicio.text for servicio in servicios]])
    
    if limpiezas:
        limpiezas_texto_total.extend([limpiezas.text for limpiezas in limpiezas])
        comunicaciones_texto_total.extend([comunicacione.text for comunicacione in comunicaciones])
        llegadas_texto_total.extend([llegada.text for llegada in llegadas])
        presiciones_texto_total.extend([presicione.text for presicione in presiciones])
        ubicaciones_texto_total.extend([ubicacione.text for ubicacione in ubicaciones])
        calidad_precios_texto_total.extend([calidad_precio.text for calidad_precio in calidad_precios])
    else:
        limpiezas_texto_total.append(None) 
        comunicaciones_texto_total.append(None) 
        llegadas_texto_total.append(None) 
        presiciones_texto_total.append(None) 
        ubicaciones_texto_total.append(None) 
        calidad_precios_texto_total.append(None) 


    print("Longitud de titulos_texto:", len(titulos_texto_total))
    print("Longitud de tipo_texto:", len(tipo_texto_total))
    print("Longitud de ratings_texto:", len(ratings_texto_total))
    print("Longitud de huespedes_texto:", len(huespedes_texto_total))
    print("Longitud de habitaciones_texto:", len(habitaciones_texto_total))
    print("Longitud de camas_texto:", len(camas_texto_total))
    print("Longitud de baños_texto:", len(baños_texto_total))
    print("Longitud de precios_texto:", len(precios_texto_total))
    print("Longitud de precios_texto:", len(conjuntos_texto_total))
    print("Longitud de _texto:", len(servicios_texto_total))
    print("Longitud de limpiezas_texto:", len(limpiezas_texto_total))
    print("Longitud de comunicaciones_texto:", len(comunicaciones_texto_total))
    print("Longitud de llegadas_texto:", len(llegadas_texto_total))
    print("Longitud de presiciones_texto:", len(presiciones_texto_total))
    print("Longitud de ubicaciones_texto:", len(ubicaciones_texto_total))
    print("Longitud de calidad_precios_texto:", len(calidad_precios_texto_total))
    print("Longitud de conjuntos2_texto:", len(conjuntos2_texto_total))
    #print("Longitud de links_texto:", len(links_texto_total))


datos = pd.DataFrame({
    'Rentado': tipo_texto_total,
    'Tipo': titulos_texto_total,
    'Eval_gen': ratings_texto_total,
    'Huespedes': huespedes_texto_total,
    'Habitaciones': habitaciones_texto_total,
    'Camas': camas_texto_total,
    'Baños': baños_texto_total,
    'Precio': precios_texto_total,
    'Conjunto': conjuntos_texto_total,
    'Servicios': servicios_texto_total,
    'Limpieza': limpiezas_texto_total,
    'Comunicacion': comunicaciones_texto_total,
    'Llegada': llegadas_texto_total,
    'Presentacion': presiciones_texto_total,
    'Ubicacion': ubicaciones_texto_total,
    'Calidad_precio': calidad_precios_texto_total,
    'Conjunto2': conjuntos2_texto_total,
    #'Lat_long2': links_texto_total,
    'link': enlaces
})

datos.to_csv('rbnb-data.csv', index=True, na_rep='-')



