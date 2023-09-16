i=0
while(i<5):
    print(i)
    i=i+1

j=int(input("Enter the number : "))
while(j>0):
    print(j)
    j=j-1    

    # Emulating a do-while loop to get a positive number from the user
while True:
    user_input = int(input("Enter a positive number: "))
    if user_input > 0:
        break
    else:
        print("Please enter a positive number.")
