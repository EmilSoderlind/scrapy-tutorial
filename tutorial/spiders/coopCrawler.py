from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class coopCrawler(CrawlSpider):
    name = "coop"
    #allowed_domains = ["en.wikipedia.org"]
    start_urls = [
        'https://www.coop.se/handla-online'
    ]

    rules = (
        Rule(LinkExtractor(allow=('/varor/')),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        product_name = response.css("h1.ItemInfo-heading::text").extract_first()

        if(product_name is None):
            return

        product_URL = response.url
        product_price_value = response.css("span span.ItemInfo-priceValue::text").extract_first().replace(":-","").replace(":",".")
        product_brand_name = response.css("span.ItemInfo-brand::text").extract_first().replace(".", "")
        product_description = response.css("div.u-paddingVsm div.u-textSmall span::text").extract_first()
        product_price_compare = response.css("div.u-flexGrow div.ItemInfo-description div::text").extract_first()
        product_image_url = "www." + response.css("div.ItemInfo-image img::attr(src)").extract_first()[2:]

        # Select field to parse quantity from
        product_quantity_1 = response.css("div.ItemInfo-description::text")[1].extract().strip().replace(".", "")
        product_quantity_2 = response.css("div.ItemInfo-description::text")[2].extract().strip().replace(".", "")

        if(product_quantity_1 == ""):
            product_quantity = product_quantity_2
        else:
            product_quantity = product_quantity_1

        product_category_1 = product_URL.split("/")[5]
        product_category_2 = product_URL.split("/")[6]
        product_category_3 = product_URL.split("/")[7]

        yield {
                'product_name': product_name,
                'product_price_value': product_price_value,
                'product_quantity': product_quantity,
                #'product_description': product_description,
                'product_brand_name': product_brand_name,
                'product_price_compare': product_price_compare,
                'product_image_url': product_image_url,
                'product_URL' : product_URL,
                'product_category_1' : product_category_1,
                'product_category_2' : product_category_2,
                'product_category_3' : product_category_3,
            }
