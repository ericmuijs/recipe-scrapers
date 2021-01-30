from ._abstract import AbstractScraper
from ._utils import get_minutes


class AlbertHeijn(AbstractScraper):
    @classmethod
    def host(cls):
        return "ah.nl"
    
    def title(self):
        return self.soup.find('meta', property="twitter:title")['content']

    def total_time(self):
        return get_minutes(self.soup.find('div', class_ = "microdata").find('time', itemprop='totalTime')['datetime'])

    def yields(self):
        return self.soup.find('span', class_= "js-scale-servings scaler__label").text

    def image(self):
        return self.soup.find('meta', property="og:image")['content']

    def ingredients(self):
        return [span.text for span in self.soup.find('ul',class_="list shopping ingredient-selector-list").find_all('span',class_="label")]

    def instructions(self):
        return '\n'.join([instruction.text for instruction in self.soup.find('section',itemprop="recipeInstructions").find_all('li')])

    def cook_time(self):
        #<span><time itemprop="cookTime" datetime="PT30M"></time></span>

    
    def cuisine(self):
        return 

    # def ratings(self):
    #     return self.schema.ratings()

    # def nutrients(self):
    #     return self.schema.nutrients()


"""

<div class="microdata">
<span><time itemprop="totalTime" datetime="PT30M"></time></span>
<span><time itemprop="cookTime" datetime="PT30M"></time></span>
<span itemprop="recipeCuisine">hollands</span>
<span itemprop="recipeCategory">hoofdgerecht</span>
<span itemprop="description">Frisse appelstukjes en pittige oude kaas met komijn: topcombi!
</span>
<span itemprop="recipeYield">4 personen</span>
<div itemprop="aggregateRating" itemscope="" itemtype="http://schema.org/AggregateRating">
<span itemprop="ratingValue">4</span>
<span itemprop="reviewCount">169</span>
</div>
</div>

<section class="nutrition" itemprop="nutrition" itemscope="" itemtype="http://schema.org/NutritionInformation">
<h6>Voedingswaarden
<small>(per eenpersoonsportie)</small>
</h6>
<ul class="list solid">
<li class="odd">
energie <span itemprop="calories">825&nbsp;kcal</span>
</li>
<li class="even">
eiwit <span itemprop="proteinContent">30&nbsp;g</span>
</li>
<li class="odd">
koolhydraten <span itemprop="carbohydrateContent">72&nbsp;g</span>
</li>
<li class="even">
vet <span itemprop="fatContent">44&nbsp;g</span>
<br>waarvan verzadigd <span itemprop="saturatedFatContent">28&nbsp;g</span>
</li>
<li class="odd">
natrium <span itemprop="sodiumContent">705&nbsp;mg</span>
</li>
<li class="even">
vezels <span itemprop="fiberContent">9&nbsp;g</span>
</li>
</ul>
</section>

"""