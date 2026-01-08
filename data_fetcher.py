import asyncio
import httpx
from retry_decorator import async_retry


class DataFetcher:
    def __init__(self, max_concurrent=10):
        self.semaphore = asyncio.Semaphore(max_concurrent)

    @async_retry(max_tries=3, delay=0.5)
    async def fetch_post(self, client, post_id):
        # The semaphore limits the number of concurrent requests run at once
        async with self.semaphore:
            url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
            response = await client.get(url, timeout=5)
            response.raise_for_status()
            return response.json()

    async def run(self, post_ids):
        async with httpx.AsyncClient() as client:
            tasks = [self.fetch_post(client, pid) for pid in post_ids]

            # return exceptions=True prevents one failure from stopping the batch
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return results


