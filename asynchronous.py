import asyncio

async def task1():
    print("send first email")
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print("first email reply")

async def task2():
    print("send second email")
    asyncio.create_task(task3())
    await asyncio.sleep(3)
    print("second email reply")

async def task3():
    print("send third email")
    await asyncio.sleep(1)
    print("third email reply")

asyncio.run(task1())