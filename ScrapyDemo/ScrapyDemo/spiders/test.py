from scrapy.selector import Selector
from scrapy.http import HtmlResponse
body = '<html><body><span>good</span></body></html>'
response = HtmlResponse(url='http://example.com', body=body)
a = response.selector.xpath('//span/text()').extract()
print(a)