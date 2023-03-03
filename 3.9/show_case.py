def pep584():
    d1 = {
        "k1": 2,
        "k2": 4,
        "k3": 5
    }
    d2 = {
        "k1": 20,
        "k2": 40,
        "k4": 7
    }
    assert d1|d2 != d2|d1
    assert d1|d2 == {**d1, **d2}
    assert d2|d1 == {**d2, **d1}
    d3 = d1.copy()
    d1.update(d2)
    d3|=d2
    assert d3 == d1
    print(d3)

if __name__=="__main__":
    pep584()
