# varying number of arguments
def hello(*names,message="Hello"):
    for name in names:
        print(message, name)

hello("scott",message="Hi")
print("\n")
hello("scott","Mike","Smith")

def add(*n):
    sum=0
    for v in n:
        sum+=v
    return sum

print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4,5,6))