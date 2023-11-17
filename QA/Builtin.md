# builtin

简单的代码示例见[此](../QA_Scripts/builtin.py)

builtin keyword
- `global`: 自模块域向内开始找标识符
- `nonlocal`: 从最近域向外开始找标识符

builtin function

- `divmod` -> 返回商和余数

get variables: 可以动态获取变量
- `globals`: 返回模块内的变量(Runtime)
- `locals`: 返回最近作用域内的变量(Runtime)
- `vars`: 相当于`locals`
- `vars(object)`: 相当于 `object.__dict__()`

attr operations
- `hasattr`
- `getattr`
- `setattr`
- `delattr`

