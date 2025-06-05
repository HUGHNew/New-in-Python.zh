# [Python 3.13][Python3.13]

Type Hint
- [PEP 696][PEP696]: 默认支持了三个类型参数(不需要 import 就能用了) `from typing import TypeVar, ParamSpec, TypeVarTuple`
- [PEP 702][PEP702]: `warning.deprecated` 能用了
- [PEP 705][PEP705]: `typing.ReadOnly` (相当于const) 可用于 `typing.TypedDict` 还可以跟 `Required/NotRequired` 之类的结合使用
- [PEP 742][PEP742]: `typing.TypeIs` (跟`typing.TypeGuard`类似) 用于type checker做类型细化(narrow)推断的 更高级的`isinstance`

Optimization:
- REPL 更好用了
- Traceback 更清晰了
- GIL 解锁 (experimental)
- JIT 编译器 (experimental) --experimental-jit-interpreter [PEP 744][PEP744]

Others
- `functools.partial` 会报 `FutureWarning` 在未来版本的逻辑可能会变化
- 支持了Android/iOS平台 (Android 原来也能用 aarch64 的)


### PEP696

看上去更像C++的模板了

```python
# T = TypeVar("T")
# Ts = TypeVarTuple("Ts")

def move_first_element_to_last(tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    return (*tup[1:], tup[0])
```

### PEP702

```python
from warnings import deprecated
from typing import overload

@deprecated("Use B instead")
class A:
    pass

@deprecated("Use g instead")
def f():
    pass

@overload
@deprecated("int support is deprecated")
def g(x: int) -> int: ...
@overload
def g(x: str) -> int: ...
```

### PEP742

用于细化类型 将一个不太确定的类型 推断为一个具体的类型 `TypeIs[T]`的值是个`bool`

一般使用如下

```python
def narrower(x: I) -> TypeIs[R]: ...

def func1(val: A):
    if narrower(val):
        assert_type(val, True_Type)
    else:
        assert_type(val, False_Type)
```

具体示例如下

```python
from typing import TypeIs, Literal

type Direction = Literal["N", "E", "S", "W"]

def is_direction(x: str) -> TypeIs[Direction]:
    return x in {"N", "E", "S", "W"}

def maybe_direction(x: str) -> None:
    if is_direction(x):
        print(f"{x} is a cardinal direction")
    else:
        print(f"{x} is not a cardinal direction")
```

[Python3.13]: https://docs.python.org/3.13/whatsnew/3.13.html
[PEP696]: https://peps.python.org/pep-0696/
[PEP702]: https://peps.python.org/pep-0702/
[PEP705]: https://peps.python.org/pep-0705/
[PEP742]: https://peps.python.org/pep-0742/
