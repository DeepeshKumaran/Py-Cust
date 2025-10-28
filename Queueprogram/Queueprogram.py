from datetime import datetime
import pandas as pd
from collections import deque
class CustOrder:
    def __init__(self):
        #Initializing queue
        self.orderno=1
        self.queue=deque()
        self.history=pd.DataFrame(columns=['Package ID','Package Name','Order Time','Delivery Time'])
    
    def enqueue(self,order_name):
        #Adding new order to queue
        order={'Order_ID':self.orderno,'name':order_name,'time_ordered':datetime.now().strftime('%d-%b-%Y %H:%M:%S'),'time_deli':None}
        (self.queue).append(order)
        print(f'Order no. {self.orderno} {order_name} is placed at {order["time_ordered"]}.')
        self.orderno+=1

    def dequeue(self):
        #Removing order first in queue
        if not self.queue:
            print('Queue is empty. No more orders to deliver.')
        else:
            deliv=self.queue.popleft()
            deliv['time_deli']=datetime.now().strftime('%d-%b-%Y %H:%M:%S')
            new_entry={'Package ID':deliv['Order_ID'],'Package Name':deliv['name'],'Order Time':deliv['time_ordered'],'Delivery Time':deliv['time_deli']}
            self.history=pd.concat([self.history,pd.DataFrame([new_entry])],ignore_index=True)
            print(f'Order no. {deliv["Order_ID"]} {deliv["name"]} is delivered at {deliv["time_deli"]}.')

    def peek(self):
        #Looking at order first in queue
        if not self.queue:
            print('Queue is empty. No more orders to deliver.')
        else:
            deliv=self.queue[0]
            print(f"Next order in queue is order no. {deliv['Order_ID']} {deliv['name']} was placed at {deliv['time_ordered']}.")
    
    def display(self):
        #Looking at entire queue
        if not self.queue:
            print('Queue is empty. No more orders to deliver.')
        else:
            for i in self.queue:
                print(f'Order no. {i["Order_ID"]}: {i["name"]} was placed at {i["time_ordered"]}.')
    
    def disphis(self):
        #Looking at entire history
        if self.history.empty:
            print('History is empty. Nothing to print.')
        else:
            print('Delivery History:')
            print(self.history.to_string(index=False))
    
    def search(self):
        #Searching for an order
        df=pd.DataFrame(self.history)
        if df.empty:
            print('History is empty. No orders to search for.')
        else:
            no=int(input('Enter the order no. to search for: '))
            res=df[df['Package ID']==no]
            if res.empty:
                print(f'Order no. {no} was not found in history.')
            else:
                print('Found in History')
                print(res.to_string(index=False))


if __name__=="__main__":
    q=CustOrder()
    while True:
        print()
        print('----- CUSTOMER ORDER QUEUE -----')
        print('1. Add new order')
        print('2. Deliver order')
        print('3. Look at order first in queue')
        print('4. Look at entire queue')
        print('5. Look at entire history')
        print('6. Look for order in history')
        print('7. Exit the program')
        print('--------------------------------')
        try:
            chc=int(input('Enter which action you wish to perform: '))
            print()
            if chc==1:
                order=input('What order would you like to add to queue: ')
                q.enqueue(order)
            elif chc==2:
                q.dequeue()
            elif chc==3:
                q.peek()
            elif chc==4:
                q.display()
            elif chc==5:
                q.disphis()
            elif chc==6:
                q.search()
            elif chc==7:
                print('Exiting the program')
                break
            else:
                print('Invalid input')
        except ValueError:
            print('Invalid input')
            continue



    