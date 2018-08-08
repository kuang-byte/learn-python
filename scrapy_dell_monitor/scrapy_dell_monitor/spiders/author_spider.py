import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com']

    def start_requests(self):
        url = 'http://quotes.toscrape.com'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for href in response.css(".author + a::attr(href)"):
            self.logger.info("href %s" % href)
            yield response.follow(href, self.parse_author)

        for href in response.css("li.next a::attr(href)"):
            self.logger.info("href %s" % href)
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthday': extract_with_css('.author-born-date'),
            'bio': extract_with_css('div.author-description')
        }