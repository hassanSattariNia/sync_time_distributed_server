
import logging
logging.basicConfig(level=logging.INFO)
import time
import asyncio



logging.critical("Start Run ")

async def main():
    for i in range(30):
        logging.critical(f"current time is {time.perf_counter()}")
        await asyncio.sleep(1.5)


if __name__ == "__main__":
    asyncio.run(main())