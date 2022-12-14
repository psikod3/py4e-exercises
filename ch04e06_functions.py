""" 4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should
be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
Put the logic to do the computation of pay in a function called computepay() and use the function to do the
computation. The function should return a value. You should use input to read a string and float() to convert the
string to a number. Do not worry about error checking the user input unless you want to - you can assume the user
types numbers properly. Do not name your variable sum or use the sum() function. """


# py ch04e06_functions.py

def computepay(h, r):
    if float(h) <= 40.0:
        p = float(h) * float(r)
        return p
    else:
        p = 40.0 * float(r) + (float(h) - 40.0) * float(r) * 1.5
        return p


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
pay = computepay(hrs, rate)
print("Pay", pay)
