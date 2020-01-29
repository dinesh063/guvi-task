startingPoint=int(input("enter starting point:"))
endingPoint=int(input("enter ending point:"))
distance=endingPoint-startingPoint
services=['cab','auto','suv']
amt=0
for i in range(1,len(services)+1):
    print(i,services[i-1])
while(1):
    ride=int(input("choose your ride(1-3):"))
    if(ride>3 or ride<=0):
        print("invalid ride option")
    
    elif(ride==1):
        amt=distance*12
        break
    elif(ride==2):
        amt=distance*8
        break
    else:
        amt=distance*20
        break
print("total amount:",amt,"rs")
