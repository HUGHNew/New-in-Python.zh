a = 1
b = 3


def global_and_local():
    def l():
        a = 2
        print({k:v for k,v in locals().items()})
        def _d():pass
        b = 4
        print({k:v for k,v in locals().items()})

    print({k:v for k,v in globals().items() if not k.startswith("__")}) # ignore builtin variables
    # a=1, b=3, global_and_local=<function>

    l()
    # a=2
    # a=2, b=4
def global_and_nolocal():
    a = 2
    print("top func a:{}, id:{}".format(a, id(a)))
    def local_domain_a():
        global a
        print("global a:{}, id:{}".format(a, id(a)))
    def local_domain_b():
        def inner():
            nonlocal a
            print("nonlocal a:{}, id:{}".format(a, id(a)))
        inner()
    local_domain_a()
    local_domain_b()
# global_and_local()
print("global a:{}, id:{}".format(a, id(a)))
global_and_nolocal()

# vars
vars()['a'] = 2
print(a, id(a)==id(vars()['a']))