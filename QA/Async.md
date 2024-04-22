# Async

> since Python 3.4

> Python 3.11 引入了很多管理(TaskGroup)和控制上(timeout/wait)上的功能 <但目前以3.10的标准来看>

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
task1 = asyncio.create_task(func()) # task 需要手动创建

# future 比较底层
```

### exection

对于 coroutine 和 task 而言主要的区别在于
- 执行时机
- 并行程

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

> `asyncio.TaskGroup` 是 Python 3.11 引入的异步上下文管理器

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