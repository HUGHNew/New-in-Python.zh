import asyncio, time

async def after(secs, todo):
    await asyncio.sleep(secs)
    todo()

def timer(func):
    async def wrapper():
        start = time.time()
        rel = await func()
        end = time.time()
        print(f'Time taken: {end - start} seconds')
        return rel
    return wrapper

@timer
async def coroutines_2():
    """Time taken: 0.701075553894043 seconds"""
    print('Hello ...')
    # asyncio.sleep(1)
    c1t, c2t = 0.2, 0.5
    con = after(c1t, lambda: print(f'after {c1t} second'))
    con2 = after(c2t, lambda: print(f'after {c2t} second'))
    assert asyncio.iscoroutine(con)
    await con
    await con2
    print('... World!')

@timer
async def tasks_2():
    """Time taken: 0.5008699893951416 seconds"""
    print('Hello ...')
    c1t, c2t = 0.2, 0.5
    task1 = asyncio.create_task(after(c1t, lambda: print(f'after {c1t} second')))
    task2 = asyncio.create_task(after(c2t, lambda: print(f'after {c2t} second')))
    await task1
    await task2
    print('... World!')

async def coro_runtime():
    async def ham(bf, af):
        print(bf)
        await asyncio.sleep(0.4)
        print(af)

    h = ham("enter", "quit")
    await asyncio.sleep(0.1)
    print("before await")
    await h
    print('-' * 10)
    task = asyncio.create_task(ham("enter", "quit"))
    await asyncio.sleep(0.1)
    print("before await")
    await task
"""output:
before await
enter
quit
----------
enter
before await
quit
"""

async def subproc():
    proc = await asyncio.create_subprocess_shell(
        'echo "Hello, World!"',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()
    print(f'[{proc.pid}] stdout: {stdout.decode()}')
    print(f'[{proc.pid}] stderr: {stderr.decode()}')

    proc = await asyncio.create_subprocess_exec(
        "/usr/bin/ls", '.'
    )

# asyncio.run(coroutines_2())
# asyncio.run(tasks_2())
# asyncio.run(coro_runtime())
@timer
async def runtime():
    async def ham(bf, af):
        print(bf)
        await asyncio.sleep(0.4)
        print(af)

    async def say(idx):
        print(f"say {idx}")
        await asyncio.sleep(1)
        print(f"done {idx}")

    s = asyncio.sleep(1)
    h = ham("enter", "quit")
    y = say(42)
    await asyncio.gather(s, h, y)
    # h = ham("enter", "quit")
    # print(h.cr_running)
    # await say(42)
    # print("before await")
    # await h
    # await asyncio.gather(ham("enter", "quit"), say(42))
    # await asyncio.gather(ham("enter", "quit"), asyncio.sleep(1))
    # await asyncio.gather(*[say(i) for i in range(5)])

async def sleeper():
    async def sync_sleeper(sec):
        time.sleep(sec)
        return sec

    async def async_sleeper(sec):
        await asyncio.sleep(sec)
        return sec

    @timer
    async def sync_sync():
        await asyncio.gather(sync_sleeper(1), sync_sleeper(1))

    @timer
    async def sync_async():
        await asyncio.gather(sync_sleeper(1), async_sleeper(1))

    @timer
    async def async_sync():
        await asyncio.gather(async_sleeper(1), sync_sleeper(1))

    @timer
    async def async_async():
        await asyncio.gather(async_sleeper(1), async_sleeper(1))

    await sync_sync()
    await sync_async()
    await async_sync()
    await async_async()

asyncio.run(sleeper())
# print(type(main), asyncio.iscoroutinefunction(main))

async def tg():
    async with asyncio.TaskGroup() as group:
        task1 = group.create_task(sleeper())
        task2 = group.create_task(runtime())
    print("Both tasks have completed now.")

def manual_start_async():
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(runtime())
    finally:
        loop.close()

# if __name__ == "__main__":
#     manual_start_async()