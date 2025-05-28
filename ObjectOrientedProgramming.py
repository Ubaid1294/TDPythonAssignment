# Class
# Syntax
#       Class Classannme:
#           Statements
# Call the class


# 1:
class Car1:
    pass        # Placeholder which returns null
car = Car1()
print(car)

# 2:

class Car2:
    Color = "Black"

Car = Car2()
print(Car.Color)

# 3:
class Car3:
    color = "Black"
    Type = 'SUV'
Car = Car3()
print(Car.color.upper())



class Counting:
    n = 0
    def cnt(self):
        self.n  = self.n + 1
        print("Counted",self.n)
C = Counting()
C.cnt()
C.cnt()
C.cnt()


class Const_Dest:
    x = 0
    def __init__(self, Color, Type):
        self.Color = Color
        self.Type = Type
        print("Constructed")

    def __del__(self):
        print("Destructed")
CD = Const_Dest("Black", "SUV")
print(CD.Color)
print(CD.Type)

CD1 = Const_Dest("Red", "Sedan")
print(CD1.Color)
print(CD1.Type)


# def name(name):
#     print("Hi {}".format(name))
# n = name('Jen')
# print(n)

class greetings:
    x = 0
    Name = ""
    def __init__(self, Z):
        self.Name = Z
        print("Hi {}".format(self.Name))

class football_fans(greetings):
    points = 0
    def pts(self):
        print(self.Name,"Score")
n = greetings("Sam 1")
f = football_fans("Jim")
f.pts()




# Inheritance
print("\nSingle Level Inheritance\n")

class A:
    def state1(self):
        print("State 1 present in Class A")
    def state2(self):
        print("State 2 present in Class A")
    def state3(self):
        print("State 3 present in Class A")

class B(A):
    def state4(self):
        print("State 4 present in Class B")
    def state5(self):
        print("State 5 present in Class B")



a = A()
a.state1()
a.state2()

b = B()
b.state4()
b.state5()
b.state3()

print("\nMulti-level Inheritance \n")

class C(B):
    def state6(self):
        print("State 6 present in Class C")
    def state7(self):
        print("State 7 present in Class C")


c = C()
c.state6()
c.state7()

c.state4()
c.state1()

print("\nMultiple Level Inheritance\n")

class A:
    def state1(self):
        print("State 1 present in Class A")
    def state2(self):
        print("State 2 present in Class A")
    def state3(self):
        print("State 3 present in Class A")

class B:
    def state4(self):
        print("State 4 present in Class B")
    def state5(self):
        print("State 5 present in Class B")
class C(A,B):
    def state6(self):
        print("State 6 present in Class C")
    def state7(self):
        print("State 7 present in Class C")


a = A()
a.state1()

b = B()
b.state4()

c = C()
c.state6()
c.state1()
c.state4()


print("\nOperator Overloading \n")

class veg:
    def __init__(self, Carrot, Beans):
        self.Carrot = Carrot
        self.Beans = Beans

    def __add__(self, other):
        carrot = self.Carrot + other.Carrot
        beans = self.Beans + other.Beans
        return veg(carrot, beans)

V1 = veg(5,6)
V2 = veg(7,8)
V3 = V1+V2
print(V3.Carrot,V3.Beans)

print("\nData Hiding\n")

class simple:
    def __init__(self):
        self.__x = 10
        self.y = 20

    def __A1_(self):
        print("Apple")

    def _B1_(self):
        print("Banana")

S = simple()
print(S._simple__x)
print(S.y)

S._simple__A1_()

# print(dir(S))