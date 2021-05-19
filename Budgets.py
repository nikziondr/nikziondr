class Category:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    
    def deposit(self, budget):
        amount_entered = int(input('How much do you want to deposit? \n'))
        budget.amount += amount_entered
        return print("You have deposited ${} in {} category".format(amount_entered, self.category))

    def balance(self):
        return print("This is the current balance: ${}".format(self.amount))

    def withdrawal(self, budget):
        amount_entered = int(input('How much do you want to withdraw? \n'))
        budget.amount -= amount_entered
        return print("You have withdrawn ${} in {} category".format(amount_entered, self.category))

    def transfer(self, budget):
        food_cat = Category("Food", 500)
        clothing_cat = Category('Clothing', 100)
        car_cat = Category("Car", 300)

        account_choice = int(input('Current budget selected: {}, which budget would you like to transfer money out of?\n 1.Food 2.Clothing 3.Car\n'.format(budget.category)))
        
        
        if account_choice == 1:
            account_choice = food_cat
        elif account_choice  == 2:
            account_choice = clothing_cat
        elif account_choice == 3:
            account_choice = car_cat
        else:
            print('Choose a valid option')
            budget.transfer(budget)
        
        transfer_amount = int(input('How much do you want to transfer? \n'))

        if account_choice.category != budget.category:
            account_choice.amount -= transfer_amount
            budget.amount += transfer_amount
            return print("Transfer between budget accounts completed")
        else:
            print('Cannot transfer to same budget, please choose another option')
            budget.transfer(budget)


def initial():
    print("welcome to the budget program \n")
    print("Choose a budget to start:\n")
    option = int(input("1.Food 2.Clothing 3.Car \n"))  
    
    if option == 1:
        budget = Category("Food", 500)
        operations(budget)
    elif option == 2:
        budget = Category('Clothing', 100)
        operations(budget)
    elif option == 3:
        budget = Category("Car", 300)
        operations(budget)
    else:
        print("Invalid choice, try again")
        initial()

def operations(budget):

    print('What would you like to do?')
    operation = int(input('1.Balance 2.Deposit 3.Withdrawal 4.Transfer 5.Change budget\n'))

    if operation == 1:
        budget.balance()
        operations(budget)

    elif operation == 2:
        budget.deposit(budget)
        operations(budget)

    elif operation == 3:
        budget.withdrawal(budget)
        operations(budget)

    elif operation == 4:
        budget.transfer(budget)
        operations(budget)

    elif operation == 5:
        print('====Going back to the beginning====')
        initial()

    else:
        print("Invalid choice, try again")
        operations(budget)

initial()