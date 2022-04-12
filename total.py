Tam=int(input("Enter Tamil Mark : "))
Eng=int(input("Enter English Mark: "))
Math=int(input("Enter Maths Mark: "))
Sci=int(input("Enter Science Mark: "))
SSci=int(input("Enter Social Science Mark: "))

print("Tamil Mark is : ",+Tam)
print("English Mark is : ",Eng)
print("Maths Mark is : ",Math)
print("Science Mark is : ",Sci)
print("Social Science Mark is : ",SSci)

Total= Tam+Eng+Math+Sci+SSci
Avg = Total/5

print("Total Mark is : ", Total)
print ("Average is :",Avg)
