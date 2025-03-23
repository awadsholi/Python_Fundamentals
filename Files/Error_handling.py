from typing import Union

#Try-Except Blocks
try:
    num = int(input("Entar a number: "))
    result = 10 / num

except ZeroDivisionError: #Handling when user enters 0
    print("Zero division Error")

except ValueError: # ValueError when user enters a non-numeric value
    print("Error: Invalid Input")

except Exception as e:# to catch another exceptions (General)
    print(f"unexpected Error :{e}")

# Finally and else Blocks:

try:
    num = int(input("Enter Another Number: "))
    result = 30 / num

except ZeroDivisionError: #Runs if there is an error caught
    print("Zero Division Error")

else: #Runs if only no exceptions
    print(f"Done the result is : {result}")

finally: # Always runs
    print("Completed")

#Custom Class Exception
class NegativeNumberError(Exception): #Custom class for Negative value exception
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Invalid")
    return num ** 0.5

try:
    print(square_root((-9)))
except NegativeNumberError as e:
    print(f"Caught an error: {e}")



#Raising Exception
def withdraw(balance,amount):
    if amount > balance:
        raise ValueError("Invalid amount input") # to trigger ValueError
    return  balance - amount


#Type Annotation For function that may Raise Exceptions

try:
    new_balance = withdraw(100 , 150)
except ValueError as e:
    print(f"Error {e}")

def divide(a,b) -> Union[float,None]: #To return float or None both is correct equivalent with Union[X,None]
    try:
        return a / b #is correct
    except ZeroDivisionError:
        print("Not Allowed")
        return None #if there is an exception

