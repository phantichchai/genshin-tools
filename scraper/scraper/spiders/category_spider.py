import scrapy
import json

class CategorySpider(scrapy.Spider):
    name = 'category'

    def __init__(self):
        self.start_urls = 'https://genshin-impact.fandom.com/'
        with open('achievements.json') as file:
            self.achievements = json.load(file)
    
    def start_requests(self):
        urls = []
        for achievement in self.achievements:
            urls.append(self.start_urls + achievement['link'])
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        rows = response.css('table.article-table.sortable').css('tbody').css('tr')
        category = response.css('h2.pi-item::text').get()
        for row in rows:
            try:
                yield {
                    'category': category,
                    'title': row.css('tr').css('td').css('a')[0].attrib['title'],
                    'link': row.css('tr').css('td').css('a')[0].attrib['href'],
                }
            except:
                pass