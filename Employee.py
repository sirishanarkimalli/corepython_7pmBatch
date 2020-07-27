#  3 attributes and one special method ans show
class Employee:
    # attribues :id,name,job
    # dunder
    # self=obj1
    #
    def __init__(self,id,name,job):
        # private, public protected
        self.id=id
        self.name=name
        self.__job=job  # private

    def show(self):
        print(f"Id  :{self.id}")
        print(f"Name  :{self.name}")
        print(f"Id  :{self.__job}")

    def change_job(self,newjob):
        self.__job=newjob

obj1 =Employee(1,"Scott","Programmer")
obj2 =Employee(2,"Mark","Manager")
obj1.change_job("SRM")
obj1.show()
obj1.age=20
obj1._Employee__job="Lead"
# calling a method
obj1.show()

print(obj1.__dict__)
print(obj2.__dict__)


