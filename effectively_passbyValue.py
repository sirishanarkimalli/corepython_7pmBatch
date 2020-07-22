def zero(n): # formal parametrs
    print("Before change: ", id(n))
    n=0
    print("After change: ",id(n))

a= 100
print("Before call: ",id(a))
zero(a)  # a= actual parameter
print("After call: ",id(a))
print(a)