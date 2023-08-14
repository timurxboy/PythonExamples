# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))





#Source Code: Without Using Temporary Variable
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)


"""
If the variables are both numbers, we can use arithmetic operations to do the same. 
It might not look intuitive at first sight. 
But if you think about it, it is pretty easy to figure it out. 
Here are a few examples
"""

#Addition and Subtraction
x = x + y
y = x - y
x = x - y

#Multiplication and Division
x = x * y
y = x / y
x = x / y

#XOR swap - This algorithm works for integers only
x = x ^ y
y = x ^ y
x = x ^ y
