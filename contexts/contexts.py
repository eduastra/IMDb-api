import requests
from requests import get
from bs4 import BeautifulSoup

class AppContext:
    def __init__(self):
        url = requests.get(link)
        self.soup = BeautifulSoup(url.content, 'lxml')