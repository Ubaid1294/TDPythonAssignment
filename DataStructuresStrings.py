# Dictionary  {'Key':Value}

My_Dict1 = {'Key1': 1,'Key2':'2','Key3':[33,445],'Key4':(2,4,5),"Key5":5}
print(My_Dict1['Key3'])


My_Dict2 = {1:'a',2:'b',3:'c',4:'d'}
print(My_Dict2[2])

Dictionary = {'A': 'Apple','B':'Banana','C':'Cat','D':'Dog','E':'Elephant'}
print(Dictionary)
Dictionary['F'] = 'Food'
print(Dictionary)
del Dictionary['A']
print(Dictionary)

print(Dictionary.keys())
print(Dictionary.values())
print(Dictionary.items())
print(Dictionary.get('A'))
print(Dictionary.get('B'))



#### LIST

a = 1
b = 2
c = 3
d = 4
print(c)

NumberList = [1,2,3,4,5]
print(NumberList[3])

ColorList = ['black','red','green','blue']
print(ColorList[2])

MixedList = [1,'Black', 4,{1:2},(3,2)]
print(MixedList[3])

blankList = []
print(blankList)


List1 = ['Mike',110.1,1987]
List2 = ['Pop',2]

print(List1 + List2)

A = ['Disco',10.3,4]
A[0] = 'Hardwork'
print(A)

N = [1,2,3,4,5]
print(N * 2)

Game = ['Football','Basketball','Chess']
print('Footbal' in Game)


List1 = ['Mike',110.1,1987]
List1.append('Hardwork')
print(List1)
List1.extend([10,23,'Hardwork'])
print(List1)

List1.remove(1987)
print(List1)

del List1[2:4]
print(List1)

List1.pop(2)
print(List1)

List1.insert(2,'Pop')
print(List1)

List2 = [10.1,1980, 12,8,9,345]
List2.sort()
print(List2)

List2.reverse()
print(List2)

print(List1)
print(List1.index('Hardwork'))

print(len(List1))

print(len(List2))


N = [10,20,30,40,50,60,70]
print(N[0:5])
print(N[2:6])
print(N[-2:])
print(N[4:])

print(N[0:5:2])



X = []

for i in range(11):
    z = i ** 2
    X.append(z)
print(X)

## USing List Comprehension
## [Expression for item in list]
X = [i ** 2 for i in range(11)]
print(X)


X = []
for i in range(11):
    if i % 2 == 0:
        Z = i ** 2
        X.append(Z)
print(X)

X = [i ** 2 for i in range(11)
     if i % 2 != 0]
print(X)



## Set
## Collection data type
## Unordered
## Unique elements
## {}

Set1 = {1,2,3,4,5,3}
print(Set1)
Set1.add(6)
print(Set1)

Set1.remove(5)
print(Set1)

print(4 in Set1)

Set2 = {7,8,3,4,5}
print(Set1 & Set2)  # Intersection
print(Set1 | Set2)  # Union
print(Set1 ^ Set2)  # Difference
print(Set1.union(Set2))
print(Set1.intersection(Set2))

print("Set1",Set1)
Set2 = {1,2,3}
print("Set2",Set2)
print(Set2.issubset(Set1)) # SubSet



# String Functions

A = 'AabiD'
print(A.capitalize())
print(A.upper())
print(A.lower())
print(A.title())

B = '543'

print(B.isalpha())
print(B.isdecimal())
print(B.isnumeric())
print(B.islower())
print(B.isupper())
print(B.isspace())


String = ' Mike is a good boy '

print(String.startswith('Mike'))
print(String.endswith('Good boy'))
print(String.replace('Mike','Nick'))
print(String.find('o'))
print(String.lstrip())
print(String.rstrip())
print(String.strip())
print(String.split())
print(String.split(','))
print(String.splitlines())
print(String.split('\n'))

Name = 'Mike'
Num = len(Name) * 3
print("Hello {}. your lucky number is {}.".format(Name,Num))


Example = 'format() method'
String = 'This is an example of {} on string.'.format(Example)
print(String)

FirstString = "Apple"
SecondString = "Ball"
ThirdString = 'Cat'
String = "{1} {0} {2}".format(FirstString,SecondString,ThirdString)
print(String)

Price = 150
WithTax = 150 + 50
print(Price, WithTax)
print("Price: Rs {:.1f} and with tax: Rs {:.1f}".format(Price, WithTax))



## Tuples

Tup1 = (1,2,3,4,5,3)
print(Tup1)
print(Tup1[3])
print(Tup1.count(3))

Tup1 = ('Mike', 10, 2.5)
Tup2 = ('pop',4)
print(Tup1 + Tup2)

## Tuples are immutable
Number = (10,45,345,1,2,3,4,5)
# Number[0] = 11
print(Number)
n1 = sorted(Number)
print(n1)
print(n1.index(4))
print(Number.index(3))