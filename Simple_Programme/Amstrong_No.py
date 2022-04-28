print("   Amstrong Number  ")
a=int(input("Enter any number : "))
tot=0

if a<=0:
    print("Enter valid number...")
else:
    num = a
    while num != 0 :
        A = num % 10 
        tot = tot + A ** 3
        num //= 10

if a == tot:
    print("Amstrong Number")
else:
    print("Not an Amstrong Number")