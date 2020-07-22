names =["Bill","John","Smith","Mark"]
ages=[60,55,45,49]

for n,a in zip(names,ages):
    print(n,a)

for t in zip((1,2,3),('a','b','c')):
    print(t)

for t in zip((1,2,3),{'a','b','c'}):
    print(t)
