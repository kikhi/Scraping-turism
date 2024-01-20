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
driver.maximize_window()
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
                                      '//*[@data-date="2024-01-18"]')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-date="2024-01-19"]')))\
    .click()


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@class="a83ed08757 c21c56c305 a4c1805887 f671049264 d2529514af c082d89982 cceeb8986b"]')))\
    .click()
print("2 Marca calendario")
sleep(5)
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="bodyconstraint-inner"]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/h3/a/div[1]')))\
    .click()

sleep(5)
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

#for x in range(1, numero_mayor + 1):
for x in range(1):
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
ratings_texto_total = []
personals_texto_total = []
instalaciones_texto_total = []
limpiezas_texto_total = []
conforts_texto_total = []
calidades_texto_total = []
ubicaciones_texto_total = []
comentarios_texto_total = []
fantasticos_texto_total = []
bienes_texto_total = []
aceptables_texto_total = []
malos_texto_total = []
muy_malas_texto_total = []
comentarios_ingles_texto_total = []
comentarios_español_texto_total = []
tipos_clientes_familias_texto_total = []
tipos_clientes_parejas_texto_total = []
tipos_clientes_grupos_amigos_texto_total = []
tipos_clientes_personas_solas_texto_total = []
tipos_clientes_personas_por_trabajo_texto_total = []


print("Click al boton Inicio")
for enlace in enlaces:
    driver.get(enlace)

    sleep(5)

    driver.execute_script("window.scrollBy(0, 5000);")

    titulos = driver.find_elements(By.XPATH, '//*[@class="d2fee87262 pp-header__title"]')
    ratings = driver.find_elements(By.XPATH, '//*[@data-testid="review-score-component"]')

    personals = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[10]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div[2]')    
    instalaciones = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[10]/div/div[3]/div/div[3]/div/div[2]/div[2]/div/div/div[1]/div/div[2]')
    limpiezas = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[10]/div/div[3]/div/div[3]/div/div[2]/div[3]/div/div/div[1]/div/div[2]')
    conforts = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[10]/div/div[3]/div/div[3]/div/div[2]/div[4]/div/div/div[1]/div/div[2]')
    calidades = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[10]/div/div[3]/div/div[3]/div/div[2]/div[5]/div/div/div[1]/div/div[2]')
    ubicaciones = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[10]/div/div[3]/div/div[3]/div/div[2]/div[6]/div/div/div[1]/div/div[2]')

    titulos_texto_total.extend([titulo.text for titulo in titulos])
    ratings_texto_total.extend([rating.text for rating in ratings])

    print("Longitud de titulos_texto:", len(titulos_texto_total))
    print("Longitud de rating_texto:", len(ratings_texto_total))
    

    sleep(5)
    WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-testid="review-score-component"]')))\
    .click()

    sleep(5)

    
    
    
    personals_texto_total.extend([personal.text for personal in personals])
    instalaciones_texto_total.extend([instalacion.text for instalacion in instalaciones])
    limpiezas_texto_total.extend([limpieza.text for limpieza in limpiezas])
    conforts_texto_total.extend([confort.text for confort in conforts])
    calidades_texto_total.extend([calidade.text for calidade in calidades])
    ubicaciones_texto_total.extend([ubicacione.text for ubicacione in ubicaciones])

    print("Longitud de personal_texto:", len(personals_texto_total))
    print("Longitud de titulos_texto:", len(instalaciones_texto_total))
    print("Longitud de limpieza_texto:", len(limpiezas_texto_total))
    print("Longitud de conforts_texto:", len(conforts_texto_total))
    print("Longitud de calidades_texto:", len(calidades_texto_total))
    print("Longitud de ubicaciones_texto:", len(ubicaciones_texto_total))

    WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="review_score_filter_dropdown"]')))\
    .click()

    comentarios = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/div/div/ul/li[1]/button')
    fantasticos = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/div/div/ul/li[2]/button')   
    bienes = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/div/div/ul/li[3]/button')  
    aceptables = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/div/div/ul/li[4]/button')  
    malos = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/div/div/ul/li[5]/button')   
    muy_malas = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[2]/div/div/ul/li[6]/button')  

    comentarios_texto_total.extend([comentario.text for comentario in comentarios])
    fantasticos_texto_total.extend([fantastico.text for fantastico in fantasticos])
    bienes_texto_total.extend([biene.text for biene in bienes])
    if aceptables:
        aceptables_texto_total.extend([aceptable.text for aceptable in aceptables])
    else:
        aceptables_texto_total.append("-")
    if malos:
        malos_texto_total.extend([malo.text for malo in malos])
    else:
        malos_texto_total.append("-")
    if muy_malas:
        muy_malas_texto_total.extend([muy_mal.text for muy_mal in muy_malas])
    else:
        muy_malas_texto_total.append("-")

    print("Longitud de comentarios_texto:", len(comentarios_texto_total))
    print("Longitud de fantasticos_texto:", len(fantasticos_texto_total))
    print("Longitud de bienes_texto:", len(bienes_texto_total))
    print("Longitud de acpeptables_texto:", len(aceptables_texto_total))
    print("Longitud de malos_texto:", len(malos_texto_total))
    print("Longitud de muy_malas_texto:", len(muy_malas_texto_total))

    WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="review_lang_filter_dropdown"]')))\
    .click()


    comentarios_español = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[3]/div/div/ul/li[2]/button/span[2]')
    comentarios_ingles = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[3]/div/div/ul/li[3]/button/span[2]')

    WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="reviewer_type_filter_dropdown"]')))\
    .click()
  
    tipos_clientes_familias = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/ul/li[2]/button/span[2]')
    tipos_clientes_parejas = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/ul/li[3]/button/span[2]')
    tipos_clientes_grupos_amigos = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/ul/li[4]/button/span[2]')
    tipos_clientes_personas_solas = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/ul/li[5]/button/span[2]')
    tipos_clientes_personas_por_trabajo = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[6]/div[1]/div[1]/div[1]/div/div[2]/div[15]/div/div[1]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/ul/li[6]/button/span[2]')

    comentarios_ingles_texto_total.extend([comentario_ingles.text for comentario_ingles in comentarios_ingles])
    comentarios_español_texto_total.extend([comentario_español.text for comentario_español in comentarios_español])

    tipos_clientes_familias_texto_total.extend([tipo_cliente_familia.text for tipo_cliente_familia in tipos_clientes_familias])
    tipos_clientes_parejas_texto_total.extend([tipo_cliente_pareja.text for tipo_cliente_pareja in tipos_clientes_parejas])
    
    if tipos_clientes_grupos_amigos:
        tipos_clientes_grupos_amigos_texto_total.extend([tipo_cliente_grupo_amigo.text for tipo_cliente_grupo_amigo in tipos_clientes_grupos_amigos])
    else:
        tipos_clientes_grupos_amigos_texto_total.append("0")
    if tipos_clientes_personas_solas:
        tipos_clientes_personas_solas_texto_total.extend([tipo_cliente_persona_sola.text for tipo_cliente_persona_sola in tipos_clientes_personas_solas])
    else:
        tipos_clientes_personas_solas_texto_total.append("0")
    if tipos_clientes_personas_por_trabajo:
        tipos_clientes_personas_por_trabajo_texto_total.extend([tipo_cliente_persona_por_trabajo.text for tipo_cliente_persona_por_trabajo in tipos_clientes_personas_por_trabajo])
    else:
        tipos_clientes_personas_por_trabajo_texto_total.append("0")

    print("Longitud de comentarios_ingles:", len(comentarios_ingles_texto_total))
    print("Longitud de comentarios_español:", len(comentarios_español_texto_total))
    print("Longitud de tipos_clientes_familias:", len(tipos_clientes_familias_texto_total))
    print("Longitud de tipos_clientes_parejas:", len(tipos_clientes_parejas_texto_total))
    print("Longitud de tipos_clientes_grupos_amigos:", len(tipos_clientes_grupos_amigos_texto_total))
    print("Longitud de tipos_clientes_personas_solas:", len(tipos_clientes_personas_solas_texto_total))
    print("Longitud de tipos_clientes_personas_por_trabajo:", len(tipos_clientes_personas_por_trabajo_texto_total))

    sleep(50000)





print("Fin de recopilacion")
sleep(5)


"""

Document builder

"""
datos = pd.DataFrame({
    'Titulo': titulos_texto_total,
    'Ratings': ratings_texto_total,
    'Personal Rating': personals_texto_total,
    'Instalaciones Rating': instalaciones_texto_total,
    'Total de comentarios': comentarios_texto_total,
    'Rating - Fantastico': fantasticos_texto_total,
    'Rating - bien': bienes_texto_total,
    'Rating - aceptables': aceptables_texto_total,
    'Rating - malos': malos_texto_total,
    'Rating - muy malas': muy_malas_texto_total,
    'Comentarios en español': comentarios_ingles_texto_total,
    'Comentarios en ingles': comentarios_español_texto_total,
    'tipos_clientes_familias': tipos_clientes_familias_texto_total,
    'tipos_clientes_parejas': tipos_clientes_parejas_texto_total,
    'tipos_clientes_grupos_amigos': tipos_clientes_grupos_amigos_texto_total,
    'tipos_clientes_personas_solas': tipos_clientes_personas_solas_texto_total,
    'tipos_clientes_personas_por_trabajo': tipos_clientes_personas_por_trabajo_texto_total

})

datos.to_csv('booking-data.csv', index=True, na_rep='-')


"""
otbc.datos@gmail.com
"""
