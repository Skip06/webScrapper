import httpx
from loguru import logger
import asyncio

class Fetcher:
    async def getHtml(url: str):
        async with httpx.AsyncClient() as client:
            logger.info(f'fetching {url}')
            response = await client.get(url)
            html = response.text
            return html

