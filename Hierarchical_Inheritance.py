class A: #Parent class
    def meth1(self):
        print("Method-A is printing")

class B(A): #Child Class
    def meth2(self):
        print("Method-B is printing")

class C(A): #Child class
    def meth3(self):
        print("Method-C is printing")
# Object is created only for class C but I can access the Class A method...
obj_C = C()

# Object is created only for class B but I can access the Class A method...
obj_B = B()

#.................
obj_B.meth1()
obj_B.meth2()
#..................
obj_C.meth1()
obj_C.meth3()