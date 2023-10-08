# [Python 3.12][Python3.12]

- [PEP 701][PEP701]: f-string 大增强
- [PEP 684][PEP684]: GIL 解锁前奏 现在只有 C-API

Type Hint
- [PEP 695][PEP695]: 引入 `type` 语法
- [PEP 692][PEP692]: 使用 `TypedDict` 作为 `**kwargs` 的类型标注
- [PEP 698][PEP698]: 子类的 `override`


### PEP701

改变了解析逻辑 从原来的贪婪模型改成了非贪婪模型 感觉对于效率也没什么影响

```python
f"""{f'''{f'{f"{1+1}"}'}'''}""" == f"{f"{f"{f"{f"{f"{1+1}"}"}"}"}"}" # 支持同类型引号嵌套
```

### PEP695

主要的就是两个点
1. 扩充泛型类和泛型函数写法
2. 引入新的显式类型别名写法

```python
# 紧凑的显式泛型标注 原来需要写 T = TypeVar("T") (3.5 引入)
def max[T](args: Iterable[T]) -> T: ...

class list[T]:
    def __getitem__(self, index: int, /) -> T: ...

    def append(self, element: T) -> None: ...


Point2d = tuple[float, float] # 隐式写法
Point2d: TypeAlias = tuple[float, float] # 显式写法
type Point2d = tuple[float, float] # 新写法
```


### PEP692

```python
from typing import TypedDict, Unpack

class Movie(TypedDict):
  name: str
  year: int

def foo(**kwargs: Unpack[Movie]): ...
```

### PEP698

```python
from typing import override

class Base:
  def get_color(self) -> str:
    return "blue"

class GoodChild(Base):
  @override  # ok: overrides Base.get_color
  def get_color(self) -> str:
    return "yellow"

class BadChild(Base):
  @override  # type checker error: does not override Base.get_color
  def get_colour(self) -> str:
    return "red"
```

[Python3.12]: https://docs.python.org/3.12/whatsnew/3.12.html
[PEP701]: https://peps.python.org/pep-0701/
[PEP684]: https://peps.python.org/pep-0684/
[PEP695]: https://peps.python.org/pep-0695/
[PEP692]: https://peps.python.org/pep-0692/
[PEP698]: https://peps.python.org/pep-0698/