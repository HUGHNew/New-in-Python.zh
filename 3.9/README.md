# [Python 3.9][Python3.9]

- [PEP 584][PEP584]: 新增字典合并和更新运算符(合并: `|`  更新:`|=`)
- [PEP 585][PEP585]: 标准容器泛型的类型标注
- [PEP 616][PEP616]: 更宽松的修饰器语法限制

## PEP584

内置的 `dict` 新增了 `|` `|=`作为合并和更新的运算符 是原有的 `{**d1, **d2}` `dict.update` 操作的语法糖

```python
old = {}
old.update({"k1":1}) # 这是一个语句
old |= {"k1":1} # 和上一行一样

{**old, **{"k1":1}} # 一个表达式
old | {"k1":1}
```

## PEP585

对于 `__future__.annotaions` 运行时保留泛型参数

```python
>>> list is list[str]
False
>>> list == list[str]
False
>>> list[str] == list[str]
True
>>> list[str] == list[int]
False
```

## PEP616

值得关注 后续补充一个修饰器专题

[Python3.9]: https://docs.python.org/release/3.11.0/whatsnew/3.9.html#new-features
[PEP584]: https://peps.python.org/pep-0584/
[PEP585]: https://peps.python.org/pep-0585/
[PEP616]: https://peps.python.org/pep-0616/