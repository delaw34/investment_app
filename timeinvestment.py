#investment app that returns interest every 24hours
#import time modules
import time
Profit_percentage = 10

def investment_timer():
    
  #user enters name of the investor
   name_of_investor = "Lawrence"
   print('Welcome!', name_of_investor, 'to Cohort 4 Investment application')
   #user enters the amount to invest
   wallet = 10000
   #application returns 10% profit on capital
   interest_calc = wallet * Profit_percentage / 100
   wallet_balance = wallet + interest_calc    
   print(name_of_investor,'Your wallet has been credited with the sum of:','N', wallet_balance,"with a 10% interest on your capital")
while True:
   investment_timer()
   time.sleep(10)
     

