import scrapy

class AchievementSpider(scrapy.Spider):
    name = 'achievements'
    start_urls = ['https://genshin-impact.fandom.com/wiki/Achievement']

    def start_requests(self):
        urls = [
            'https://genshin-impact.fandom.com/wiki/Achievement',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.css('table.wikitable.sortable').css('tbody').css('tr')
        for row in rows:
            try:
                yield {
                    'icon': row.css('tr').css('td').css('a')[0].attrib['href'],
                    'category': row.css('a::text').get(),
                    'link': row.css('tr').css('td').css('a')[1].attrib['href']
                }
            except:
                pass
            
