import scrapy


class QuotesSpider(scrapy.Spider):
    name = "yr"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/yr-id/chapter-1-a-different-6-p-m/',
            'https://www.worldnovel.online/yr-id/chapter-2-supernatural-encounter/',
            'https://www.worldnovel.online/yr-id/chapter-3-hells-dictum/',
            'https://www.worldnovel.online/yr-id/chapter-4-granny/',
            'https://www.worldnovel.online/yr-id/chapter-5-ghastly-mahjong/',
            'https://www.worldnovel.online/yr-id/chapter-6-the-yin-yang-road/',
            'https://www.worldnovel.online/yr-id/chapter-7-the-netherworld-odyssey/',
            'https://www.worldnovel.online/yr-id/chapter-8-king-yamas-seal/',
            'https://www.worldnovel.online/yr-id/chapter-9-ksitigarbhas-enlightenment/',
            'https://www.worldnovel.online/yr-id/chapter-10-rakshasa/',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }