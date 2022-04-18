## Assignment

Complete the `Grouping` class in `finances.py`. It should be able to instantiate objects based on different budget groups like *food*, *clothing*, and *entertainment*. Objects from this class should have three properties:
* `name`: name of the finance group. (Food, Clothing, ...)
* `ledger`: list that can store the transactions (is empty at start)
* `balance`: the balance for this group (is 0 at start)

The class should also contain the following methods:

* A `deposit()` method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append a dictionairy to the ledger list in the form of `{"description": amount}`. The method should also increase the balance by the given amount.
* A `withdraw()` method that is similar to the `deposit()` method, but the amount passed in should be stored in the ledger as a negative number. The method should also decrease the balance by the given amount. If there are not enough funds, nothing should be added to the ledger and the balance should not change. This method returns `True` if the withdrawal took place, and `False` otherwise.
* A `get_balance()` method that returns the current balance of the budget group.
* A `transfer()` method that accepts an amount and another budget group as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Group]". The method should then add a deposit to the other budget group with the amount and the description "Transfer from [Source Budget Group]". If there are not enough funds, nothing should be added to either ledgers. The balance of both groups must also be updated appropriately. This method should return `True` if the transfer took place, and `False` otherwise. The description of each transfer should be unique. Do this by adding a timestamp.
* A `check_funds()` method that accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget group and returns `True` otherwise. This method should be used by both the `withdraw()` method and `transfer()` method.

When the budget object is printed it should display:
* A title line of 30 characters where the name of the group is centered in a line of `*` characters. (look up the center function)
* A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters. (look up how to align text using f-strings)
* A line displaying the group total.

Here is an example of the output: for `print(food)`
```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```
Tip: Look up the in-built function `__repr__()` it changes the print of an object.

#### Implementation

You can test finance.py using the examples given in `test.py`. Afterwards in `main.py` add the following groups:
* `hobby`: money spent on hobbies.
* `travel expenses`: money spent on travelling.
* `animals`: money spent on taking care of the animals.

Add a deposit of 500 for hobby, 1000 for travel expenses and 1500 for animals. Give each deposit a description. Afterwards add following expenses:
* `hobby`: 100, 200, 300 (Do not name)
* `travel expenses`: 300, 150, 800 (Name freely)
* `animals`: 400, 50 (Larger than 23 characters)

Transfer 500 from animals to travel expenses. Afterwards add following expenses:
* `travel expenses`: 800 (Name freely)
* `animals`: 200 (Name freely)

Finally, print the three objects. `travel expenses` should look as follows (except descriptions)

```
*******Travel Expenses********
Initial deposit           1000
Brussel                   -300
Maasmechelen              -150
From Travel Expenses,      500
Parijs                    -800
Total: 250.0
```

### Extra
Besides the `Grouping` class, create a function (ouside of the class) called `create_spend_chart()` that takes a list of group objects as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each group passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each group name should be vertacally below the bar. There should be a title at the top that says "Percentage spent by group".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

```
Percentage spent by group
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

#### Implementation
Use the function `create_spend_chart()` to determine the percentage spent on the groups `hobby`, `travel expenses` and `animals`. It should look as follows:

```
Percentage spent by category
100 |
 90 |
 80 |
 70 |
 60 |
 50 |
 40 |    o  o
 30 |    o  o
 20 |    o  o
 10 | o  o  o
  0 | o  o  o
     ----------
      h  T  a
      o  r  n
      b  a  i
      b  v  m
      y  e  a
         l  l
            s
         E
         x
         p
         e
         n
         s
         e
         s
```

Good luck!
