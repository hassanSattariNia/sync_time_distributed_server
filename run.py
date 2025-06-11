
import logging
logging.basicConfig(level=logging.INFO)
import time
from datetime import datetime
import asyncio



logging.critical("Start Run ")

async def main():
    for i in range(30):
        time_stamp = time.time()
        logging.critical(f"TimeStamp:{time_stamp:.6f}")
        logging.critical(f"Time:{datetime.fromtimestamp(time_stamp).strftime('%M:%S')}")

if __name__ == "__main__":
    asyncio.run(main())