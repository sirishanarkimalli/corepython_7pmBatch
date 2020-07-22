# keyword arguments demo
def fun(**details):
    for k,v in details.items():
        print(k,v)

# fun(a=10,b=20,message="hi")

# both varying aruguments and keyword arguments
def fun1(*n,**d):
    for v in n:
        print(v)
    for k,v in d.items():
        print(k,v)

fun1(10,20,30, a=70,b="asa")
