import time

import asyncio

async def wash(basket):
    print(f'Washing Machine ({basket}): Put the coin')
    print(f'Washing Machine ({basket}): Start washing...')
    await asyncio.sleep(5)
    print(f'Washing Machine ({basket}): Finishd washing')
    return f'{basket} is completed'

async def main():
    asyn1 = asyncio.gather(wash("Basket A"), wash("Basket B"))
    print(asyn1)
    print(type(asyn1))
    task = asyn1
    print(task)
    print(type(task))
    result = await task
    print(result)

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')