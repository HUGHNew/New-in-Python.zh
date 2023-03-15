# [Python 3.10][Python3.10]

- [PEP 634][PEP634]: 结构化模式匹配
- [bpo-12782](https://bugs.python.org/issue?@action=redirect&bpo=12782): 允许带括号的上下文管理器
- [PEP 604][PEP604]: 添加联合类型的新运算符 `X|Y`
- [PEP 612][PEP612]: 参数指定变量
- [PEP 613][PEP613]: 显式类型别名

### PEP634

[官方教程][PEP636]

也可以参考一下[知乎](https://zhuanlan.zhihu.com/p/358606875)

整体的功能性较强

### PEP604

新增 `typing.Union` 语法糖 `X|Y`

同时支持 `isinstance()` 和 `issubclass()`

```python
isinstance(1, int|str)
def doubleIt(x: int|str) -> Union[int, str]:
    return x + x
```

### PEP612

最初的Callable不便于添加装饰器

新增加了 `typing.ParamSpec` 和 `typing.Concatenate` 来支持表达返回类型与参数类型依赖的关系

```python
def callIt(callable: Callable[[], None]): pass # 3.5 的 Callable[[参数类型], 返回值类型]

```


### PEP613

```python
oistr = Union[int, str] # 3.5 支持的类型别名
istr: TypeAlias = int|str # 给类型别名添加显式类型
```


[Python3.10]: https://docs.python.org/release/3.11.0/whatsnew/3.10.html#new-features
[PEP634]: https://peps.python.org/pep-0634/
[PEP604]: https://peps.python.org/pep-0604/
[PEP612]: https://peps.python.org/pep-0612/
[PEP613]: https://peps.python.org/pep-0613/
[PEP636]: https://peps.python.org/pep-0636/