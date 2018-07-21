from bs4 import BeautifulSoup as bs4
import requests
from time import localtime, strftime

class Weather():

    def site(self, link):
        page_response = requests.get(link, timeout=50)
        return bs4(page_response.content, "html.parser")
        
    def print_temperature(self, website, t_max,t_min):
        print("\n"+website+" --> Dresden: "+self.date+  "\n")
        print("T. Max: "+str(t_max)+"\n")
        print("T. Min: "+str(t_min)+"\n")
        print("-"*40) 
        
    def avg(self, values):
        t_max_avg=0
        t_min_avg=0
        for i,j in values:
            t_max_avg+=i
            t_min_avg+=j
        t_max_avg=round(t_max_avg/len(values))
        t_min_avg=round(t_min_avg/len(values))
        print("\n"+"Average Temperature in Dresden "+self.date+"\n")
        print("T. Max.: "+ str(t_max_avg)+"\n")
        print("T. Min.: "+ str(t_min_avg)+"\n")
        print("-"*40)
        return [t_max_avg,t_min_avg]      
        
    def weather_1(self):
        #wetter.com
        link="https://www.wetter.com/wetter_aktuell/wettervorhersage/3_tagesvorhersage/deutschland/dresden/DE0002265.html"
        page_content = self.site(link)
        main_container=page_content.find('div',{"class":"[ pack__item weather-strip__2 ]"})
        temperature_container=main_container.find_all("div",{"class":"text--white"})
        t_max=int(temperature_container[0].text.strip("°"))
        t_min=int(temperature_container[1].text.strip().strip("/").strip().strip("°"))
        self.print_temperature("Wetter.com",t_max,t_min)
        return [t_max,t_min]
        
    def weather_2(self):
        #wetteronline.de
        link="https://www.wetteronline.de/wetter/dresden"
        page_content = self.site(link)
        main_container=page_content.find("table",{"id":"weather"})
        t_max=int(main_container.find("tr",{"class":"Maximum Temperature"}).find_all("span")[1].text.split("°")[0])
        t_min=int(main_container.find("tr",{"class":"Minimum Temperature"}).find_all("span")[1].text.split("°")[0])
        self.print_temperature("Wetteronline.de",t_max,t_min)
        return [t_max,t_min]
        
    def weather_3(self):
        #weather.com (google)
        fahrenheit=lambda x:(x-32)*(5/9)
        link="https://weather.com/weather/monthly/l/GMXX0025:1:GM"
        page_content = self.site(link)
        main_container=page_content.find("section",{"class":"today-historical"})
        t_max=main_container.find("td",{"class":"col-high"}).find("span").text
        t_min=main_container.find("td",{"class":"col-low"}).find("span").text
        t_max=round(fahrenheit(int(t_max)))
        t_min=round(fahrenheit(int(t_min)))
        self.print_temperature("Weather.com",t_max,t_min)
        return [t_max,t_min]
        
    def __init__(self):
        self.date=strftime("%d"+"."+"%m"+"."+"%y")
        self.values=list()
        self.values.append(self.weather_1())
        self.values.append(self.weather_2())
        self.values.append(self.weather_3())
        self.average_temperature=self.avg(self.values)
        
wetter_dresden=Weather()
