# Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.
import os


class Budget:

    def __init__(self, name):
        os.system('cls')
        self.name = name
        self.balance = 0

    # These objects should allow for Depositing funds to each of the categories
    def deposit(self, amount):
        #  os.system('cls')
        self.balance = self.balance + amount

        result = ("********** Successful Transaction **********\n")
        result += (f"You have successfully deposited ${amount} to the {self.name} budget \n")
        result += (f"Your new balance in the {self.name} budget is ${self.balance} ")

        return result

    # These objects should allow for Withdrawing funds from each category      
    def withdraw(self, amount):
        # os.system('cls')
        if self.balance < amount:
            print("********** Transaction Failed **********")
            print("Insufficient funds")

        else:
            self.balance = self.balance - amount
            result = ("********** Successful Transaction **********\n")
            result += (f"You have successfully withdrawn ${amount} from the {self.name} budget \n")
            result += (f"Your new balance in the {self.name} budget is ${self.balance}")

            return result

    # These objects should allow for Computing category balances   
    def get_balance(self):
        balance = (f"The current balance of the {self.name} budget is ${self.balance}")
        return balance

    # These objects should allow for transferring balance amounts between categories   
    def transfer(self, amount, category):

        if self.name == category.name:
            result = ("ERROR!\n")
            result += ("You cannot transfer funds within the same category\n")
            result += ("You can only transfer funds to another category")
            return result

        else:
            if self.balance < amount:
                print("********** Transaction Failed **********")
                print("Insufficient funds")

            else:
                self.balance -= amount
                category.balance += amount

                trans_result = ("********** Successful Transfer **********\n")
                trans_result += (
                    f"You have successfully transferred ${amount} from the {self.name} budget to the {category.name} budget \n")
                trans_result += (f"The current balance for the {self.name} budget is ${self.balance}\n")
                trans_result += (f"The current balance for the {category.name} budget is ${category.balance}")

                return trans_result


food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")

# # Testing the Deposit Function
print(food.deposit(10000))
print("---------------------------------" * 2)
print(clothing.deposit(5000))
print("---------------------------------" * 2)
print(entertainment.deposit(75000))

# # Testing the withdraw Function   
print("===================" * 3)
print(food.withdraw(900))
print("---------------------------------" * 2)
print(clothing.withdraw(500))

# Testing the Transfer Function                
print(food.transfer(5000, clothing))

# # Testing the Balance Function 
print("===================" * 3)
print(food.get_balance())
print("---------------------------------" * 2)
print(clothing.get_balance())
print("---------------------------------" * 2)
print(entertainment.get_balance())