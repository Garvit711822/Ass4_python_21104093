first_integer_as_divident=int(input("Enter a integer as divident:"))
second_integer_as_divisor=int(input("Enter another integer as divisor:"))
quotient=first_integer_as_divident//second_integer_as_divisor
remainder=first_integer_as_divident%second_integer_as_divisor
print("Quotient of two numbers is",quotient,"and the remainder is",remainder)
print(callable(remainder))
print(callable(quotient))
print(callable(first_integer_as_divident))
print(callable(second_integer_as_divisor))