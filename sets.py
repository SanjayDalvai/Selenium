print("Hello World")

# Python program to
# demonstrate sets

def asc():

    a=246
    b=1
    c=a+b
    return c
# Same as {"a", "b", "c"}
myset1 = set(["a", "1", "sanjay",2,3,4,5,6,7,10,11])
print(myset1)

myset2 = set([asc(),10,11,12,"sagara"])

# Adding element to the set
myset1.add("dalvai")

myset3 = myset1.union(myset2)

print(myset3)
