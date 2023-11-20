# Generator

[generator_code](../QA_Scripts/generator.py)

> `Generator` 是一个 `Iterator` 定义 `send`  
> `Iterator` 是一个 `Iterable` 定义 `__next__`  
> `Iterable` 定义 `__iter__` 方法

## annotation

一个标准的`Generator`标注是`Generator[YieldType, SendType, ReturnType]`


只能从 `Generator` 中获取 `yield` 出的值 (Python 3.10+)

## send

`Generator` 通过 `yield` 返回值之后 函数会在 `yield` 处暂停

`send` 的作用可以在 `yield` 处向函数传值 传值的类型标注在 `Generator` 第二个位置

> 简单可以理解为 `send` 的参数是最近一次 `yield` 调用的返回值 同时 `send` 的调用会触发 `Generator` 的执行 得到下一次 `yield` 的值来作为 `send` 的返回值 **这就可能引发 *`StopIteration`***

```python
# in generator
get_send = yield value

# using generator
next_yield = generator.send("value for last yield")
```

## yield from

`yield from` 用来在 `Generator` 中返回 `Generator` 的值

```python
def g0():
  for i in range(3):
    yield i**2

def g1():
  notify = yield "g1 start up"
  st = yield from g0()
  print(st)
  yield "g1 get over"
```