# program to print prime numbers between 1 and 100
for num in range(2,101):
    for i in range(2,num//2+1):
        if num%i == 0 :
            break
    else:
        print(num)


