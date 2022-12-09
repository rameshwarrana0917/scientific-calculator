import math
print("Welcome to the calculator")
again="YES"
while(again=="YES"):
    print("Which operation you want to perform")
    choice=int(input("1.(Add Subtract Multiply Divide mod(a,b))    2.(square root and exponent)     3.(sin cos and tan) 4.(conversion): "))
    if(choice==1):
        first=float(input("Enter first number:   "))
        second=float(input("Enter second number:    "))
        print("Addition for two number are:  ",(first+second))
        print("Subtraction for two number are:  ",(first-second))
        print("Multiplication for two number are:   ",(first*second))
        print("Division for two number are:    ",(first/second))
        print("mod(first,second):   ",(first%second))
    elif(choice==2):
        inside_choice=int(input("What you want to perform (Square root(1)/Exponent(2)"))
        if(inside_choice==1):
            first=float(input("Enter the number:    "))
            print("Square root of the function is:  ",(first)**(0.5))
        elif(inside_choice==2):
            first=float(input("Enter first number:   "))
            second=float(input("Enter second number:    "))
            print("Exponent of the first to second is:  ",(first**second))
    elif(choice==3):
        first=float(input("Enter the radian value:    "))
        print("Sin of the number:   ",math.sin(first))
        print("Cos of the number:   ",math.cos(first))
        print("Tan of the number:   ",math.tan(first))
    elif(choice==4):
        inside_choice=int(input("What you want to perform (Degree to radian(1)/Radian to degree(2)"))
        if(inside_choice==1):
            first=float(input("Enter the Degree value:  "))
            print("Degree to radian is:    ",math.radians(first))
        elif(inside_choice==2):
            first=float(input("Enter the radian value:  "))
            print("Radian to degree is:    ",math.degrees(first))
    else:
        print("invalid try")
        break
    perform=input("Do you want to perform again: (Yes/NO)   ")
    again=perform.upper()