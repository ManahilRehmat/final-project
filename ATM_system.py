import  time

print(' please enter your card')
time.sleep(5)

passward=7889
pin=int(input("enter your pin"))
balance=40000

if pin == passward:
    while True :
        print("""
        1 == balance
        2 == withdraw balance
        3 == deposit balance      
        4 == exit
        
        """
        )
        try:
           option=int(input(" please enter your choise"))
        except:
           print("please enter  valid option")

        if option == 1:
            print(f" your current balance is {balance}") 

        if option == 2:
            withdraw_amount=int(input(' please enter amount'))
            balance=balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            print(f"your curent balance is {balance}")

        if option == 3:
            deposit_amount=int(input(' please enter deposit amount'))
            balance=balance + deposit_amount 
        
            print(f"{deposit_amount} is credited to your account")

            print(f"current balance is {balance}")

        if option == 4:
            break   
else :
    print(" wrong pin plz try again")
            





