import math

class Currency:
    def __init__(self, denominations):
        self.denominations = denominations

class Euro(Currency):
    def __init__(self):
        denominations = {
            50000: "500 euro note",
            20000: "200 euro note",
            10000: "100 euro note",
            5000: "50 euro note",
            2000: "20 euro note",
            1000: "10 euro note",
            500: "5 euro note",
            200: "2 euro coin",
            100: "1 euro coin",
            50: "50c",
            20: "20c",
            10: "10c",
            5: "5c",
            1: "1c"
        }
        super().__init__(denominations)

class Dollar(Currency):
    def __init__(self):
        denominations = {
            10000: "100 Dollar bill",
            5000: "50 Dollar bill",
            2000: "20 Dollar bill",
            1000: "10 Dollar bill",
            500: "5 Dollar bill",
            200: "2 Dollar bill",
            100: "1 Dollar bill",
            25: "Quarter",
            10: "Dime",
            5: "Nickel",
            1: "Penny"
        }
        super().__init__(denominations)

class BalanceCalculator():
    def __init__(self, currency):
        self.currency = currency

    def calculate_denominations(self, balance):
        denominations = self.currency.denominations
        numberOfBills = []
        denomination = []
        for coin in denominations.keys():
            if balance >= coin:
                numberOfBills.append(math.floor(balance/coin))
                balance -= (numberOfBills[-1]*coin)
                denomination.append((denominations[coin]))
        return numberOfBills, denomination

def get_balance():
    while True:
        try:
            balance = int(input("Enter balance: ")) #587
            if balance > 0:
                break
            else:
                print("Please enter a number greater than 0")
        except ValueError:
            print("Please enter a whole number")
            continue
    return balance

def get_currency():
    while True:
        currency = input("Enter currency [e/euro or d/dollar]: ") #euro or dollar
        if currency.lower() in ['e', 'd', 'euro', 'dollar']:
            break
        else:
            print("The currency specified is currently not supported. Please choose from euros or dollars")
    return currency

def main():
    balance = get_balance()
    currency_input = get_currency()

    if currency_input.lower() in ['e', 'euro']:
        currency = Euro()
    else:
        currency = Dollar()

    balance_calculator = BalanceCalculator(currency)
    numberOfBills, denomination = balance_calculator.calculate_denominations(balance)

    for i in range(0, len(numberOfBills)):
        print(f'{numberOfBills[i]}- {denomination[i]}')

if __name__ == "__main__":
    main()