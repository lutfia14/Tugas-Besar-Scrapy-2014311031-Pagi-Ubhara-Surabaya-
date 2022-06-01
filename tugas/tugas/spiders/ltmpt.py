import scrapy


class QuotesSpider(scrapy.Spider):
    name = "star"
    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/star-odyssey/chapter-1-l-u-yin/',
            'https://www.worldnovel.online/star-odyssey/chapter-2-camp-of-the-seven-sages/',
            'https://www.worldnovel.online/star-odyssey/chapter-3-arrival/',
            'https://www.worldnovel.online/star-odyssey/chapter-4-formcast-model/',
            'https://www.worldnovel.online/star-odyssey/chapter-5-cultivation/',
            'https://www.worldnovel.online/star-odyssey/chapter-6-the-die-and-the-cosmic-art/',
            'https://www.worldnovel.online/star-odyssey/chapter-7-within-the-city/',
            'https://www.worldnovel.online/star-odyssey/chapter-8-fire-crystals/',
            'https://www.worldnovel.online/star-odyssey/chapter-9-farsight/',
            'https://www.worldnovel.online/star-odyssey/chapter-10-cosmic-palm/',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }