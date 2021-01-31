from tests import ScraperTest

from recipe_scrapers.albertheijn import AlbertHeijn


class TestAlbertHeijnScraper(ScraperTest):

    scraper_class = AlbertHeijn

    def test_host(self):
        self.assertEqual("ah.nl", self.harvester_class.host())

    def test_title(self):
        self.assertEqual('Volkoren mac and cheese met pompoen', self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(55, self.harvester_class.total_time())

    def test_cook_time(self):
        self.assertEqual(30, self.harvester_class.cook_time())

    def test_yields(self):
        self.assertEqual('4 personen', self.harvester_class.yields())

    def test_image(self):
        self.assertEqual('https://static.ah.nl/static/recepten/img_RAM_PRD143023_890x594_JPG.jpg', self.harvester_class.image())

    def test_ingredients(self):
        self.assertEqual(['3 rode uien', '4 tenen knoflook', '800 g flespompoenen', '300 g volkorenmacaroni', '1 el milde olijfolie', '200 g zuivelspread bieslook light', '½ tl gemalen nootmuskaat', '½ tl chilivlokken', '200 g Zaanse Hoeve geraspte kaas mild 30+'], self.harvester_class.ingredients())

    def test_instructions(self):
        self.assertEqual('Snipper de ui heel fijn en snijd de knoflook fijn. Schil de pompoen, halveer en verwijder de draderige binnenkant en pitten. Snijd in blokjes van ca. 1 cm. Breng 2 pannen ruim water aan de kook. Kook de macaroni in 8 min. beetgaar in de ene pan en kook de pompoen 8 min. in de andere pan.\nVerhit ondertussen de olie in een koekenpan, fruit de ui en de helft van de knoflook 5-8 min. op laag vuur. Verwarm de oven voor op 200 °C. Giet de macaroni en pompoen af en bewaar een kopje van het pompoenkookvocht. Pureer de pompoen en het kookvocht met de staafmixer en meng de zuivelspread, nootmuskaat en chilivlokken erdoor tot een gladde saus.\nMeng de macaroni en pompoen, de helft van de geraspte kaas en het gebakken knoflook-uimengsel. Schep in de ovenschaal. Meng de rest van de geraspte kaas met de rest van de knoflook. Verdeel over de schaal. Bak de mac and cheese ca. 25 min. tot goudgeel en knapperig.', self.harvester_class.instructions())

    def test_cuisine(self):
        self.assertEqual('amerikaans', self.harvester_class.cuisine())

    def test_category(self):
        self.assertEqual('hoofdgerecht', self.harvester_class.category())
