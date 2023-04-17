#investment app

percentage = 50
percentage2 = 7



def sum():
       account_name = (input("Enter your account name here: "))
       wallet = int(input("Enter your investment amount here:  "))
       wallet_balance = wallet * (1 + (percentage / 100))
       print("Your wallet has been credited with the sum of",wallet,"and 50% interest added new balance is",wallet_balance)
       withdrawal_amount = int(input("enter amount you want to withdraww: "))
       if withdrawal_amount >= wallet_balance :
          print(account_name," you have insufficient funds")
         
       else: 
           final_wallet_balance = wallet_balance - withdrawal_amount
           vat_cal = withdrawal_amount * percentage2 / 100
           final_withdrawal_amount = withdrawal_amount - vat_cal
           rounded_num = round(final_withdrawal_amount)
           print(account_name,"your withdrawal amount is",rounded_num , "with a 7% service charge is",vat_cal, "and your balance is", final_wallet_balance)
             
       
            
    

        
    

sum()

