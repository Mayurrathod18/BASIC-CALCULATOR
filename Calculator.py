function = input("What do you want to do (Addition, Subtraction, Multiplication or Dividion)? ")
numbers = list(map(float, input("Please enter your numbers here (comma separated, like 10,20,30): ").strip("[]").split(",")))

#ADDITION
def my_sum(*numbers):
    return sum(numbers)
    
#SUBTRACTION
def my_subs(*numbers):
    result1 = numbers[0]
    for nums in numbers[1:]:
        result1 -= nums
    return result1

#MULTIPLICATION
def my_multip(*numbers):
    result3 = numbers[0]
    for nums in numbers[1:]:
        result3 *= nums
    return result3

#DIVISION
def my_divs(*numbers):
    result5 = numbers[0]
    if result5 == 0:
        return 'invalid'
    for nums in numbers[1:]:
        if nums == 0:
            return 'Invalid'
        result5 /= nums
    return result5        
        
if function.lower() == "addition":
    result = my_sum(*numbers)
    print(f"Your answer is: {result}")

elif function.lower() == 'subtraction':
     result2 = my_subs(*numbers)
     print(f"Your answer is: {result2}")
    
elif function.lower() == 'multiplication':
     result4 = my_multip(*numbers)
     print(f"Your answer is: {result4}")

elif function.lower() == 'division':
     result2 = my_divs(*numbers)
     print(f"Your answer is: {result2}") 
else:
    print('Try again!')