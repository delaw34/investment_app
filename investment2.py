#investment application
#user enters name of the investor
#user enters the amount to invest
#application returns 50% profit on capital
#user enters amount to withdraw
#user gets a failed transaction if the inputed withdrawal amount is higher than the wallet balance
#user withdrawal transaction is successful if withdrawal amount is lower than the wallet balance
#the application deducts a 7% vat from the wallet balance


Profit_percentage = 50
Vat_percentage = 7


def investment():
       name_of_investor = (input('Enter your account name here: '))
       print('Welcome!', name_of_investor, 'to Cohort 4 Investment application')
       wallet = int(input("Enter your investment amount here: N "))
       interest_calc = wallet * Profit_percentage / 100
       wallet_balance = wallet + interest_calc    
       print(name_of_investor,'Your wallet has been credited with the sum of:','N', wallet_balance,"with a 50% interest on your capital")
       withdrawal_amount = int(input("Enter amount you want to withdraw: N"))
       if withdrawal_amount >= wallet_balance :
          print(name_of_investor," your transaction failed due to insufficient funds")
         
       else: 
           final_wallet_balance = wallet_balance - withdrawal_amount
           vat_calc = final_wallet_balance * Vat_percentage /100
           final_balance = final_wallet_balance - vat_calc   
           print(name_of_investor,"your withdrawal transaction was successful and your account has been debited with:",'N', withdrawal_amount , "and a 7% service charge", vat_calc, "has been deducted and ", 'your final balance is:' ,'N', final_balance)
investment() 
