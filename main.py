from core.fetcher import Fetcher
from models.datamodels import Quotes
from scrapper.scrapper import parseQuotes
import asyncio

async def run():
    fetcher = Fetcher()
    html = await fetcher.getHtml('https://quotes.toscrape.com/')
    data = parseQuotes(html)

    for quote in data:
        print(f'{quote.author} says {quote.text}')

if __name__ == '__main__':
    asyncio.run(run())
