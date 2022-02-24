""" iterative function to calculate Pascals Triangle """
rows=int(input("Enter number of rows:"))
for i in range(rows):
    print(''*(rows-i),end='')
    print(''.join(map(str,str(11**i))))