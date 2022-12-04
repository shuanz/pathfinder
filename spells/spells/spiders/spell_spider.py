from scrapy import Spider
from scrapy.selector import Selector
from spells.items import SpellItem

# [ ] coletar tags


class StackSpider(Spider):
    name = "spell"
    allowed_domains = ["https://pf2srd.com.br"]
    with open("spells_link.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        spells = Selector(response).xpath('/html/body/div[1]/div/div/main/article')


        for spell in spells:
            item = SpellItem()
            item['title'] = spell.xpath('/html/body/div[1]/div/div/main/article/header/h1/text()').extract()[0]
            item['level'] = spell.xpath('/html/body/div[1]/div/div/main/article/header/span/text()').extract()[0]
            item['tradition'] = spell.xpath('/html/body/div[1]/div/div/main/article/section[2]/p/a/text()').extract()[0]            
            item['execution_component'] = spell.xpath('/html/body/div[1]/div/div/main/article/section[2]/div[1]/ps/text()').extract()[0] 
            print(item)
            yield item

            