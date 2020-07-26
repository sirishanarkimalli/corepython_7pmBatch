class Product:

    #class attribute
    taxrate=18

    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

    def show(self):
        print(f"The ID is: {self.id}")
        print(f"The name is: {self.name}")
        print(f"The price is: ${self.price}")

    @staticmethod
    def change_taxrate(newtaxrate):
        Product.taxrate=newtaxrate

    @classmethod
    def dummy(cls):
        return cls(0,"",0.00)

    def netprice(self):
        np=self.price *1.15
        return np
        # n=float("{:.2f}".format(np))
        # print(f"The net price of {self.name}, with a tax of 15% is: ${n}")

    def change_price(self,newprice):
        if newprice >= 0:
            self.price=newprice
        else :
            print("Invalid Price!")

    def setName(self,newname):
        self.name=newname

obj1=Product(1,"Milk",3.00)
obj1.netprice()
obj1.change_price(5.00)

Product.change_taxrate(20)

p=Product.dummy()
p.show()
p.setName("Smith")
p.show()
print(p)