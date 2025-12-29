import time
from functools import wraps


def retry(max_tries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retrying {attempt} failed. {e}")
                    if attempt < max_tries - 1:
                        time.sleep(delay)
                        continue
                    else:
                        print("Max retries reached. Raising exception.")
                        raise
        return wrapper
    return decorator