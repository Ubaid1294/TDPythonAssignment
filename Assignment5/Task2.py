# Task 2: Demonstrate List Slicing
# Problem Statement: Write a Python program that:
# 1. Creates a list of numbers from 1 to 10.
# 2. Extracts the first five elements from the list.
# 3. Reverses these extracted elements.
# 4. Prints both the extracted list and the reversed list


# OriginalList = [1,2,3,4,5,6,7,8,9,10]
OriginalList = list(range(1,11))
print("Original list: {}".format(OriginalList))
ExtractedList = OriginalList[:6]
print("Extracted list: {}".format(ExtractedList))
ExtractedList.reverse()
print("Reversed list: {}".format(ExtractedList))
