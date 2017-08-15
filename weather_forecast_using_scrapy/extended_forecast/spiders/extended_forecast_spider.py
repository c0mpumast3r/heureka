# Author: Franklet Semilla
# Date: 8/14/2017

from scrapy import Spider
from scrapy.selector import Selector
from extended_forecast.items import ExtendedForecastItem


class ExtendedForecastSpider(Spider):
    name = "extended_forecast"
    allowed_domains = ["forecast.weather.gov"]
    start_urls = [ "http://forecast.weather.gov/MapClick.php?lat=40.7142&lon=-74.0059#.WZEO2lEjGUk", ]
    
    def parse(self, response):
        questions = Selector(response).xpath('//li[@class="forecast-tombstone"]/div')

        for question in questions:
            item = ExtendedForecastItem()
            item['period'] = ' '.join(question.xpath('p[@class="period-name"]/text()').extract())
            item['condition_long'] = ' '.join(question.xpath('p/img/@title').extract())
            item['condition_short'] = ' '.join(question.xpath('p[@class="short-desc"]/text() | p[@class="short-desc"]/br/text()').extract())
            item['temperature'] = ' '.join(question.xpath('p[@class="temp temp-low"]/text() | p[@class="temp temp-high"]/text()').extract())

            #Display to console, as required by this assessment exercise
            print "\n"
            print item['period']
            print "  Condition (short desc): " + item['condition_short']
            print "  Condition (long desc) : " + item['condition_long']
            print "  Temperature: " + item['temperature']
            print "\n" 

            #yield to return scraped data with minimal memory usage
            #this also complements saving of scraped data to a json file by executing for ex: "scrapy crawl extended_forecast -o items.json -t json" 
            yield item

            
