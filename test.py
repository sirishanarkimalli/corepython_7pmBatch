num = int(input("Enter a number"))
# for n in range(1,num +1):
#     if num%n == 0 :
#         print(n)

for i in range(2,num//2+1):
    if num%i == 0:
        print("Not a prime")
        break
else:
    print("prime")


