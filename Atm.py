

class Atm(object):
    # Considering the variables
   

    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
     
    
    def cardNumberCheck(self): 
      x = 5000
        print("Your Balance is "+ x)
    
    def withdrawl(self,amount):
        amount = input("Enter it here")
        new_amount = x - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
def main():
        cN = input("Enter your Card Number")
        pin = input("Enter the Pin Number")

        user = Atm(cN,pin)

        print("Please mention the type of actvity you want to proceed with")
        print("1.Balance Enquriy  ; 2.withdrawl")
        
        activity = input("Enter Activity number here")
        
        if(activity == 1):
           user.cardNumberCheck()
        elif (activity == 2):
            amount = int(input("enter the amount:- "))
            user.withdrawl(amount)
        else:
            print("Invalid Number")


if __name__ == "__main__":
    main()
