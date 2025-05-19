# IF statement
    ## IF (Expression);
    ##       Statement1
    ## Statement2

# a = 11
# b = 20
a = int(input('Enter a number: '))
if a>5:
    print("Greater than 5")
print("None")

# IF ELSE statement
    ## IF (Expression);
    ##       Statement1
    ## ELSE
    ##       Statement2
Marks = int(input('Enter a Marks: '))

if Marks >= 40:
    print("You have Passed!")
else:
    print("You have Failed!")


#Challange
Age = int(input('Enter Age: '))

if Age >= 18:
    print("You can vote.")
else:
    print("You can not vote.")


# ELIF statement
    ## if (Expression);
    ##       Statement1
    ## elif:
    ##       Statement2
    ## else:
    ##       Statement3

Operand_1 = int(input('Enter Operand 1: '))
Operand_2 = int(input('Enter Operand 2: '))
Operator = input('Enter Operator: (+,-,*,*)')

if Operator == '+':
    print(Operand_1 + Operand_2)
elif Operator == '-':
    print(Operand_1 - Operand_2)
elif Operator == '*':
    print(Operand_1 * Operand_2)
elif Operator == '/':
    print(Operand_1 / Operand_2)
else:
    print("Operator not recognized.")
print('Thank You!')



# range --- has three parameters start, end, steps

n = list(range(11))
print(n)
n = list(range(3,11))
print(n)

n = list(range(2,11,2))
print(n)


# for loop

l = ['Mike',10.2,1980]
for n in l:
    print(n)

x= 'apple'
for n in x:
    print(n)

for i in range(1,5):
    print("n")



# while loop
#  counter variable
# while test exp:
#   statement
#   inc+/dec-

counter = 1
while counter <= 5:
    print('apple')
    counter += 1


count = 0
while count <=10:
    print(count)
    count += 1

counter  = 1
while counter <= 5:
    print("Python")
    counter = counter + 1
