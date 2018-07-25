# weather_scraper
Weather Scraper can collect Today's Forecaste Information from 4 different Websites for the city of Dresden (Germany). 
It calculates the mean Temperature (for the max. und min.) and also the standard deviation.

It saves the data in data.txt in JSON Format, where the keys have the structure %d.%m.%y and contains another dictionary where
the keys are the different Website's IDs. The List within the second Dictionary contains the Max. Temperature and
Min. Temperature (in that order).

REQUISITES:
python3
  $sudo apt install python3
beautifulsoup4
  $pip3 install beautifulsoup4
requests
  $pip3 install requests
