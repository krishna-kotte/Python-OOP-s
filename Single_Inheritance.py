class A: #Parent class
    def meth1(self):
        print("Method-A is printing")

class B(A): #Child Class
    def meth2(self):
        print("Method-B is printing")
 # Object is created only for class B but i can access the Class A method...
obj = B()

obj.meth1()
obj.meth2()