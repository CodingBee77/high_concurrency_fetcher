# ⚡🕸️ High concurrency fetcher
A mini, runnable script that fetches data from a public API (like JSONPlaceholder).

It's using:
- **asyncio** and **Semaphores** to limit concurrrency and don't get banned
- **httpx** library and async client for API calls
- custom **@retry decorator**
- **handle exceptions** gracefully with 'return_exceptions=True' flag -> gather won't "fail-fast." and instead, it returns a list where some items are the successful results
and others are the Exception objects themselves. You then just filter the list for errors!



