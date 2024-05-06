import asyncio

async def fetch_data():
    await asyncio.sleep(7)
    print({"data": 100})

async def countdown():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)


async def main():
    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(countdown())

    # await x
    await y

asyncio.run(main())

