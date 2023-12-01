# [context][2]

## context-manager

```python
class WithBlock:
    def __enter__(self,) -> str: # context you want
        return "hello,world"
    def __exit__(self, exc_type:type[BaseException], exc_value:BaseException, tracebackb) -> int:
        return True # handle exceptions in with-block
```

对于资源管理器而言 需要实现的两个方法分别是
- `__enter__`: 返回需要的资源
- `__exit__`: 处理资源的回收 (返回值为 `True` 可以阻止异常的传播)

## [with][1]

[语法定义][3]

```python
with EXPRESSION as TARGET:
    SUITE

# equivalent as following

manager = (EXPRESSION)
enter = type(manager).__enter__
exit = type(manager).__exit__
value = enter(manager)
hit_except = False

try:
    TARGET = value
    SUITE
except:
    hit_except = True
    if not exit(manager, *sys.exc_info()):
        raise
finally:
    if not hit_except:
        exit(manager, None, None, None)
```

## contextlib

该库是 `with` 语法的协助工具 帮助定义上下文管理器

主要函数为 `contextlib.contextmanager` 该装饰器简化了上下文管理器的定义 (**async** 相关的函数以`a`开头)

### contextmanager

```python
@contextmanager
def managed_resource():
    try:
        yield "需要管理的资源"
        # 这行以上的内容相当于 __enter__ 函数
    finally:
        # finally 块内容相当于 __exit__
        pass # 释放资源
```
在实际的代码执行逻辑上等价于
```python
with managed_resource():
  BLOCK

"""
1. managed_resource 在 yield 之前的代码
2. BLOCK 代码
3. yield 与 finally 之间的代码
4. finally 部分的代码
"""
```

### closing

另外一个常用函数是 `closing` 其实现相当于

```python
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
```

但是 `open` 函数不需要额外调用 `closing` 因为其基类的 [`__exit__`][4] 调用了 `close`

```c
static PyObject *
iobase_exit(PyObject *self, PyObject *args)
{
    return PyObject_CallMethodNoArgs(self, &_Py_ID(close));
}
```

[1]: https://docs.python.org/zh-cn/3/reference/datamodel.html#context-managers
[2]: https://docs.python.org/3/library/contextlib.html
[3]: https://docs.python.org/zh-cn/3/reference/compound_stmts.html#with
[4]: https://github.com/python/cpython/blob/a65a3d4806a4087f229b5ab6ab28d3e0b0a2d840/Modules/_io/iobase.c#L499C1-L503C2