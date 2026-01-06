class calc:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

cal=calc()

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice=input("Enter your choice(1-5): ")
    
    if choice=="5":
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

    else:
        print("Error!!!!")