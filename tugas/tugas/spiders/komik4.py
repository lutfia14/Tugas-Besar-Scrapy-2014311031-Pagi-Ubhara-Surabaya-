import scrapy


class QuotesSpider(scrapy.Spider):
    name = "domain"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/almighty-sword-domain/chapter-1-little-sweeper/',
            'https://www.worldnovel.online/almighty-sword-domain/chapter-2-beat-him-to-death/',
            'https://www.worldnovel.online/almighty-sword-domain/chapter-3-vortex-dantian/',
            'https://www.worldnovel.online/almighty-sword-domain/chapter-4-battling-the-colossal-python-king/',
            'https://www.worldnovel.online/almighty-sword-domain/chapter-5-the-dao-of-talismans/',
            'https://www.worldnovel.online/almighty-sword-domain/chapter-6-conflict-arises-again/',
            'https://www.worldnovel.online/almighty-sword-domain/chapter-7-the-outer-court-rankings/',
            'https://www.worldnovel.online/almighty-sword-domain/chapter-8-life-and-death-arena/',
            'https://www.worldnovel.online/almighty-sword-domain/chapter-9-gamble/',
            'https://www.worldnovel.online/almighty-sword-domain/chapter-10-basic-sword-technique/',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }