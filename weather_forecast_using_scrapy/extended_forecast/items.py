# -*- coding: cp1252 -*-
# Author: Franklet Semilla
# Date: 8/14/2017

from scrapy.item import Item, Field

#defines the items or “containers” for the data that we plan to scrape
class ExtendedForecastItem(Item):
    period = Field()
    condition_long = Field()
    condition_short = Field()
    temperature = Field()
