print("   Reverse Number Program ")
revno = 0
n=int(input("Enter the number : "))
b = n  

if n == 0 :
    print("Enter the valid number")
else:
    while (n!=0):
        a = n % 10      
        revno = revno * 10  + a
        n //= 10   
    print("Reverse Number is : ", revno) 
    if revno == b:
        print ("The given number is a palindrome")  
    else:
        print ("The given number is not a palindrome")