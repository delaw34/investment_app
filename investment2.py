#investment app
# user adds name
# user add amount
# application returns 50% profits on capital
# user enter withdraws amount
# user get a failed transaction if input amount is higher than account balance
# user gets credited  if input amount is lower than account balance
# application get 7% service charge from account balance

profit_percentage = 50
vat_percentage = 7


def investment():
       account_name = (input('Enter your account name here: '))
       print('Welcome!', account_name, 'to cohort 4 Investment application')
       wallet = int(input("Enter your investment amount here: N "))
       intrest = wallet * profit_percentage / 100
       wallet_balance = wallet + intrest
       print(account_name,'Your wallet has been credited with the sum of:','N', wallet_balance,"with a 50% interest on your capital")
       withdrawal_amount = int(input("Enter amount you want to withdraw: N"))
       if withdrawal_amount >= wallet_balance :
          print(account_name," your transaction failed due to insufficient funds")
         
       else: 
           final_wallet_balance = wallet_balance - withdrawal_amount
           vat_reduction = final_wallet_balance * vat_percentage /100
           final_balance = final_wallet_balance - vat_reduction
           print(account_name,"your withdrawal transaction was successful and your acount has been debited with:",'N', withdrawal_amount , "and a 7% service charge has been deducted and ",'your final balance is:' ,'N', final_balance)
investment()
