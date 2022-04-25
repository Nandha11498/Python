print("Identity Operators -In , Not in ")
a=int(input("Enter the a value: "))
b=int(input("Enter the b value: "))
namelist=[1,5,3,8,7,11,4,8,3,5,9,7,4,1]
if ( a in namelist):
	print(" value is in the NameList")
else:
	print("value is not in the NameList")
    
if a not in namelist :
    print("value is not in the namelist")
else:
    print ("value is in the namelist")