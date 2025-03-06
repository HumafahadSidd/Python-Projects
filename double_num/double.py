"""Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4 8 16 32 64 128"""
#solution:
num = int(input("Enter a number: "))
print(num)
curr_num = num * 2
while True:
    if curr_num <= 100:
     print(f'The {curr_num} is the double of input number that was {num}')
    else:
       print("The result value of given number is greater than 100.so i cant print the value")
    break
    
