from Taxitaxi import taxi












def getfreetaxi(arr,pickuptime,pickupspot):
    res=[]
    for i in arr:
        # freetime as well as able to reach within pickup time
        if i.freetime <= pickuptime and abs(ord(i.currentspot)-ord(pickupspot)) <= pickuptime-i.freetime :
            res.append(i)
    return res
def sorttaxi(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i].totalearnings>a[j].totalearnings:
                a[i],a[j]=a[j],a[i]
    return a

def booktaxi(id,pick,drop,picktime,available):

    near=1000
    
    

    #checking for nearest taxi
    for i in available:
        distance_between_customer_taxi=abs(ord(i.currentspot)-ord(pick)) *15
        if(distance_between_customer_taxi<near):
            booked=i
            distance=abs(ord(pick)-ord(drop))*15
            earning=100+(5*(distance-5))  #first 5 km 100 hence distance minus 5
            droptime=picktime+(distance//15)
            nextfreetime=droptime
            nextspot=drop
            trip=str(id) +"        "+str(id)+"          "+pick+"       "+drop+"        "+str(picktime)+"      "+str(droptime)+"          "+str(earning)

        near=distance_between_customer_taxi
    booked.setdetails(True,drop,droptime,i.totalearnings+earning,trip)
    print("Booked successfully...  taxi: "+str(booked.id))






no_of_taxi=[]
#for now four taxies
taxione=taxi()
no_of_taxi.append(taxione)
taxotwo=taxi()
no_of_taxi.append(taxotwo)
taxithree=taxi()
no_of_taxi.append(taxithree)
taxifour=taxi()
no_of_taxi.append(taxifour)


while True:

    

    print('enter\n 0 for booking \n 1 for taxi details')
    n=int(input())
    
    customerid=1
    if n==0:
        #taxi booking
        print("Pick up point: ")
        pick=input()
        print("\nDrop point: ")
        drop=input()
        print("\nPickup time:")
        pickuptime=int(input())#absolute time only

        freetaxi=getfreetaxi(no_of_taxi,pickuptime,pick)
        if len(freetaxi)==0:
            print("\n No available taxi wait for a while")
        else:
            available=sorttaxi(freetaxi)
            booktaxi(customerid,pick,drop,pickuptime,available)
            customerid +=1
    elif n==2:
        break
    else:
        for i in no_of_taxi:
        
            i.printdetails()

            

