# taking user input. Accepts numbers with decimals and negatives too.
# https://www.w3schools.com/python/python_numbers.asp
input1 = float(input("Enter the first number: "))
input2 = float(input("Enter the second number: "))
input3 = float(input("Enter the third number: "))

# https://www.w3schools.com/python/ref_func_max.asp
largest = max(input1, input2, input3)
print("The largest number is:", largest)

# trying to use if/else
if input3 > input2 and input3 > input1:
    print("The 3rd entry was the largest", input3)
else:
    if input2 > input3 and input2 > input1:
        print("The 2nd entry was the largest", input2)
    else: 
        print("The 1st entry was the largest", input1)