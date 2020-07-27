class Student:
    def __init__(self,name):
        self.name= name

    def show(self):
        print("Name= ",self.name)

class PythonStudent(Student):

    def __init__(self,name,marks):
        super().__init__(name)
        self.theory_marks=marks

    # Overriding super class show method
    def show(self):
        super().show()
        print("Theory_Marks= ", self.theory_marks)

class JavaStudent(Student):
    def __init__(self,name,title,marks):
        super().__init__(name)
        self.project_title=title
        self.project_marks=marks

    def show(self):
        print("project_title= ", self.project_title)
        print("project_marks= ", self.project_marks)

# s=Student("John")
# s.show()

p=PythonStudent("Scott",90)
p.show()
# j= JavaStudent("Steve","Robot",50)
# j.show()