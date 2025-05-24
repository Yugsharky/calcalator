
first_number = float(input( "Enter first number: "))
second_number = float(input ( "Enter second number:"))
operation = input ("Enter operation( +, -, *):")

if operation == "+":
    result =first_number + second_number
elif operation == "-": 
    result = first_number - second_number
elif operation== "*":
    result = first_number * second_number
elif operation =="/": 
    result = first_number / second_number
print ( "result:", result) 
