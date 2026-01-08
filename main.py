import asyncio
import json

from data_fetcher import DataFetcher


async def main():
    ids_to_fetch = range(1, 51) # Lets fetch the first 50 posts
    fetcher = DataFetcher(max_concurrent=5)

    try:
        print(f"Starting data fetch for {len(ids_to_fetch)} posts...")
        results = await fetcher.run(ids_to_fetch)

        # If we finish the whole process without interruption
        with open("fetched_posts_log.txt", "w") as log_file:
            json.dump(([r for r in results if isinstance(r, dict)]), log_file)

    except KeyboardInterrupt:
        print("\n⚠️ Interrupted! Saving progress...")
        # In a real app, you'd access the 'results' gathered so far
        # and write them to a database or file before exiting.

    finally:
        print("🧹 Cleaning up connections and exiting.")


if __name__ == "__main__":
    # We catch KeyboardInterrupt here because asyncio.run()
    # propagates it up from the event loop.
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
