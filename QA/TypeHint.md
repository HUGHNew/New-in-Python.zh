# 类型标注

Python 3.5 引入 `typing` 包来支持 type hint

此时已经引入了`TypeVar` `Generic`对于泛型标注的支持

Python 3.7 引入 `__future__.annotations` 来修正以前的问题
- 类型标注只能前置声明 (不能声明未定义类型)
- 类型标注降低效率
- 对于标准容器 可以直接使用带参数的类型标注 如`dict[str,int]`

同时 给`typing`模块添加了解释器支持(PEP560)


Python 3.8 `typing` 添加
- `Literal` 指定返回几个字面值
- `Final`   指定该值不可变

Python 3.9 `__future__.annotations` 支持运行时标准容器泛型参数 (对于3.7的增强)

Python 3.10
- 提供了 `typing.Union`(3.5 随  `typing` 引入) 类型的语法糖: `X|Y` 并且补充了`isinstance` `issubclass` 对于 Union 的支持
-  显式指定 `TypeAlias`


```python
oistr = Union[int, str] # 3.5 支持的类型别名
istr: TypeAlias = int|str # 给类型别名添加显式类型
```

Python 3.11

新增类型
- `Self`
- `LiteralString` 字符串常量

Python 3.12

新增
- 使用 `TypedDict` 作为 `**kwargs` 的类型标注
- 子类的 `override`
- 泛型的简写(比较像Kotlin的写法)

```python
# new generic syntax in Python
def max[T](args: Iterable[T]) -> T: ...

class list[T]:
    def __getitem__(self, index: int, /) -> T: ...

# type keyword
type Point2d = tuple[float, float] # 新写法

from typing import TypedDict, Unpack

class Movie(TypedDict):
  name: str
  year: int

# type annotations for kwargs
def foo(**kwargs: Unpack[Movie]): ...
```

目前新增的TypeHint趋向于复杂化 很多新特性并不通用