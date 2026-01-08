class calc:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def pow(self,a,b):
        return a**b

cal=calc()

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power")
    print("6.Exit")

    choice=input("Enter your choice(1-6): ")
    
    if choice=="6":
        print("Exiting,Thankyou!")
        break
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))

    if choice=="2":
        print("Result: ",cal.sub(a,b))
    elif choice=="1":
        print("Result: ",cal.add(a,b))
    elif choice=="3":
        print("Result: ",cal.mul(a,b))
    elif choice=="4":
        print("Result: ",cal.div(a,b))
    elif choice=="5":
        print("Result: ",cal.pow(a,b))

    else:
        print("Error!!!!")