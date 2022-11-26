""" 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done'
is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number
catch it with a try/except and put out an appropriate message and ignore the number. """

# py ch05e02_loops.py

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    
    else:
        try:
            num = int(num)  # try "checks" if input is integer (would give error if you try to int('bob')
            
            if largest is None:  # can't compare numbers to None, so we need to assign 'starting number' to the variable
                largest = int(num) 
                continue  # so loop will prompt for new input
                
            elif smallest is None:
                smallest = int(num)
                continue
            
            elif int(num) > largest:
                largest = int(num)
                continue 
                
            elif int(num) < smallest :
                smallest = int(num)
                continue
                
        except :
            print("Invalid input")
            continue

print("Maximum is", largest)
print("Minimum is", smallest)