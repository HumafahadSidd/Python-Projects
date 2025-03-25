"""Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):"""

Anton=21
beth=Anton+6
chen=beth+20
ethan=chen
drew=chen+Anton

print(f"Anton is {Anton} years old.")
print(f"Beth is {beth} years old.")                 
print(f"Chen is {chen} years old.")
print(f"Drew is {drew} years old.")
print(f"Ethan is {ethan} years old.")

def age():
    Anton=21
    beth=Anton+6
    chen=beth+20
    ethan=chen
    drew=chen+Anton

    print(f"Anton is {Anton} years old.")
    print(f"Beth is {beth} years old.")
    print(f"Chen is {chen} years old.")
    print(f"Drew is {drew} years old.")
    print(f"Ethan is {ethan} years old.")

if __name__ == '__main__':
    age()



