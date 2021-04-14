# pg. 56 A program to calculate the value of some change into a dollar amount

def get_change():
    print ("Change Counter. Please enter the count of each coin type below.")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = float(quarters * .25 + dimes * .10 * nickels * .05 + pennies * .01)
    print("The total value of your change is: ", total)

get_change()
