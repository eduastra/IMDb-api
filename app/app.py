import requests
from bs4 import BeautifulSoup
from config.configs import Parameters
from context.parsers import DataStrip


class AppContext:

    def __init__(self):
        url = requests.get(Parameters.IMDB.value)
        self.soup = BeautifulSoup(url.content, 'lxml')

    def run(self):
        print('foi')
        data = DataStrip.articleTitle(self.soup)
        return data


app = AppContext()
app.run()