# 类型标注

Python 3.5 引入 `typing` 包来支持 type hint

Python 3.7 引入 `__future__.annotations` 来修正以前的问题
- 类型标注只能前置声明 (不能声明未定义类型)
- 类型标注降低效率

同时 给`typing`模块添加了解释器支持(PEP560)

Python 3.8 `typing` 添加
- `Literal` 指定返回几个字面值
- `Final`   指定该值不可变

Python 3.9 `__future__.annotations` 支持内置容器作为泛型来进行类型标注

Python 3.10 提供了 `typing.Union` 类型 和 `X|Y` 语法糖 并且补充了`isinstance` `issubclass` 对于 Union 的支持