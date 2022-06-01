import scrapy


class QuotesSpider(scrapy.Spider):
    name = "ohmy"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-1/',
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-2/',
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-3/',
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-4/',
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-5/',
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-6/',
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-7/',
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-8/',
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-9/',
            'https://www.worldnovel.online/oh-my-god-earthlings-are-insane/chapter-10/',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }