input_equation = input("Enter equation here: ")

try:
    result = eval(input_equation)
    print(result)
except ZeroDivisionError:
    print("Dividing by zero is not definied")

except SyntaxError:
    print("Not the correct Syntax")

except Exception as e:
    print(f"Error: {e}")
