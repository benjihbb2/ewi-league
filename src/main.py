'''
Combining operations
'''
from operations import summation, subtraction, multiplication, division

def perform_operation(num1, num2, operation):
    if operation == "add":
        result = summation(num1, num2)
    elif operation == "subtract":
        result = subtraction(num1, num2)
    else:
        raise ValueError("Invalid operation. Please choose 'add' or 'subtract'.")

    return result

def perform_mult_div(num1,num2,operation):
	if operation =="multiply":
		result == multiplication(num1,num2)
	elif operation == "divide":
		result = division(num1,num2)
	else:
		raise ValueError("Invalid operation. Please choose 'multiply' or 'divide'")
	return result
