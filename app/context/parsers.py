import requests
from requests import get
from bs4 import BeautifulSoup
from app.config.configs import Parameters


class DataStrip:

    def __init__(self):
        pass


    def articleTitle(self, soup):
        data = soup.find("h1", class_="header").text
        return data

