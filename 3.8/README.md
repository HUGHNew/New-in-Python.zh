# [Python 3.8][Python3.8]

- [PEP 572][PEP572]: [赋值表达式](#pep572)
- [PEP 570][PEP570]: [限定只能使用位置参数](#pep570)

## pep572

```python
# 一个新的赋值符号 := (walrus)
(result := 42) # 该表达式的值为 42
result = 42 # 原始的赋值语句是一个语句
```

## pep570

新增参数语法(`/`)来支持限定前面的参数只能使用位置参数

```python
def _pos_only(a,b,c,/,d):
    pass
_pos_only(1,2,c=3,d=4)
# TypeError: _pos_only() got some positional-only arguments passed as keyword arguments: 'c'
```

使用上与`*`相同 不同作用方向不一样 这里是前向指定

## bpo-36817

f-string 引入了一个新的符号 `=`

`f"{expr=}"` 相等于 `f"expr={expr}"`

```python
prog = "Python"
version = 1.1415
print(f"{prog=} {version+2=:.2f}")
# prog='Python' version+2=3.14
```

[Python3.8]: https://docs.python.org/release/3.11.0/whatsnew/3.8.html#new-features
[PEP572]: https://peps.python.org/pep-0572/
[PEP570]: https://peps.python.org/pep-0570/