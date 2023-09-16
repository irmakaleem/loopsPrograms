a=int(input("Enter The Value of a : "))
match a:
    case 1:
        print("case is 1")
    case 2:
        print("case is 2") 

    case 3:
        print("case is 3")

    case _ if a==6 :
        print(a)    

    case _ if a!=30:
        print("not equals to 30")    

