# Task2 :Write and Append Data to a File
# Problem Statement: Write a Python program that:
# 1.Takes user input and writes it to a file named output.txt.
# 2.Appends additional data to the same file.
# 3.Reads and displays the final content of the file.

InputWrite = input("Enter to write to the file: ")
with open('output.txt','w') as file:
    file.write(InputWrite +'\n')


InputAppend = input("Enter additional text to append: ")
with open('output.txt','a') as file:
    file.write(InputAppend + '\n')

print("Final content of output.txt:")

with open('output.txt','r') as file:
    ReadingFile = file.read()
    print(ReadingFile)
