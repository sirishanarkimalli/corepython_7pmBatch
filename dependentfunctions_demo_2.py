# def iseven(n):
#     if n%2 ==0 :
#         return True
#     else:
#         return False

nums=[10,11,24,27,80]

# for n in filter(iseven, nums):
#     print(n)

for n in filter(lambda n : n%2 ==0, nums):
    print(n,end=" ")


print("\n")
for n in sorted(nums,key=lambda n : n if n>=0 else -n):
    print(n, end=" ")

# #  sorted(iterable,*,key=None,reverse=False)
#
# nums=[1,11,4,7,80]
#
# def squares(n):
#     return n*n
#
print("\n")
for n in map(lambda n : n*n , nums):
    print(n,end=" ")
