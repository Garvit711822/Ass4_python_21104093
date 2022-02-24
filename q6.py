from itertools import permutations
import enchant
d = enchant.Dict("en_US")
op=set()
word=str(input("Enter a word:"))
letters=[x.lower() for x in word ]
for n in range(len(word),len(word)+1):
    for y in list(permutations(letters,n)):
        z=(''.join(y))
        if len(z)>2:
            if d.check(z):
                op.add(z)
print(op)
