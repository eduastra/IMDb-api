

class DataStrip:

    def __init__(self, soup=None):
        self.soup = soup
        pass

    @property
    def articleTitle(self):
        data = self.find("h1", class_="header").text
        return data

    def body(self):
        content = self.find(id="main")
        return content.find_all("div", class_="lister-item mode-advanced")
