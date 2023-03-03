# [Python 3.6][Python3.6]

- [PEP 498][PEP498] [模板字符串 (f-string)](#pep498)
- [PEP 515][PEP515] [数值中可插入下划线](#pep515)
- [PEP 526][PEP526] [变量类型标注](#pep526)
- [PEP 525][PEP525] asynchronous generators.
- [PEP 530][PEP530] asynchronous comprehensions.

## PEP498

新增语法: `f"f-string"`

**f-string** 是 `str.format` 的语法糖 两者都支持嵌套 都是 前者更直观

```python
width, prec, value = 10,4,12.34567
assert "{} {:{}.{}}".format("results:", value, width, prec) == f"results: {value:{width}.{prec}}"
```

## PEP515

数值字面量数字间可以插入单下划线

另外还可以与 f-string 联动

```python
print(f"{1234:_} {0xfffffff:_x}")
# 1_234 fff_ffff
# 十进制每三位隔开
# 2/8/16 进制每四位隔开
```

## PEP526

Python 3.5 引入的 typing 包来支持 type hint
- 函数的类型
- type alias

Python 3.6 补充支持了变量的类型标注

```python
unbound_value: str
# 赋值前使用会 raise UnboundLocalError
# 相当于 C 的裸指针
unbound_value = "" # 可以正常使用
```

## PEP525



## PEP530




[Python3.6]: https://docs.python.org/release/3.11.0/whatsnew/3.6.html#new-features
[PEP498]: https://docs.python.org/release/3.11.0/whatsnew/3.6.html#whatsnew36-pep498
[PEP515]: https://docs.python.org/release/3.11.0/whatsnew/3.6.html#whatsnew36-pep515
[PEP526]: https://docs.python.org/release/3.11.0/whatsnew/3.6.html#whatsnew36-pep526
[PEP525]: https://docs.python.org/release/3.11.0/whatsnew/3.6.html#whatsnew36-pep525
[PEP530]: https://docs.python.org/release/3.11.0/whatsnew/3.6.html#whatsnew36-pep530