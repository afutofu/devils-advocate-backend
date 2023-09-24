import scrapy
from ..items import DevilfruitscrapeItem
from random import randint
import re


class DevilFruitsSpider (scrapy.Spider):
    name = "devilfruits"

    start_urls = [
        "https://onepiece.fandom.com/wiki/Category:Devil_Fruits"
    ]

    def parse(self, response):

        collapsible_count = 1
        collapsible_max = 3

        for fruit_type_collapsible in response.css(".collapsible"):

            td_count = 1
            td_max = 2

            for fruit_group in fruit_type_collapsible.css(".cs+ td"):

                # fruit_count = 1
                # fruit_max = 2

                for next_fruit in fruit_group.css("span a"):
                    link = next_fruit.css("::attr(href)").get()

                    next_page = "https://onepiece.fandom.com" + link

                    yield response.follow(next_page, callback=self.scrape_fruit_info,
                                          cb_kwargs=dict(collapsible_count=collapsible_count))

                    # fruit_count += 1
                    # if fruit_count > fruit_max:
                    #     break

                td_count += 1
                if td_count > td_max:
                    break

            print(collapsible_count)

            collapsible_count += 1
            if collapsible_count > collapsible_max:
                break

    def scrape_fruit_info(self, response, collapsible_count):

        item = DevilfruitscrapeItem()

        name = response.css(".page-header__title::text").get()
        price = randint(500000, 5000000)
        imagelink = response.css(".pi-image-thumbnail::attr(src)").get()
        english_name = response.css(
            ".pi-item-spacing:nth-child(3) .pi-font::text").get()
        meaning = response.css(
            ".pi-border-color:nth-child(4) .pi-font::text").get()

        info = response.xpath(
            '//*[contains(concat(" ",normalize-space(@class)," ")," pi-layout-default ")]/following-sibling::*[1]/self::p//text()').extract()

        info = "".join(info)
        info = re.sub(r"\[\d+\]", "", info)

        if collapsible_count == 1:
            item['fruit_type'] = "Paramecia"
        elif collapsible_count == 2:
            item['fruit_type'] = "Zoan"
        elif collapsible_count == 3:
            item['fruit_type'] = "Logia"

        item['name'] = name
        item['price'] = price
        item['imagelink'] = imagelink
        item['english_name'] = english_name
        item['meaning'] = meaning
        item['info'] = info

        yield item
