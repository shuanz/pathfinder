from scrapy import Spider
from scrapy.selector import Selector
from spells.items import SpellItem

# [ ] coletar todas as urls


class StackSpider(Spider):
    name = "spell"
    allowed_domains = ["https://pf2srd.com.br"]
    start_urls = [
        "https://pf2srd.com.br/magias/lanca-divina",
    ]

    def parse(self, response):
        spells = Selector(response).xpath('/html/body/div[1]/div/div/main/article/header/h1')


        for spell in spells:
            item = SpellItem()
            item['title'] = spell.xpath(
                '/html/body/div[1]/div/div/main/article/header/h1/text()').extract()[0]
            print("item")
            print(item)
            yield item