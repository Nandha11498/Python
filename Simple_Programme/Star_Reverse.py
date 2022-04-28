print("		Star pattern Programme  ")
a=int(input(" Enter the number of lines : "))
for i in range (0,a):
    for j in range (a,i,-1):
        print("*", end=" ")
    print()