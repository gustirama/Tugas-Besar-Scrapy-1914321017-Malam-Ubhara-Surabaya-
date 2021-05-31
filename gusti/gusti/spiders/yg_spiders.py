import scrapy


class QuotesSpider(scrapy.Spider):
    name = "yg"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel/legend-of-swordsman/',
	    'https://www.worldnovel.online/novel/kiss-me-goodnight-mrs-ceo/',
	    'https://www.worldnovel.online/novel/star-odyssey/',
	    'https://www.worldnovel.online/novel/medical-master/',
	    'https://www.worldnovel.online/novel/soul-land-iv/',
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')