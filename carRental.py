class BikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print('Total Bikes: ' , self.stock)

    def rentForBikes(self,q):
        if q<=0:
            print('Enter positive value')

        elif q>self.stock:
            print('Enter value less then stock')
        else:
            self.stock= self.stock-q
            print('Total price', q*100)
            print('Total Bikes', self.stock)

while True:
    obj = BikeShop(100)
    uc = int(input(
        '''
            1) Display Stocks
            2) Rent a Bike
            3) Exit 
        '''
    ))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input('Enter the QTY---'))
        obj.rentForBikes(n)
    else:
        break
        