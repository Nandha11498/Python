print("\n    Fibonacci Serious")
nterms=int(input("\n Enter the Number of Terms : "))
a = 0
b = 1
c = 0

if nterms<=0:
    print ("\n Enter the Valid number! ")
elif nterms == 1 :
    print ("\n The fibonacci Serious step 1 : ",a)
else:
    n = 1
    while c < nterms:
        print ("\n The fibonacci Serious step - {0} : {1} ".format(n,a))
        d = a + b
        a = b
        b = d
        c+=1
        n+=1
 