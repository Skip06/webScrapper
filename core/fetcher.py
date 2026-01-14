import httpx
from loguru import logger
import asyncio

class Fetcher:
    async def getHtml(self, url: str):
        async with httpx.AsyncClient() as client:
            logger.info(f'fetching {url}')
            response = await client.get(url)
            html = response.text
            return html

# in a "good" scraper, you don't want to just fetch one page. You want to fetch 1,000 pages.

#     Without an Object: Every time you call the function, your OS has to open a new socket, perform a TCP handshake, and negotiate TLS. This is slow.

#     With an Object: You can open the httpx.AsyncClient once inside the __init__ constructor and reuse that same connection for every request. This is called Connection Pooling, and it's how high-performance backend systems (like those you'll build in Go or Rust) actually work.
