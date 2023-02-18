def fibbonacci(limit):
    a, b = 0, 1

    while a < limit:
        yield a
        a, b = b, a + b
    

fib = fibbonacci(30)
for i in fib:
    print(i)


mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator():
    print(i)