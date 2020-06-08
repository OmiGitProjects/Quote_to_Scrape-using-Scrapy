import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetoscrapeItem

class LoginForm(scrapy.Spider):

        name = 'loginQuotes'

        start_urls = [
                'http://quotes.toscrape.com/login',
        ]

        def parse(self, response):

                token = response.css('form input::attr(value)').extract()
                
                return FormRequest.from_response(response, formdata={
                        'csrf_token' : token,
                        'username' : 'Omi2407',
                        'password' : 'omi'
                }, callback=self.start_scraping)

        def start_scraping(self, response):
                open_in_browser(response)
                # title = response.css('title::text').extract()
                all_divs = response.css('div.quote')

                for items in all_divs:
                        title = items.css('span.text::text').extract()
                        author = items.css('.author::text').extract()
                        tags = items.css('.tag::text').extract()

                        quote = QuotetoscrapeItem()

                        quote['TitleQuote'] = title
                        quote['AuthorQuote'] = author
                        quote['TagsQuote'] = tags

                        # yield {'Title':title, 'Author':author, 'Tags':tags}
                        yield quote