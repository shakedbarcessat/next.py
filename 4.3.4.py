def get_fibo():
    x=0
    y=1
    while True:
        yield x
        x_brfore=x
        x=x+y
        y=x_brfore


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))