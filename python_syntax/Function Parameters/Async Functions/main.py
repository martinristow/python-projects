import asyncio


async def prepare_coffee():
    print("The coffee making has started!")
    await asyncio.sleep(5)
    print("The coffee is brewed!")


async def make_sandwich():
    print("Making sandwich is starting!")
    await asyncio.sleep(8)
    print("The sandwich is made!")


async def tasks():
    coffee_task = asyncio.create_task(prepare_coffee())
    sandwich_task = asyncio.create_task(make_sandwich())

    await coffee_task
    await sandwich_task

asyncio.run(tasks())
