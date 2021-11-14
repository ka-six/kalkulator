import sys
import logging
logging.basicConfig(level=logging.DEBUG)

operator = input("Select an operator, using number: 1 Add, 2 Subtract, 3 Multiply, 4 Divide:")

if operator != "1" and operator != "2" and operator != "3" and operator != "4":
    print("Only select the number from 1 to 4!")
    exit(1)

operations = {
    "1":"Adding",
    "2":"Subtracting",
    "3":"Multiplying",
    "4":"Dividing"
}

a = input("Give the first number:")
b = input("Give the second number:")

number_a = float(a)
number_b = float(b)
#czy tutaj użyć float czy int czy może jeszcze coś innego?

logging.debug(f"{operations[operator]} {number_a} and {number_b}")

def kalkulator(number_a, number_b):
    if operator == "1":
        c = number_a + number_b
        return c
    elif operator == "2":
        c = number_a - number_b
        return c
    elif operator == "3":
        c = number_a * number_b
        return c
    elif operator == "4":
        if number_b == 0:
            print("Do NOT divide by zero!")
            exit(1)
        else:
            c = number_a / number_b
            return c
      
wynik = kalkulator(number_a, number_b)
print(f"The result is: {wynik}")