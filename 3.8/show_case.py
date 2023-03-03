def pep572():
    assert (a := (b := ( c:= 3 ))) == 3
    print(c)
    lst = [1,2,3]
    if (n := len(lst)) > 2: # 有点 Go 的味道
        print(f"lst len:{n}")

def _pos_only(a,b,c,/,*,d):
    print(a,b,c)
    print("d:",d)

def pep570():
    # _pos_only(1,2,3,4) # TypeError
    _pos_only(1,2,3,d=4)
    # _pos_only(1,2,c=3,d=4) # TypeError

def bpo_36817():
    # f-string 自描述
    prog = "Python"
    version = 1.1415
    print(f"{prog=} {version+2=:.2f}")
    print(f"{prog} {version+2:.2f}")

if __name__=="__main__":
    pep570()
    bpo_36817()