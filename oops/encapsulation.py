'''Demonstration of encapsulation'''


class BankAccount:
    '''A basic BankAccount class where you can withdraw and deposit amount

    Args: account_number(str): unique identifier
          amount(float): intial amount of the account holder
    
    Raises:it will raise value error if the unique identifier is not valid
    
    
    '''

    def __init__(self,account_number:str,amount:float):

        if amount<0:
            raise ValueError('Amount cannot be negative at the time of initialization')
        
        self.__account_number = account_number # private attribute
        self.__amount = amount


    def getCurrentBalance(self):
        '''Public method to get the balance '''
        return self.__amount
    

    def deposit(self,balance:float):
        '''public method to deposit the balance 

        Args: balance(float) - Balance user want to deposit to their existing amount
       
        Raises: ValueEroor if the amount is less than ZERO
        '''
        if balance<0 or not isinstance(balance,(int,float)):
            raise ValueError("Deposit amount should be a valid amount (float Non negative)")
        self.__amount += float(balance)
        print("Deposit succesfull")
        print(f"The total amount in our account is now {self.__amount}")


    def withDraw(self,balance:float):
        '''public method to withdraw amount from the account
        
        Args: balance(float) - The specific amount user want to withdraw 

        Raises: ValueError("If the specific amount is less than ZERO")
        '''
        if balance<0:
            raise ValueError("Withdraw amount should not be less thn zero")
        
        if balance > self.__amount:
            raise ValueError(f"You don't have sufficient balance to withdraw..You current balance is{self.__amount}")

        self.__amount -= balance
        print(f"Balance withdraw succesfully")
        print(f"Your current balance is {self.__amount}")
    

    def infoAccount(self):
        '''Method to get the bank account details'''
        print(f'Your Account Number is : {self.__account_number}')
        print('-'*30)
        print(f'Your Account balance is : {self.__amount}')
        print('-'*30)
        print('Thank You')



if __name__ == "__main__":
    '''Drive function to check the class and its methods'''
    
    account = BankAccount("3456767780955",500)
    account.deposit(250)
    account.infoAccount()
    print(f'current balance is {account.getCurrentBalance()}')
    account.withDraw(60)

    # print(account.__account_number) will throw error that account object has no attribute 
    
 

