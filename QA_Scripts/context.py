from contextlib import contextmanager, closing
class Enter:
    def __enter__(self,) -> str:
        print("enter")
        return "hello,world"
    def __exit__(self, a:type[BaseException], b:BaseException, c) -> str:
        print("exit")
        return True

@contextmanager
def managed_resource():
    resource = 42
    try:
        print("get your resource")
        yield resource # equivalent __enter__().return
        print("postprocess")
        # 这行以上的内容相当于 __enter__ 函数
        # yield resource # only yield once is allowed here 
    finally:
        # finally 块内容相当于 __exit__
        print("exit block")

# with managed_resource() as mr:
#     print(f"managing:{mr}")

with closing(open("./QA_Scripts/builtin.py")) as co:
    print(co.closed)
    co.close()
print(co.closed)

with open("./QA_Scripts/builtin.py") as co:
    print(co.closed)
print(co.closed)

# with Enter() as e:
#     print(e, type(e))
#     raise TypeError



