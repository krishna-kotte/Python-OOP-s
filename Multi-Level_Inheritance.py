class A: #Grand-Parent class
    def meth1(self):
        print("Method-A is printing")

class B(A): #Parent Class
    def meth2(self):
        print("Method-B is printing")

class C(B): #Child class
    def meth3(self):
        print("Method-C is printing")
 # Object is created only for class C but I can access the Class A and Class B method...
obj = C()

obj.meth1()
obj.meth2()
obj.meth3()