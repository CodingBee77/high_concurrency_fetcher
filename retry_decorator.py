import asyncio
import time
from functools import wraps


def async_retry(max_tries=3, delay=1):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_tries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying {attempt} failed. {e}")
                    if attempt < max_tries - 1:
                        await asyncio.sleep(delay)
                    else:
                        print("Max retries reached. Raising exception.")
                        raise
        return wrapper
    return decorator