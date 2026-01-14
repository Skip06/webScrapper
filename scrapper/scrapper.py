from selectolax.parser import HTMLParser
from models.datamodels import Quotes

def parseQuotes(html: str):
    tree = HTMLParser(html)
    quotes = []
    for node in tree.css('div.quote'):  # returns all <div class="quote">
        text = node.css_first('span.text').text()
        author = node.css_first('small.author').text()
        tags = [tag.text() for tag in node.css('div.tags a.tag')]

        quoteObj = Quotes(text=text, author=author, tags=tags)
        print(quoteObj)
        quotes.append(quoteObj)

    return quotes