#investment app that returns interest every 24hours
#import time modules
import time
import datetime
Profit_percentage = 10

#user enters name of the investor
name_of_investor = input("enter your name: ")
print('Welcome!', name_of_investor, 'to Cohort 4 Investment application')
#user enters the amount to invest
wallet = int(input("enter the investment amount:  "))
time_of_transaction = datetime.datetime.now()


while True:
    
   #application returns 10% profit on capital
   interest_calc = wallet * Profit_percentage / 100
   # wallet_balance = wallet + interest_calc 
   wallet += interest_calc 
   text ="{}Your account has been credited with the sum of: N{:,.2f} with a 10% interest on your capital at:'{}"
   print(text.format(name_of_investor, wallet, time_of_transaction))
    #add interest every 24hrs

   # investment_timer()
   time.sleep(24 * 60 * 60)  # 24 hours = 24 * 60 minutes * 60 seconds
     

