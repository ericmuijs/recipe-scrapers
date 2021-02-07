from ._abstract import AbstractScraper
import re


class LekkerEnSimpel(AbstractScraper):
    @classmethod
    def host(cls):
        return "lekkerensimpel.com"
    
    def category(self):
        return self.soup.find("div", {"class" : "recipe__meta"}).find_all("span", {"class" : "recipe__meta-title"})[0].text.strip()

    def author(self):
        return "Lekker en Simpel"

    def title(self):
        return self.soup.find("h1", {"class" : "hero__title"}).text

    def total_time(self):
        time_list = self.soup.find("div", {"class" : "recipe__meta"}).find_all("span", {"class" : "recipe__meta-title"})[2].contents
        total_time=0
        number = re.compile("\d+")
        for time_str in time_list:
            if number.findall(str(time_str)):
                total_time += int(number.findall(str(time_str))[0])
        return total_time

    def yields(self):
        return self.soup.find("div", {"class" : "recipe__meta"}).find_all("span", {"class" : "recipe__meta-title"})[1].text.strip()

    def image(self):
        return self.soup.find("div", {"class" : "hero__image image-placeholder"}).find("picture").find("img")['data-lazy-src']

    def ingredients(self):
        return [' '.join([component.text.strip() for component  in li.find_all("span")]) for li in self.soup.find("div", {"class" : "recipe__necessities"}).find_all('li')]

    def instructions(self):
        return self.soup.find('div', {'class' : 'entry__content'}).text.strip()

   