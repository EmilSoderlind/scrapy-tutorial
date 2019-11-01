from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ElectronicsSpider(CrawlSpider):
    name = "electronics"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = [
        'https://en.wikipedia.org/wiki/Main_Page'
    ]

    rules = (
        Rule(LinkExtractor(allow=()),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
	print(response.css('a::text')[2].extract())
