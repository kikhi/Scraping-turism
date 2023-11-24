import requests
from bs4 import BeautifulSoup
 
url = "https://www.booking.com/searchresults.es-mx.html?ss=tijuana&label=msn-g8oUdDjZhFsaZPM5Pleo8A-80127097831937%3Atikwd-80127272512999%3Aloc-119%3Aneo%3Amte%3Alp151132%3Adec%3Aqsbooking&aid=2369661&lang=es-mx&sb=1&src_elem=sb&src=index&dest_id=-1705741&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=3&search_selected=true&search_pageview_id=faae820312c8000e&ac_meta=GhBmYWFlODIwMzEyYzgwMDBlIAAoATICZW46B3RpanVhbmFAAEoAUAA%3D&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
 
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5042.108 Safari/537.36"}
 
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
 
print(response.status_code)
 
hotel_results = []
 
for el in soup.find_all("div", {"data-testid": "property-card"}):
    hotel_results.append({
            "name": el.find("div", {"data-testid": "title"}).text.strip(),
            "link": el.find("a", {"data-testid": "title-link"})["href"],
            "location": el.find("span", {"data-testid": "address"}).text.strip(),

            #"pricing": el.find("span", {"data-testid": "price-and-discounted-price"}).text.strip(),
            #"rating": el.find("div", {"data-testid": "review-score"}).text.strip().split(" ")[0],
            "review_count": el.find("div", {"data-testid": "review-score"}).text.strip().split(" ")[1],
            "thumbnail": el.find("img", {"data-testid": "image"})['src'],
        })
 

for hotel in hotel_results:
    print("Nombre: " + hotel["name"])
    print("Enlace: " + hotel["link"])
    print("Ubicación: " + hotel["location"])
    #print("Rating: " + hotel["rating"])
    print("Review_count: " + hotel["review_count"])
    print("Thumbnail: " + hotel["thumbnail"])
    print("\n")