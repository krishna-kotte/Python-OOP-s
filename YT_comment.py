class manifest():
    def man(self):
        global a
        global b

        a=int(input("a value:"))
        b=int(input("b value:"))
        c=a+b
        print('sum is-------->',c)
    def man2(self):
        c=a-b
        if a<b:
            c=b-a
        print("difference is- >",c)

sum=manifest()
#manifest.man(sum)
sum.man()
sum.man2()