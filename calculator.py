class calc:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

cal=calc()

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Exit")

    choice=input("Enter your choice(1-3): ")
    
    if choice=="3":
        print("Exiting,Thankyou!")
        break
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))

    if choice=="2":
        print("Result: ",cal.sub(a,b))
    elif choice=="1":
        print("Result: ",cal.add(a,b))    
    else:
        print("Error!!!!")