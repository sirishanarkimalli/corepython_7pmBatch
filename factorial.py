num= int(input("Enter a num"))
i=fact=1
while i<=num :
    # fact=fact*i
    fact*=i
    i+=1
else:
    print("Over")

print(f"Factorial of {num} is {fact}")
print("Factorial of {0} is {1}".format(num,fact))