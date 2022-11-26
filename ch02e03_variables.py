# 2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Do not worry about error checking or bad user data.

# py ch02e03_variables.py

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
pay = float(hrs) * float(rate)
print('Pay:', pay)