# keyword only arguments demo
def fun(s,*, name,age=30):
        print(name,age)

fun(10,name="smith",age=40)
fun(name="Mark",age=60)
fun("John",50)