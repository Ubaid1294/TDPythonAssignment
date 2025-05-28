## Lambda functions or Anonymous functions
## Syntax --- lambda argument : Expression

Fun = lambda a : a+1
print(Fun(2))

Fun = lambda a,b : a+b
print(Fun(2,3))


## FILTER


def Even(a):
    return a%2==0

Number = list(range(1,11))
# print(Number)
print(list(filter(Even, Number)))
print(tuple(filter(Even, Number)))
print(set(filter(Even, Number)))

lam = set(filter(lambda a: a%2 ==0 , Number))
print(lam)


## MAP
Number = list(range(1,11))

def Square(a):
    return a ** 2

print(list(map(Square, Number)))
print(list(filter(Square, Number)))
print(list(map(lambda a: a ** 2 , Number)))


## Iterator and generator

## Iterator
Iteration = iter(list(range(1,11)))
print(Iteration)
print(Iteration.__next__())
print(Iteration.__next__())

## Generator

def fun():
    yield 1
    yield 2
    yield 3
Value = fun()
print(Value.__next__())

for i in Value:
    print(i)


def Square():
    n = 1
    while n<=5:
        Square = n ** 2
        yield Square
        n += 1

Value = Square()
for i in Value:
    print(i)
    
