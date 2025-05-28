# Regular Expression
# Regex
# Need for strings
# Need to import re
# Used for validate user input

print("Regular Expression \n")

# 1: match()

print("Match function \n")
import re
pattern = 'apple'
if re.match(pattern,'apple'):
    print("True")
else:
    print("False")

print("\nFindAll Function \n")

pattern = 'app'
string = re.findall(pattern,'apple app and appricot')
print(string)

print("\nSearch Function \n")

pattern = 'apple'
string = re.search(pattern,'apple app and appricot',flags=0)
print(string.group())

print("\nSub Function \n")

pattern = 'dog'
string = 'It is a dog'
print(re.sub(pattern,'caty', string,count=1,flags=0))

print("\nCharacters and Character Sequence \n")