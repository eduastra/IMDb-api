import requests
from requests import get
from bs4 import BeautifulSoup
from contexts.contexts import AppContext

def articleTitle(self):
    data = self.soup.find("h1", class_="header").text
    return data


def body(self):
    content = self.soup.find(id="main")
    return content.find_all("div", class_="lister-item mode-advanced")


@property
def run(self):
    movieFrame = self.body()
    for movie in movieFrame:
        movieFinder = movie.find("h3", class_="lister-item-header").text
        movieTitle = movieFinder.find("a")
        movieNumbers = movie.find_all("span", attrs={"name": "nv"})
        movieGenre = movie.find("span", class_="genre").text
        movieDate = movieFinder.find("span")
        movieCast = movie.find("p", class_="").text
        movieRating = movie.find("strong").text
        movieRunTime = movie.find("span", class_="runtime")
        return movieFinder, movieTitle, movieNumbers, movieGenre, movieDate, movieCast, movieRating, movieRunTime