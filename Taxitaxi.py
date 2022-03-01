class taxi:
    taxicount=0
    def __init__(self):
        taxi.taxicount+=1
        self.booked=False
        self.currentspot='A'
        self.freetime=6
        self.totalearnings=0
        self.trips=[]
        self.taxicountno=taxi.taxicount
        self.id=self.taxicountno
    



    def setdetails(self,booked,currentspot,freetime,totalearning,tripdetails):
        self.booked=booked
        self.currentspot=currentspot
        self.freetime=freetime
        self.totalearnings=totalearning
        self.trips.append(tripdetails)
        print("updated trip details",self.trips,self.totalearnings)
        
    def printdetails(self):
        print("Taxi -",self.id," Total Earnings",self.totalearnings)
        print("\n TaxiId   BookingId   from   to  pickuptime    droptime   Amount")
        for i in self.trips:
            
            print(self.id,i)



