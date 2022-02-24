first_integer_as_divident=int(input("Enter a integer as divident:"))
second_integer_as_divisor=int(input("Enter another integer as divisor:"))
quotient=first_integer_as_divident//second_integer_as_divisor
remainder=first_integer_as_divident%second_integer_as_divisor
print("Quotient of two numbers is",quotient,"and the remainder is",remainder)
list=list()
list.append(remainder)
list.append(quotient)
list.append(4)
list.append(5)
list.append(6)
print("old list:",list)
new_list=[]
for i in list:
    if i>4:
        new_list.append(i)
set=set(new_list)
print("set:",set)
new_set=frozenset(set)
print("immutable set is:",new_set)
new_set.add(0)