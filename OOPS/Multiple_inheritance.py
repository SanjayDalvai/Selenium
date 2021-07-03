class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
# Output: True
print(issubclass(list,object))

# Output: True
print(isinstance(5.5,object))

# Output: True
print(isinstance("Hello",object))