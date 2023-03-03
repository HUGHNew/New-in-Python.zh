# [Python 3.7][Python3.7]

- `__future__.annotaions`
- `dataclass` 修饰器
- `breakpoint` 函数
- `async` `await` 在 3.7 成为保留字

## dataclass

默认生成:
- `__init__`
- `__eq__`
- `__repr__`
- `__hash__`

```python
from dataclasses import dataclass

@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

print(Rect(0,0,2,1))
```

## breakpoint

内置的断点函数 会调用 `sys.breakpoint` 然后启动 [pdb](https://docs.python.org/release/3.11.0/library/pdb.html#module-pdb)

[Python3.7]: https://docs.python.org/release/3.11.0/whatsnew/3.7.html#new-features