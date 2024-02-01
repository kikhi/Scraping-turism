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

"""

Start web page

"""
driver = webdriver.Chrome()
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
    .send_keys('Rosarito')
print("1 Nombre")
sleep(5)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-testid="date-display-field-start"]')))\
    .click()

# Must update date
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-date="2024-01-26"]')))\
    .click()

# Must update date
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@data-date="2024-01-27"]')))\
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

enlaces = []

try:
    sleep(5)
    paginas = driver.find_elements(By.XPATH, '//li[@class="b16a89683f"]')
    sleep(5)
    pagina_texto = [pagina.text for pagina in paginas]
    #numero_mayor = pagina_texto.pop()
    numero_mayor = max(pagina_texto)
    numero_mayor = int(numero_mayor)
    print("Longitud de titulos_texto:", numero_mayor)
    print("PAGINAS COMPLETO")


    for x in range(1, numero_mayor + 1):
        #for x in range(1):
        print("Pagina ", x)  
        sleep(5)
        for titulos in driver.find_elements(By.XPATH, '//a[@data-testid="availability-cta-btn"]'):
            enlace = titulos.get_attribute('href')
            enlaces.append(enlace)
        
    try:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                          '//*[@class="b16a89683f cab1524053"]')))\
        .click()
    except:
        print("Fin de conteo de paginas")
except:
    for x in range(1):
        print("Pagina ", x)  
        sleep(0)
        for titulos in driver.find_elements(By.XPATH, '//a[@data-testid="availability-cta-btn"]'):
            enlace = titulos.get_attribute('href')
            enlaces.append(enlace)
        
    try:
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH,
                                          '//*[@class="b16a89683f cab1524053"]')))\
        .click()
    except:
        print("Fin de conteo de paginas")



print("TERMINADO ESCANEO DE PAGINAS DE ENLACES")




print(len(enlaces))
titulos_texto_total = []
precios_texto_total = []
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

    sleep(2)

    driver.execute_script("window.scrollBy(0, 5000);")

    titulos = driver.find_elements(By.XPATH, '//*[@id="hp_hotel_name"]/div/h2')
    sleep(1)
    ratings = driver.find_elements(By.XPATH, '//*[@id="js--hp-gallery-scorecard"]/a/div/div/div/div[1]')
    sleep(1)
    precios = driver.find_elements(By.XPATH, '//*[@id="hprt-table"]/tbody/tr[1]/td[3]/div/div[1]/div[1]/div[2]/div/span[1]')
    
    titulos_texto_total.extend([titulo.text for titulo in titulos])
    if ratings:
        ratings_texto_total.extend([rating.text for rating in ratings])
    else:
        ratings_texto_total.append("0")
    if precios:
        precios_texto_total.extend([precio.text for precio in precios])    
    else:
        precios = driver.find_elements(By.XPATH, '//*[@id="hprt-table"]/tbody/tr[1]/td[3]/div/div[1]/div[1]/div[1]/div')
        precios_texto_total.extend([precio.text for precio in precios])   

    print(len(enlaces))

    print("Longitud de titulos_texto:", len(titulos_texto_total))
    print("Longitud de rating_texto:", len(ratings_texto_total))
    print("longitud precios_texto", len(precios_texto_total))
    
    try:
        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                          '//*[@data-testid="review-score-component"]')))\
        .click()
    except:
        print("Datos en blanco")
    
    sleep(1)
    personals = driver.find_elements(By.XPATH, '//*[@id=":r1j:-label"]')    
    sleep(1)
    instalaciones = driver.find_elements(By.XPATH, '//*[@id=":r1k:-label"]')
    sleep(1)
    limpiezas = driver.find_elements(By.XPATH, '//*[@id=":r1l:-label"]')
    sleep(1)
    conforts = driver.find_elements(By.XPATH, '//*[@id=":r1m:-label"]')
    sleep(1)
    calidades = driver.find_elements(By.XPATH, '//*[@id=":r1n:-label"]')
    sleep(1)
    ubicaciones = driver.find_elements(By.XPATH, '//*[@id=":r1o:-label"]')
    
    
    categorias = [(personals, personals_texto_total),
              (instalaciones, instalaciones_texto_total),
              (limpiezas, limpiezas_texto_total),
              (conforts, conforts_texto_total),
              (calidades, calidades_texto_total),
              (ubicaciones, ubicaciones_texto_total)]

    for categoria, lista_texto_total in categorias:
        if categoria:
            lista_texto_total.extend([item.text for item in categoria])
        else:
            lista_texto_total.append("0")

    print("Longitud de personal_texto:", len(personals_texto_total))
    print("Longitud de titulos_texto:", len(instalaciones_texto_total))
    print("Longitud de limpieza_texto:", len(limpiezas_texto_total))
    print("Longitud de conforts_texto:", len(conforts_texto_total))
    print("Longitud de calidades_texto:", len(calidades_texto_total))
    print("Longitud de ubicaciones_texto:", len(ubicaciones_texto_total))

    try:
        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                          '//*[@id="review_score_filter_dropdown"]')))\
        .click()
    except:
        print("")

    comentarios = driver.find_elements(By.XPATH, '//*[@id="js--hp-gallery-scorecard"]/a/div/div/div/div[2]/div[2]')
    fantasticos = driver.find_elements(By.XPATH, '//*[@id="review_score_filter"]/div/div/ul/li[2]/button/span[2]')   
    bienes = driver.find_elements(By.XPATH, '//*[@id="review_score_filter"]/div/div/ul/li[3]/button/span[2]')  
    aceptables = driver.find_elements(By.XPATH, '//*[@id="review_score_filter"]/div/div/ul/li[4]/button/span[2]')  
    malos = driver.find_elements(By.XPATH, '//*[@id="review_score_filter"]/div/div/ul/li[5]/button/span[2]')   
    muy_malas = driver.find_elements(By.XPATH, '//*[@id="review_score_filter"]/div/div/ul/li[6]/button/span[2]')  

    categorias = [(comentarios, comentarios_texto_total),
              (fantasticos, fantasticos_texto_total),
              (bienes, bienes_texto_total),
              (aceptables, aceptables_texto_total),
              (malos, malos_texto_total),
              (muy_malas, muy_malas_texto_total)]

    for categoria, lista_texto_total in categorias:
        if categoria:
            lista_texto_total.extend([item.text for item in categoria])
        else:
            lista_texto_total.append("0")

    print("Longitud de comentarios_texto:", len(comentarios_texto_total))
    print("Longitud de fantasticos_texto:", len(fantasticos_texto_total))
    print("Longitud de bienes_texto:", len(bienes_texto_total))
    print("Longitud de acpeptables_texto:", len(aceptables_texto_total))
    print("Longitud de malos_texto:", len(malos_texto_total))
    print("Longitud de muy_malas_texto:", len(muy_malas_texto_total))

    try:
        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                          '//*[@id="review_lang_filter_dropdown"]')))\
        .click()
    except:
        print("")

    sleep(1)
    comentarios_español = driver.find_elements(By.XPATH, '//*[@id="review_lang_filter"]/div/div/ul/li[2]/button/span[2]')
    sleep(1)
    comentarios_ingles = driver.find_elements(By.XPATH, '//*[@id="review_lang_filter"]/div/div/ul/li[3]/button/span[2]')

    if comentarios_español:
        comentarios_español_texto_total.extend([comentario_español.text for comentario_español in comentarios_español])
    else:
        comentarios_español_texto_total.append("0")
    if comentarios_ingles:
        comentarios_ingles_texto_total.extend([comentario_ingles.text for comentario_ingles in comentarios_ingles])
    else:
        comentarios_ingles_texto_total.append("0")

    sleep(0)

    try:
        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                       '//*[@id="reviewer_type_filter_dropdown"]')))\
        .click()
    except:
        print("")

    sleep(1)
  
    tipos_clientes_familias = driver.find_elements(By.XPATH, '//*[@id="reviewer_type_filter"]/div/div/ul/li[2]/button/span[2]')
    tipos_clientes_parejas = driver.find_elements(By.XPATH, '//*[@id="reviewer_type_filter"]/div/div/ul/li[3]/button/span[2]')
    tipos_clientes_grupos_amigos = driver.find_elements(By.XPATH, '//*[@id="reviewer_type_filter"]/div/div/ul/li[4]/button/span[2]')
    tipos_clientes_personas_solas = driver.find_elements(By.XPATH, '//*[@id="reviewer_type_filter"]/div/div/ul/li[5]/button/span[2]')
    tipos_clientes_personas_por_trabajo = driver.find_elements(By.XPATH, '//*[@id="reviewer_type_filter"]/div/div/ul/li[6]/button/span[2]')

    if tipos_clientes_familias:
        tipos_clientes_familias_texto_total.extend([tipo_cliente_familia.text for tipo_cliente_familia in tipos_clientes_familias])
    else:
        tipos_clientes_familias_texto_total.append("0")
    if tipos_clientes_parejas:
        tipos_clientes_parejas_texto_total.extend([tipo_cliente_pareja.text for tipo_cliente_pareja in tipos_clientes_parejas])
    else:
        tipos_clientes_parejas_texto_total.append("0")
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

    sleep(0)





print("Fin de recopilacion")
sleep(5)


"""

Document builder

"""
datos = pd.DataFrame({
    'Titulo': titulos_texto_total,
    'Precio': precios_texto_total,
    'Ratings': ratings_texto_total,
    'Total de comentarios': comentarios_texto_total,
    'Personal Rating': personals_texto_total,
    'Instalaciones Rating': instalaciones_texto_total,
    'Limpieza Rating': limpiezas_texto_total,
    'Conforts Rating': conforts_texto_total,
    'Calidad Rating': calidades_texto_total,
    'Ubicacion Rating': ubicaciones_texto_total,
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
