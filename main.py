import asyncio
import json

from data_fetcher import DataFetcher


async def main():
    ids_to_fetch = range(1, 101) # Let's fetch the first 50 posts
    fetcher = DataFetcher(max_concurrent=5)
    accumulated_results = []
    try:
        print(f"Starting data fetch for {len(ids_to_fetch)} posts...")
        results = await fetcher.run(ids_to_fetch, accumulated_results)
        print("✅ Finished all requests successfully.")

    except (asyncio.CancelledError, KeyboardInterrupt):
        print(f"\n⚠️ Interrupted! Saving {len(accumulated_results)} posts...")
        # raise

    finally:
        with open("fetched_posts_log_new.log", "w") as log_file:
            json.dump(([r for r in accumulated_results if isinstance(r, dict)]), log_file)
        print("🧹 Cleaning up connections and exiting.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
