import asyncio
import datetime


async def func1(i):
    print(f'i am {i}')
    await asyncio.sleep(2)
    return i


async def func2():
    task = set()
    a = datetime.datetime.now()
    print(a)
    for i in range(25):
        print('len task', len(task))
        task.add(asyncio.create_task(func1(i)))
        if len(task) > 4:
            done, task = await asyncio.wait(task)
            for f in task:
                await f
    while task:
        done, task = await asyncio.wait(task)
        for f in task:
            await f
    print(datetime.datetime.now() - a)


asyncio.run(func2())
