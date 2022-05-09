print (" 	SIMPLE MODULE PROGRAMME  ")
def Base_fun(t,e,m,s,ss):
    print ("\t Subject \t Marks ")
    print ("\t Tamil  \t  ",t)
    print ("\t English  \t  ",e)
    print ("\t Maths  \t  ",m)
    print ("\t Science  \t  ",s)
    print ("\t Social  \t  ",ss)
    tot=t+e+m+s+ss
    avg=tot/5
    print("\n\tTotal Mark is : ",tot)
    print("\n\tAverage is : ",avg)
    return;
