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

def g0():
    for i in range(3):
        print(f"g0[iter]: {i}")
        yield i**2

def g1():
    notify = yield "g1 start up"
    st = yield from g0()
    print(st)
    yield "g1 get over"

def echo_producer() -> Generator[str, str, str]:
    echo_text = yield "start"
    while echo_text:
        echo_text = yield echo_text
    return "stop"

def echo_consumer():
    echo = echo_producer()
    print(echo.send(None), "\n\n") # for start
    for i in range(10):
        print(echo.send(f"on {i}"))
    try:
        print(echo.send(""))
    except StopIteration as e:
        print(e.value) # return value

def yield_send():
    def generator() -> Generator[int, int, str]:
        print("onStart")
        send_value = yield 0
        print(f"onSend: {send_value}")
        return "endup"
    
    def user():
        g = generator()
        print("beforeSendNone")
        yield_value = g.send(None)
        print(f"onYield: {yield_value}")
        try:
            print("beforeSend")
            g.send(42)
        except StopIteration as e:
            print(f"onReturn: {e.value}")
    
    user()

if __name__ == "__main__":
    # yield_send()
    # echo_consumer()

    # gc_test()
    # gc = 
    for v in g1():
        print(f"main: {v}")
        # vc = gc.send("no")
        # print(f"main: {vc}")