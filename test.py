import requests
from bs4 import BeautifulSoup  # Asegúrate de tener instalada la biblioteca BeautifulSoup (pip install beautifulsoup4)
import pandas as pd

# URL de la página a la que queremos hacer scraping
url = 'https://www.airbnb.mx/s/Tijuana--Baja-California--M%C3%A9xico/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&query=Tijuana%2C%20B.C.&place_id=ChIJ03tYJgI52YARViTmpK9LchQ&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click'

# Realizamos la solicitud HTTP
response = requests.get(url)

# Verificamos si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parseamos el contenido HTML de la página usando BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraemos todos los elementos con el tipo y atributo especificados
    card_containers = soup.find_all('div', {'data-testid': 'card-container'})

    # Verificamos si encontramos algún elemento
    if card_containers:
        # Creamos una lista para almacenar los títulos
        titulos = []

        # Iteramos sobre los elementos y añadimos sus textos a la lista
        for card_container in card_containers:
            titulos.append(card_container.text)

        # Creamos el DataFrame utilizando la lista de títulos
        datos = pd.DataFrame({
            'Titulo': titulos
        })

        # Guardamos el DataFrame en un archivo CSV
        datos.to_csv('expedia-data.csv', index=True, na_rep='-')

        print('Datos guardados correctamente en expedia-data.csv')
    else:
        print('No se encontraron elementos con el atributo data-testid="card-container"')
else:
    print(f'Error en la solicitud. Código de estado: {response.status_code}')



datos = pd.DataFrame({
    'Titulo': titulos
})

datos.to_csv('expedia-data.csv', index=True, na_rep='-')