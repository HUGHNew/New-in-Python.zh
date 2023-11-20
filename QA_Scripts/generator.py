from typing import Generator

# def sample():
def sample() -> Generator[int, str, float]:
    for idx in range(5):
        get_send = yield idx
        print("ret",idx,"now", "get_send", get_send)
    return 42.0
    # yield 42

def gc_test():
    gc = sample()
    print(next(gc))
    rel = gc.send("hello")
    print("send",rel)
    for v in gc:
        print(v)
    
    # region attemp to get return value
    
    try:
        print(gc.send(None))
    except StopIteration as si:
        print(si) # empty

    try:
        print(next(gc))
    except StopIteration as si:
        print(si) # empty
    
    # endregion attemp to get return value

def g0():
    for i in range(3):
        yield i**2

def g1():
    notify = yield "g1 start up"
    st = yield from g0()
    print(st)
    yield "g1 get over"

if __name__ == "__main__":
    # gc_test()
    gc = g1()
    for v in gc:
        print(f"main: {v}")
        vc = gc.send("no")
        print(f"main: {vc}")