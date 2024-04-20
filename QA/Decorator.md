# Decorator

> 装饰器本质上是一个高阶函数(high-level function)

## basis

比较完整的形式如下 装饰器函数是一个三层嵌套的函数(这时装饰器本身有参数)

```python
def log(*args, **kwargs):
  def decorator(func):
    def wrapper(*args, **kwargs):
      # do something
      return func(*args, **kwargs)
    return wrapper
  return decorator

# 使用装饰器
@log(...)
def your_func(*args, **kwargs):
  pass

# 不使用装饰器
def your_func(*args, **kwargs):
  pass

your_func = log()(your_func)
```

如果装饰器本身没有参数的话 可以简化如下(只有两层函数嵌套)

```python
def log(func):
  def wrapper(*args, **kwargs):
    # do something
    return func(*args, **kwargs)
  return wrapper

# 使用装饰器
@log
def your_func(*args, **kwargs):
  pass

# 不使用装饰器
def your_func(*args, **kwargs):
  pass

your_func = log()(your_func)
```

这样简单操作后 只有一个小问题

```python
print(your_func.__name__)
# wrapper
```
但我们更希望得到的是函数的原名 `your_func`

所以使用 `functools.wraps` 这个函数可以帮我们解决这个问题

```python
import functools
def log2unwrap(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    # do something
    return func(*args, **kwargs)
  return wrapper

@log2unwrap()
def your_func(*args, **kwargs):
  pass

print(your_func.__name__)
# your_func
```

另外一个问题就是装饰器嵌套时的顺序问题

```python
@log
@log2
def func():
  pass

# 可以看作如下形式
func = log(log2(func))
```

如这样的函数 距离函数定义最近的装饰器最早使用

## advanced

函数装饰器的基本使用就是这样 如果需要了解[类装饰器][dec-cls] 可以查看官方文档 或者等我后续有空再补充

> 其实原理差不多 就是定义类的`__init__`和`__call__`两个方法 另外注意一下 `func` 参数的位置以及需要添加 `self` 参数

[PEP0616]: https://peps.python.org/pep-0616/
[dec-cls]: https://pythonhowto.readthedocs.io/zh-cn/latest/decorator.html#decorator-class