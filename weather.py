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
        t_max=temperature_container[0].text.strip("°")
        t_min=temperature_container[1].text.strip().strip("/").strip().strip("°")
        return [t_max,t_min]
        
    def weather_2(self):
        #wetteronline.de
        link="https://www.wetteronline.de/wetter/dresden"
        page_response = requests.get(link, timeout=30)
        page_content = bs4(page_response.content, "html.parser")
        main_container=page_content.find("table",{"id":"weather"})
        t_max=main_container.find("tr",{"class":"Maximum Temperature"}).find_all("span")[1].text.split("°")[0]
        t_min=main_container.find("tr",{"class":"Minimum Temperature"}).find_all("span")[1].text.split("°")[0]
        return [t_max,t_min]
        
    def weather_3(self):
        #weather.com (google)
        fahrenheit=lambda x:(x-32)*(5/9)
        link="https://weather.com/weather/monthly/l/GMXX0025:1:GM"
        page_response=requests.get(link,timeout=30)
        page_content = bs4(page_response.content, "html.parser")
        main_container=page_content.find("section",{"class":"today-historical"})
        t_max=main_container.find("td",{"class":"col-high"}).find("span").text
        t_min=main_container.find("td",{"class":"col-low"}).find("span").text
        return [fahrenheit(int(t_max)),fahrenheit(int(t_min))]
        
    def weather_4(self):
        pass
        
    def __init__(self):
        self.link1=self.weather_1() 
        self.link2=self.weather_2()        
        self.link3=self.weather_3()
        
        
wetter_dresden=Weather()
