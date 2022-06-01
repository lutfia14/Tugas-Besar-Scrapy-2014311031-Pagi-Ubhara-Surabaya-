import scrapy


class QuotesSpider(scrapy.Spider):
    name = "theten"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/bota/chapter-1-the-ten-eggs-in-the-lifebound-space/',
            'https://www.worldnovel.online/bota/chapter-2-aeternal-infernaldownloading-phoenix/',
            'https://www.worldnovel.online/bota/chapter-3-if-you-meet-the-wrong-person-your-life-shall-be-ruined/',
            'https://www.worldnovel.online/bota/chapter-4-the-blazing-palm-that-sent-a-pig-up-the-tree/',
            'https://www.worldnovel.online/bota/chapter-5-destination-heavens-sanctum/',
            'https://www.worldnovel.online/bota/chapter-6-the-spirit-gem-gobbling-chick/',
            'https://www.worldnovel.online/bota/chapter-7-mysterious-black-arm/',
            'https://www.worldnovel.online/bota/chapter-8-the-star-of-zephyr-square/',
            'https://www.worldnovel.online/bota/chapter-9-twisting-a-knife-into-his-wound/',
            'https://www.worldnovel.online/bota/chapter-10-flamehaven-shall-tremble/',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }