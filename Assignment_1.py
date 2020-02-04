#!/usr/bin/env python
# coding: utf-8
# In this program the distance in kilometers will be stored in the variable (val_km)
# Then val_km will be multiplied by 0.6214 and the answer will be stored in a new variable (val_mi)
# At-last the complier will return the (val_mi) i.e the distance in miles in a print statement
val_km = float(input("Enter the distance in Koilometers : "))
val_mi = val_km * 0.6214
print("The distance in Miles is : " , val_mi)

# This is a function that holds 1 parameter
# Within the function there is a if-else statement
# In the if statement there is a for loop that divides the Parameter_number with every number between 2 and the Parameter_number
# And if the remainder is 0 i.e the condition within the for loop is True the print statement will be Executed "Not-Prime"
# Or else the "Yes-prime" print statement will be executed
def if_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"Sorry, It's not a prime number")
                break
        else:
            print(num,"Yes, it's a prime number")
if_prime(107)

#For this program we define a function with two parameters with which we will perform the arithmetic operations
#For addition we will store the sumation of our two arguments in a variable (add)
#For subtraction we will store the diminution of our two arguments in a variable (sub)
#For multiplication we will store the multiplication of our two arguments in a variable (multi)
#For division we will store the division of our two arguments in a variable (div)
#And lastly we will call all the variables in their respective print function
def mini_calc(num1 , num2):

    add = num1 + num2
    sub = num1 - num2
    multi = num1 * num2
    div = num1 / num2

    print("The addition of the 2 numbers is : " , add)
    print("The sutraction of the 2 numbers is : " , sub)
    print("The multiplication of the 2 numbers is : " , multi)
    print("The division of the 2 numbers is : " , div)


mini_calc(100 , 2)
