# Example 1: Using a flag variable
# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
"""
In this program, we have checked if num is prime or not. Numbers less than or equal to 1 are not prime numbers. Hence, we only proceed if the num is greater than 1.

We check if num is exactly divisible by any number from 2 to num - 1. If we find a factor in that range, the number is not prime, so we set flag to True and break out of the loop.

Outside the loop, we check if flag is True or False.

If it is True, num is not a prime number.
If it is False, num is a prime number.
"""







# Example 2: Using a for...else statement
num = 407

# To take input from the user
#num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
"""
Here, we have used a for..else statement to check if num is prime.

It works on the logic that the else clause of the for loop runs if and only if we don't break out the for loop. 
That condition is met only when no factors are found, which means that the given number is prime.

So, in the else clause, we print that the number is prime.
"""
