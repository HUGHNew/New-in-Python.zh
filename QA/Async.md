# Async

> since Python 3.4

> Python 3.11 引入了很多管理(TaskGroup)和控制上(timeout/wait)上的功能

> 推荐阅读: <https://lulaoshi.info/python/asyncio/basics.html>

## [Hello,World!][intro]

最简单的一个异步代码如下 需要通过 `asyncio.run` 来启动异步函数

```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1) # <--- 此处异步等待 阻塞1秒
    print('... World!')

asyncio.run(main())
```

如果直接执行 `main()` 会得到一个 `UserWarning` 然后主线程结束 异步函数没有完全执行

> Python 3.11 引入 `Runner` 此时可以把 `asyncio.run` 看作一个全局在调用方法 `Runner.run`

```python
# 相当于如下代码
import asyncio

# 直接写法
asyncio.run(main())
# 等价写法
with asyncio.Runner() as runner:
    runner.run(main())
``` 

### event_loop

对于异步编程而言 基于协程的调度系统的核心是 `event_loop`

`Runner` 底层使用 `event_loop` 维系一个 `Task` 列表接收`await`信号来处理调度

如上代码可以实现如下

```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1) # <--- 此处异步等待 阻塞1秒
    print('... World!')

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
```

### waitables

`await` 只能在异步的上下文等待可等待的对象

三个可等待对象
- coroutine
- task
- future

```python
# coroutine
async def func(): # 标识为 async 的即为协程函数
  pass
coro = func() # 协程函数返回值为一个协程对象

assert asyncio.iscoroutinefunction(func)
assert asyncio.iscoroutine(coro)

# task
task1 = asyncio.create_task(func()) # task 需要手动创建 是被管理的单元 有自己的调用栈

# future 是底层基类
```

### exection

对于 coroutine 和 task 而言主要的区别在于执行时机
- coroutine 在创建后并不会执行 在 await 时开始执行
- task 创建时即执行

```python
async def coro_runtime():
    async def ham(bf, af):
        print(bf)
        await asyncio.sleep(0.4)
        print(af)

    h = ham("enter", "quit")
    print("before await")
    await h # <-- coroutine
    print('-' * 10)
    task = asyncio.create_task(ham("enter", "quit"))
    print("before await")
    await task # < -- task
"""output:
before await
enter
quit
----------
enter
before await
quit
"""
```

所以从这里的示例可以看出 如果只是单纯使用协程的话 是无法提升执行效率的 (相当于执行时只有一个 task 无法进行调度 约等于同步代码)

我们需要把 coroutine 显式或隐式包装为 task 来让 event_loop 自动调度执行

```python
# 使用 gather 隐式包装
await asyncio.gather(asyncio.sleep(1), asyncio.sleep(1))
# Time taken: 1.0017027854919434 seconds
```

> `asyncio.TaskGroup` 是 Python 3.11 引入的异步上下文管理器 可以节省几行 `await`

### interoperation

异步代码可以和同步代码一起玩 不过考虑到阻塞问题 把异步操作放在前面会更好

```python
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

    await sync_sync()    # 2.0006 s
    await sync_async()   # 2.0019 s
    await async_sync()   # 1.0007 s
    await async_async()  # 1.0017 s
```

## subprocess

涉及子进程的函数主要是两个
- `create_subprocess_shell` : 参数类似于调用 `os.system`
- `create_subprocess_exec` : 参数类似于调用 `exec`

整体使用与 `subprocess` 模块差不多


## logging

`asyncio` 应该如下获取

```python
logging.getLogger("asyncio").setLevel(logging.WARNING)
```

为防止阻塞 应该采用 [handler](https://docs.python.org/zh-cn/3/howto/logging-cookbook.html#blocking-handlers) 来处理


[intro]: https://docs.python.org/zh-cn/3/library/asyncio.html