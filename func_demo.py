# default value parameters
# def line(length=10):
#     for i in range(1,length+1):
#         print("-",end="")
#
# line(20)
# print("\nHello")
# line(30)
# line()

def line(length=10,ch="-"):
    for i in range(1,length+1):
        print(ch,end="")

line(length=15,ch="*")
print("\nHello")
line(ch="^",length=20)
line(30,"$")
# line('$',30)

