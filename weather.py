from bs4 import BeautifulSoup as bs4
import requests

class Weather():
    def __init__(self):
        page_response = requests.get("http://www.spiegel.de/thema/index-a.html", timeout=30)
        page_content = bs4(page_response.content, "html.parser")
