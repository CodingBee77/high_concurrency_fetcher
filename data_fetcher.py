import asyncio
from typing import Any

import httpx
from retry_decorator import async_retry


class DataFetcher:
    def __init__(self, max_concurrent=10):
        self.semaphore = asyncio.Semaphore(max_concurrent)

    @async_retry(max_tries=3, delay=0.5)
    async def fetch_post(self, client, post_id, shared_list):
        # The semaphore limits the number of concurrent requests run at once
        async with self.semaphore:
            url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
            response = await client.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            #Critical: Append to the shared list as soon as we get data !
            shared_list.append(data)
            return data

    async def run(self, post_ids, shared_list)-> tuple[BaseException | Any]:
        if shared_list is None:
            raise ValueError("shared_list must be provided and cannot be None.")

        async with httpx.AsyncClient() as client:
            tasks = [self.fetch_post(client, pid, shared_list) for pid in post_ids]

            # return exceptions=True prevents one failure from stopping the batch
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return results


