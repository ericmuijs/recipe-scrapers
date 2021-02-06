from tests import ScraperTest

from recipe_scrapers.twentyfourkitchen import TwentyFourKitchen


class TestTwentyFourKitchenScraper(ScraperTest):

    scraper_class = TwentyFourKitchen

    def test_host(self):
        self.assertEqual("24kitchen.nl", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("24Kitchen", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Macarontaart met chocoladeganache en rood fruit", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(100, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 persons", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual("https://www.24kitchen.nl/files/styles/social_media_share/public/2017-11/Macarontaart.jpg?itok=CamTNL1G", self.harvester_class.image())

    def test_ingredients(self):
        self.assertEqual([
            '350 g puree van rood fruit',
            '25 g invertsuiker',
            '400 g melkchocolade',
            '40 g eidooier',
            '120 g bloem',
            '4 g bakpoeder',
            '1 g zout',
            '380 g kristalsuiker',
            '80 g boter',
            '300 g amandelschaafsel',
            '300 g poedersuiker',
            '4 g gele kleurstof',
            '220 g eiwit',
            '75 ml water',
            'gemengd rood fruit',
            'elektrische mixer en/of standmixer met garde',
            'taartring diameter 16 cm',
            'keukenmachine',
            'keukenthermometer',
            'spuitzak',
            'bakpapier'], self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual("Dit recept is afkomstig uit het boek De\xa0Brabander Bakt,\xa0het vervolg in boekvorm op de gelijknamige 24Kitchen-serie. Hidde de Brabander deelt zijn recepten en kennis, zodat enthousiaste thuisbakkers zelf de lekkerste, spectaculairste resultaten uit hun oven kunnen toveren. Van winegums van gin & tonic tot een eigenzinnige pavlova en natuurlijk deze prachtige macarontaart. \n\nKortom: dit boek wil je hebben en het is hier te bestellen voor €20,-!\n\nGanache\n\nDoe de fruitpuree in de pan, roer de invertsuiker erdoor en breng aan de kook. Schenk het hete mengsel over de chocolade en roer tot deze is gesmolten en goed is vermengd. Laat de ganache 18 uur rusten.\n\nTaartbodem\n\nVerwarm de oven voor op 170 °C.\n\nKlop de eidooiers luchtig met een garde of mixer. Meng de bloem met het bakpoeder, zout en de suiker. Meng het bloemmengsel door de luchtig geklopte eidooiers. Meng als laatste de zachte boter erdoor. Het beste resultaat geeft de garde in een standmixer.\n\nVet de taartring in met olie en leg hem op een met bakpapier beklede bakplaat. Druk het deeg in de vorm. Bak het deeg circa 15 minuten, verwijder de vorm. Zet de oven op 180 °C. Bak de bodem nog circa 15 minuten. Laat de bodem afkoelen.\n\nMacarons\n\nDraai voor de amandelbasis het amandelschaafsel in de keukenmachine tot een fijn poeder. Voeg de poedersuiker in drie stappen toe. Roer de kleurstof door het eiwit en spatel dit eiwitmengsel vervolgens door het amandelsuikermengsel. Zet apart.\n\nVerwarm de suiker voor de eiwitbasis met het water in een pan op matig vuur tot 118 °C. Klop het eiwit luchtig met een mixer. Neem de suikersiroop van het vuur, zet de mixer op halve snelheid en schenk de siroop bij het eiwit. Mix nog circa 5 minuten.\n\nSpatel eerst een derde en vervolgens de resterende eiwitbasis door de amandelbasis en doe het mengsel in een spuitzak. Spuit beslagrondjes van circa 3 centimeter doorsnede op een met bakpapier beklede bakplaat. Laat 30 minuten staan.\n\nVerwarm de oven voor op 115 °C. Bak de macarons circa 25 minuten. Open de ovendeur halverwege de baktijd enkele seconden zodat vrijgekomen vocht kan ontsnappen.\n\nSpuit een laagje ganache op een macaronhelft en druk er een tweede helft op. Vul de taartbodem met op zijn kant gezette macarons en decoreer met rood fruit.",
        self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(2.85, self.harvester_class.ratings())
