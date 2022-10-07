import asyncio
import time

async def now_working():
    print("now working")

async def main():
    await now_working()
    while True:
        await asyncio.sleep(5, result=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
