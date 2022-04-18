# This test file is to be used to test finance.py development. 
# It already contains a few examples of things to check.
# Start by reading README.md
import finance
from finance import create_spend_chart

# Setup for output as seen in README.md
food = finance.Grouping("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = finance.Grouping("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = finance.Grouping("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# Output as seen in README.md
print(food)
print(create_spend_chart([food, clothing, auto]))