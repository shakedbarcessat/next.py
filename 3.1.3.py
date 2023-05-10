
from final_task2 import x

def StopIteration():
    y = [1, 2, 3]
    x = iter(y)
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())

def ZeroDivisionError():
    print(5/0)


def AssertionError():
    second = 0
    assert second != 0


def KeyError():
    dic={"shaked": 18}
    print(dic[3])


def SyntaxError():
    print(HelloWorld)


def IndentationError():
    x=3
        y=4

def TypeError():
    print(5+"hello")
