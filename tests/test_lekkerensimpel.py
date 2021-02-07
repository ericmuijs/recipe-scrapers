from tests import ScraperTest

from recipe_scrapers.lekkerensimpel import LekkerEnSimpel


class TestLekkerEnSimpelScraper(ScraperTest):

    scraper_class = LekkerEnSimpel

    def test_host(self):
        self.assertEqual("lekkerensimpel.com", self.harvester_class.host())

    def category(self):
        self.assertEqual("Hoofdgerecht", self.harvester_class.category())

    def test_author(self):
        self.assertEqual("Lekker en Simpel", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Pastaschotel met spinazie en spekjes", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 personen", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual('https://www.lekkerensimpel.com/wp-content/uploads/2021/01/IMG_9563-1920x920.jpg', self.harvester_class.image())

    def test_ingredients(self):
        self.assertEqual([
            '150 gr penne',
            '75 gr spekjes',
            '1 teentje knoflook',
            '200 gr spinazie',
            '50 gr boter',
            '50 gr bloem',
            '500 ml melk',
            '100 gr geraspte kaas plus een beetje extra',
            'tl nootmuskaat',
            'cherrytomaatjes',
            'peper'],
        self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual("Een pastaschotel gaat er eigenlijk altijd wel in hier in huis, zo ook deze pastaschotel met spinazie en spekjes. We hebben de bechamelsaus voor dit recept zelf gemaakt, niet heel lastig en heel veel lekkerder dan uit een potje! \naan de slag met de pastaschotel met spinazie\nBegin met het koken van de penne. Kook de penne beetgaar (al dente), volg hiervoor de instructies op de verpakking. Verwarm ondertussen de oven voor op 180 graden en snijd het teentje knoflook fijn. Bak de spekjes in een koekenpan zonder olie voor ongeveer 3-4 minuten. Bak dan de spinazie nog even een minuut of drie mee samen met de knoflook. Meng de spinazie en spekjes door de pasta en doe alles in een ovenschaal. \n\nDan is het nu tijd om de bechamelsaus te maken. Smelt de boter en zorg ervoor dat de boter niet bruin wordt. Voeg dan de bloem toe en roer dit tot een tot er een soort beslag ontstaat en laat even heel kort sudderen (maximaal 30 seconden). Doe dan beetje voor beetje de melk erbij en tot slot roer je de geraspte kaas, nootmuskaat en peper door de saus. \n\nGiet de saus over de pasta, nog een beetje extra geraspte kaas erover, gehalveerde cherrytomaatjes en de pastaschotel kan de oven in voor ongeveer 10-15 minuten tot de kaas gesmolten is. Eet smakelijk! \nGeen fan van spekjes? Bak dan wat kipfilet blokjes! Ook erg lekker in dit recept. \n\nBewaar het recept voor de pastaschotel met spinazie op Pinterest! \n\nmeer lekkere pasta recepten\n\n\n\n\n\n\n\n \n\n\nPasta met stoofvlees \n\n\n\n\n\n\n\n\n \n\n\nPasta alfredo met spek \n\n\n\n\n\n\n\n\n \n\n\nLasagne bolognese", self.harvester_class.instructions())

