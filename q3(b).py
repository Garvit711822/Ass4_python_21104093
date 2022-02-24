first_integer_as_divident=int(input("Enter a integer as divident:"))
second_integer_as_divisor=int(input("Enter another integer as divisor:"))
quotient=int(first_integer_as_divident//second_integer_as_divisor)
remainder=int(first_integer_as_divident%second_integer_as_divisor)
print("Quotient of two numbers is",quotient,"and the remainder is",remainder)
if(quotient==0):
    print("quotient is zero")
else:
    print("quotient is non zero")
if(remainder==0):
    print("remainder is zero")
else:
    print("remainder is non zero")