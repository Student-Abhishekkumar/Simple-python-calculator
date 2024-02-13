def menu():
    print("\n..............Basic calculator...........\n")
    print("\t1. ADD")
    print("\t2. SUBTRACT")
    print("\t3. DIVIDE")
    print("\t4. MULTIPLY")

while True:
    try:
        x=input("Enter your first number : ")
        y=input("Enter your second number : ")

        menu()
        choice=int(input("Choose Which Operation You Want TO perform : "))

        if(choice=='1'):
            print("Your add number : " , x+y ) 

        elif(choice=='2'):
            print("Your subtract number : " , x-y )

        elif(choice=='3'):
            print("Your divide number : " , x/y )

        elif(choice=='4'):
            print("Your mulyiply number : " , x*y )

        else:
            print("input correct integer......")

        a=input("If you want to continue or not..... (y/n) : ")
        if(a=='n'):
            break

    except:
        print(".....INVALID INPUT.....")
        