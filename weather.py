from bs4 import BeautifulSoup as bs4
import requests

class Weather():
    def weather_1(self):
        #wetter.com
        link="https://www.wetter.com/wetter_aktuell/wettervorhersage/3_tagesvorhersage/deutschland/dresden/DE0002265.html"
        page_response = requests.get(link, timeout=30)
        page_content = bs4(page_response.content, "html.parser")
        main_container=page_content.find('div',{"class":"[ pack__item weather-strip__2 ]"})
        temperature_container=main_container.find_all("div",{"class":"text--white"})
        t_max=temperature_container[0].text
        t_min=temperature_container[1].text.strip().strip("/").strip()
        print("Wetter.com for Dresden:")
        print("T. Max: "+t_max+"\nT. Min: "+t_min)
    def __init__(self):
        self.weather_1()    
        
wetter_dresden=Weather()
