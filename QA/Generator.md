# Generator

[generator_code](../QA_Scripts/generator.py)

> `Generator` 是一个 `Iterator` 定义 `send`  
> `Iterator` 是一个 `Iterable` 定义 `__next__`  
> `Iterable` 定义 `__iter__` 方法

## annotation

一个标准的`Generator`标注是`Generator[YieldType, SendType, ReturnType]`


`for-loop` 只能从 `Generator` 中获取 `yield` 出的值 (当 `StopIteration` 时结束)

`Generator` 的返回值类需要通过 `StopIteration.value` 获取

基本使用如下

```python
def g() -> Generator[str, None, int]:
  for i in range(3):
    yield str(i**2)
  return -1

if  __name__ == "__main__":
  gen = g()
  # for v in gen: # 获取不了返回值
  #   print(v)
  try:
    while True:
      print(next(gen))
  except StopIteration as e:
    print(f"return value: {e.value}")

"""output:
0
1
4
return value: -1
"""
```

## send

如果不使用 `for-loop` `Generator` 需要 `send(None)` 来触发开始执行

然后 `Generator` 通过 `yield` 返回值之后 函数会在 `yield` 处暂停

`send` 的作用可以在 `yield` 处向函数传值 传值的类型标注在 `Generator` 第二个位置

> `send/yield` 都是交换执行权

> 简单可以理解为 `send` 的参数是最近一次 `yield` 调用的返回值 同时 `send` 的调用会触发 `Generator` 的执行 得到下一次 `yield` 的值来作为 `send` 的返回值 **这就可能引发 *`StopIteration`***

```python
if  __name__ == "__main__":
    def generator() -> Generator[int, int, str]:
        print("onStart")
        send_value = yield 0
        print(f"onSend: {send_value}")
        return "endup"
    
    def user():
        g = generator()
        print("beforeSendNone")
        yield_value = g.send(None)
        print(f"onYield: {yield_value}")
        try:
            print("beforeSend")
            g.send(42)
        except StopIteration as e:
            print(f"onReturn: {e.value}")
    
    user()
"""output:
beforeSendNone
onStart
onYield: 0
beforeSend
onSend: 42
onReturn: endup
"""
```

## yield from

`yield from` 用来在 `Generator` 中返回 `Generator` 的值 能把嵌套的结构序列化

```python
def g0():
    for i in range(3):
        print(f"g0[iter]: {i}")
        yield i**2

def g1():
    notify = yield "g1 start up"
    st = yield from g0()
    print(st)
    yield "g1 get over"

if __name__ == "__main__":
    for v in g1():
        print(f"main: {v}")

"""output:
main: g1 start up
g0[iter]: 0
main: 0
g0[iter]: 1
main: 1
g0[iter]: 2
main: 4
None
main: g1 get over
"""
```