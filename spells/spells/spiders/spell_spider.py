from scrapy import Spider
from scrapy.selector import Selector
from spells.items import SpellItem

# [ [ coletar SGV


class StackSpider(Spider):
    name = "spell"
    allowed_domains = ["https://pf2srd.com.br"]
    with open("spells_link.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        spells = Selector(response).xpath('/html/body/div[1]/div/div/main/article')


        for spell in spells:
            item = SpellItem()
            item['title'] = spell.xpath('/html/body/div[1]/div/div/main/article/header/h1/text()').get()
            item['level'] = spell.xpath('/html/body/div[1]/div/div/main/article/header/span/text()').get()
            item['tradition'] = spell.xpath('//html/body/div[1]/div/div/main/article/section[2]/p/text()').getall()
            item['description'] = spell.xpath('/html/body/div[1]/div/div/main/article/section[3]/p/text()').get()
            item['details'] = spell.xpath('/html/body/div[1]/div/div/main/article/section[2]/div/p/text()').getall()
            item['tags'] = spell.xpath('/html/body/div[1]/div/div/main/article/section[1]/p/a/text()').getall()
            item['action'] = spell.xpath('/html/body/div[1]/div/div/main/article/section[2]/div[1]/p/svg').getall()
            yield item