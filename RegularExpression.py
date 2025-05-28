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

print("\n^ - Matches the beginning of the line\n")
string = 'It is a dog 566'
pattern = '^I'
print(re.findall(pattern,string))

print("\n$ - Matches the end of the line\n")
pattern = 'dog$'
print(re.findall(pattern,string))

print(". - Matches any character")
pattern = '^I....'
print(re.findall(pattern,string))

print("\n\d - Matches any digit\n")
pattern = '\d'
print(re.findall(pattern,string))

print("\n\D - Matches any non-digit\n")
pattern = '\D'
print(re.findall(pattern,string))

print("\n\s - Matches whitespaces\n")
pattern = '\s'
print(re.findall(pattern,string))

print("\n\S - Matches any non-whitespace\n")
pattern = '\S'
print(re.findall(pattern,string))

print("\n* - Repeats a character zero or more times\n")
String = "From bobby.mark@mail.com"
Pattern = 'ma*'
print(re.findall(Pattern,String))

print("\n+ - Repeats a character one or more times\n")
Pattern = 'ma+'
print(re.findall(Pattern,String))

print("\n( - Indicates where string extraction is to start\n"
      ") - Indicates where string extraction is to end\n")
Pattern = '^From (\S+@\S+)'
print(re.findall(Pattern,String))


print("\n? - Repeats a character one or more times\n")
Pattern = '^F.*?'
print(re.findall(Pattern,String))

print("[]/[aeiou] - matches a single character in the listed set")
String = 'Pythonn is a Programming Language 3.0'
Pattern = '[aeiou]'
print(re.findall(Pattern,String))

Pattern = '[^aeiou]'
print(re.findall(Pattern,String))

Pattern = '[a-zA-Z0-9]'
print(re.findall(Pattern,String))

Pattern = '[A-Z]'
print(re.findall(Pattern,String))

Pattern = 'Python{2}'
print(re.findall(Pattern,String))

String = 'From bobby.mark@mail.com'
Pattern = '@([^ ]*)'
print(re.findall(Pattern,String))

