# Python语法更新

> 异步相关内容后续再补充

根据 Python 官方文档进行 Python 新语法部分内容的翻译和代码示例补充 (从 3.6 版本开始)

目前参考文档 [Python 3.11.2][whatsnew]  时间 2023/2/24



该目录下各个文件为版本号 原网站都是 <https://docs.python.org/release/3.11.0/whatsnew/3.x.html>



[whatsnew]: https://docs.python.org/release/3.11.0/whatsnew/index.html

## QA

### Type Hint

Python 3.5 引入 `typing` 包来支持 type hint

Python 3.7 引入 `__future__.annotations` 来修正以前的问题
- 类型标注只能前置声明 (不能声明未定义类型)
- 类型标注降低效率

同时 给`typing`模块添加了解释器支持(PEP560)

Python 3.8 `typing` 添加
- `Literal` 指定返回几个字面值
- `Final`   指定该值不可变