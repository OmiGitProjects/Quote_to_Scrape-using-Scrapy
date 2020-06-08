# Step 1: Get HTML
import scrapy
from ..items import QuotetoscrapeItem

class ScrapyWeb(scrapy.Spider):
        name = 'Quotes'

        start_urls = [
                'http://quotes.toscrape.com/',
        ]

        def parse(self, response):

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

                # next_page = response.css('li.next a::attr(href)').get()
                # if next_page is not None:
                #         yield response.follow(next_page, callback=self.parse)