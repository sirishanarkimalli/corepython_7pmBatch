# Passing function names as paramters
def mathop(op,a,b):
    return op(a,b)

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

print("Add= ",mathop(add,20,30))
print("Mul= ",mathop(mul,20,30))
