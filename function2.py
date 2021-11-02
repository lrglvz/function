# Create a program which you will enter the amount of money you have,
# it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format: You can buy ___ apples and your change is ___ pesos.

# functions first!
def displayIntro():
    print(f"A conversation between a vendor and a buyer.")

def vendorAsk():
    print(f"Vendor: How much money do you have?")

def buyerMoney():
    moneyAmount = int(input("Buyer: "))
    return moneyAmount

def buyerAsk():
    print(f"Buyer: How much is an apple?")

def vendorAns():
    applePrice = int(input("Vendor: "))
    return applePrice

def displaySolution(moneyAmount, applePrice):
    print(f"(Solution: ({moneyAmount} // {applePrice}) and ({moneyAmount} % {applePrice}) = ?)")


def displayAmount(maximumApple, change):
    print(f"Vendor: You can buy {maximumApple} apples and your change is {change} peso/s.")


# introduction
displayIntro()

# enter the amount of money you have.
vendorAsk()
money = buyerMoney()

# enter the price of an apple.
buyerAsk()
price = vendorAns()

# solution for better understanding how it happened.
displaySolution(money, price)

# finally, the output.
displayAmount(money//price, money%price)