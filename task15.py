from time import time
import asyncio
import os

import random


async def new_file(n):
    for i in range(n):
        k = 1
        filename = f'in_{k + i}.dat'
        with open(filename, 'w') as file:
            num1 = float(f'{random.randint(0, 10000)}'
                         f'.{random.randint(0, 1000)}')
            num2 = float(f'{random.randint(0, 10000)}'
                         f'.{random.randint(0, 1000)}')
            file.write(f'{random.randint(1, 3)}\n{num1} {num2}')
            print(f'{filename} - Сreated!\n')
        await read_file(n)


async def read_file(n):
    for i in range(n):
        k = 1
        filename = f'in_{k + i}.dat'
        try:
            with open(filename, 'r') as file:
                ax = file.read().split('\n')
                operation = ax[0]
                nums = ax[1].split(' ')
            what_to_write = f'fail - {filename}, ' \
                f' Operetion - {operation}\n' \
                f'Num - {nums[0]}, {nums[1]}'
            await write_to_file(filename, operation, nums, what_to_write)
        except FileNotFoundError:
            pass


async def write_to_file(filename, operation, nums, what_to_write):
    with open('output.dat', 'a') as out:
        if int(operation) == 1:
            res = f'Rez  - {float(nums[0]) + float(nums[1])}'
            out.write(f'{what_to_write}\n{res}')
        if int(operation) == 2:
            res = f'Rez - {float(nums[0]) * float(nums[1])}'
            out.write(f'{what_to_write}\n{res}')
        if int(operation) == 3:
            res = f'Rez - {(float(nums[0])**2) + (float(nums[1])**2)}'
            out.write(f'{what_to_write}\n{res}')
    path = os.path.join(os.path.abspath
                        (os.path.dirname(__file__)), f'{filename}')
    os.remove(path)


def main(n):
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(new_file(n)),
             ioloop.create_task(read_file(n))]
    wait_tasks = asyncio.gather(*tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()


if __name__ == '__main__':
    start = time()
    main(50)
    full_time = time() - start
    print(f'Итого времени: {full_time}')
