#!/usr/bin/env python
"""change_return.py

Find the correct change for a given cost and amount paid. Include
coin amounts. Currency is in Canadian dollars, which no longer uses
pennies, so coins consist only of quarters, dimes, and nickels."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

def get_currency(msg):
    while(True):
        try:
            currency = raw_input(msg)
            currency = (float)(currency)
            currency = round(currency, 2)
            if currency < 0:
                raise ValueError
            return currency
        except(ValueError):
            print("Your input is invalid. Please try again.")

def main():
    print("Note: currency amounts will be rounded to nearest cent.")
    cost = get_currency("Please enter the cost: ")
    payment = get_currency("Please enter the amount paid: ")

    if (payment < cost):
        print("Amount paid is insufficient.")
    elif (payment == cost):
        print("Exact payment made, no change necessary.")
    else:
        total_change = round(payment - cost, 2)
        change = (int)(100 * total_change)

        dollars = change / 100

        change = change - (dollars * 100)
        quarters = change / 25

        change = change - (quarters * 25)
        dimes = change / 10

        change = change - (dimes * 10)
        nickels = change / 5

        change = change - (nickels * 5)
        if(change > 2):
            nickels += 1

        print("Total change: {}".format(total_change))
        print("Required bills and change:")
        print("Dollars: {}".format(dollars))
        print("Quarters: {}".format(quarters))
        print("Dimes: {}".format(dimes))
        print("Nickels: {}".format(nickels))

if __name__ == "__main__":
    main()
