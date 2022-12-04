# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class SpellItem(Item):
    title = Field()
    level = Field()
    tradition = Field()
    execution_component = Field()
