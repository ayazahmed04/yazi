# Scraper Engine.py
import asyncio
import aiohttp
from config.settings import USER_AGENTS, DEFAULT_HEADERS
from .parse import parse

class ScrapeEngine:
    def __init__(self, start_urls):
        self.start_urls = start_urls
        self.seen_urls = set() # Track seen urls to avoid duplicates

    async def fetch(self , session , url):
        headers = DEFAULT_HEADERS
        headers['User-Agent'] = USER_AGENTS[0] # Select a User Agent Rotated if needed
        async with session.get(url, headers = headers ) as response:
            return await response.text()

    async def crawl(self):
        """Crawls with URLS concurrently. """
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, url) for url in self.start_urls]
            pages = await asyncio.gather(*tasks)
            # Processes each pages (parse or further crawl)
            for page in pages:
                parse(pages)
