# Tutedude Assignments

## Assignment 1

### Task 1: Perform Basic Mathematical Operations
Problem Statement:
```
1.Takes two numbers as input from the user.
2.Performs the basic mathematical operations on these two numbers:
    Addition,
    Subtraction,
    Multiplication,
    Division
3.  Displays the results of each operation on the screen
```

**Answer**
```
Step1: Start
Step2: Prompt the user to enter a FirstNumber
Step3: Prompt the user to enter the SecondNumber
Step4: Adding the two numbers which user has entered
Step5: Subtracting the same two numbers which user has entered
Step6: Multiplying the same two numbers which user has entered
Step7: Dividing the same two numbers which user has entered
Step8: End
```

### Task 2: Create a Personalized Greeting
```
Problem Statement: 
1.Takes a user's first name and last name as input.
2.Concatenates the first name and last name into a full name.
3.Prints a personalized greeting message using the full name
```

**Answer***
```
Step1: Start
Step2: Prompt message to the user to "Enter your first name and store it in a variable FirstName
Step3: Prompt message to the user to "Enter your last name: " LastName and store it in a variable LastName
Step4: Concatenate FirstName and LastName with the greeting message and prompt it.
Step5: End
```


## Assignment 2
### Task 1: Check if a Number is Even or Odd
```
Problem Statement: Check if a Number is Even or Odd
1.Takes an integer input from the user.
2.Checks whether the number is even or odd using an if-else
```

**Answer**
```
Step 1: Start  
Step 2: Prompt the user to enter a number  
Step 3: Store the number in a variable called Number  
Step 4: Check if Number modulo 2 equals 0  
    -->If yes, go to Step 5  
    -->If no, go to Step 6  
Step 5: Print that the number is even  
Step 6: Print that the number is odd  
Step 7: End
```

### Task 2: Check the Sum of 1-50 
```
Problem Statement:Sum of Integers from 1 to 50 Using a Loop
1.Uses a for loop to iterate over numbers from 1 to 50.
2.Calculates the sum of all integers in this range.
```

**Answer**
```
Step 1: Start  
Step 2: Initialize a variable Sum to 0  
Step 3: Repeat steps 4 and 5 for i = 1 to 51
Step 4: Add the current value of i to Sum  
Step 5: Increment i by 1  
Step 6: After the loop ends, print the value of Sum  
Step 7: End
```

## Assignment 3
### Task 1: Calculate factorial using function
```
Problem Statement: Write a Python program that:
1.Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.Returns the calculated factorial.
3.Calls the function with a sample number and prints the output.
```

**Answer**
```
Step 1: Start
Step 2: Read an integer N from the user
Step 3: Call the function Factorial(N)
Step 4: Inside Factorial(N), check if N is less than or equal to 1
Step 5: If yes, return 1 (base case)
Step 6: If no, return N * Factorial(N - 1) (recursive case)
Step 7: Receive the returned value from Factorial(N) and store it in Result
Step 8: Print "Factorial of N is: Result"
Step 9: End
```

### Task2: Using the Math Module for Calculations
```
Problem Statement: Write a Python program that:
1. Asks the user for a number as input.
2. Uses the math module to calculate the:
    - Square root of the number,
    - Natural logarithm(log base e) of the number,
    - Sine of the number( in radians)
3. Displays the calculated results.
```

**Answer**
```
Step 1: Start
Step 2: Import the math module
Step 3: Read an integer N from the user
Step 4: Check if N is less than 1
Step 5: If yes, print "Please enter a positive number"
Step 6: If no, calculate and print the square root of N using math.sqrt(N)
Step 7: Calculate and print the natural logarithm of N using math.log(N)
Step 8: Calculate and print the sine of N (in radians) using math.sin(N)
Step 9: End
```

## Assignment 4
### Task 1: Read a File and Handle Errors
```
Problem Statement:  Write a Python program that:
1.Opens and reads a text file named sample.txt.
2.Prints its content line by line.
3.Handles errors gracefully if the file does not exist.
```

**Answer**
```
Step 1: Start
Step 2: Use try block to attempt opening the sample.txt file.
Step 3: To display output with line numbers, initialize a variable to keep track of the line number count.
Step 4: Use for loop to read the file line by line and print each line along with its line number.
Step 5: If the file does not exist in the directory, handle the error using except block with FileNotFoundError, and display the message 'File not Found' on the console.
Step 7: End
```

### Task2: Write and Append Data to a File
```
Problem Statement: Write a Python program that:
1.Takes user input and writes it to a file named output.txt.
2.Appends additional data to the same file.
3.Reads and displays the final content of the file.
```

**Answer**
```
Step 1: Start
Step 2: Take input from the user to write into the file.
Step 3: Open the file in write mode (w) and write the entered content into the file.File closes automatically as I used open with() statement.
Step 4: Take another input from the user to append into the file.
Step 5: Open the file output.txt in append mode (a) and append the entered content into the file. File closes automatically as I used open with() statement.
Step 6: Print the 'Final Content of the output.txt' message.
Step 7: Open the file output.txt in read mode (r) and read the content of the file and display that content.File closes automatically as I used open with() statement.
Step 8: End
```

## Assignment 5
### Task 1: Create a Dictionary of Student Marks
```
Problem Statement: Write a Python program that:
1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.
```

**Answer**
```
Step 1 : Start
Step 2 : Create a dictionary of students that holds student name as keys and their marks as values.
Step 3 : Take the Students name from the user as input.
Step 4 : Search the marks of entered name from the dictionary and store their values into marks variable.
Step 6 : Use the if statement to check whether the entered name exists in the dictionary.If present then return the students name and their marks otherwise return the message 'Student not found'.
Step 7: End
```