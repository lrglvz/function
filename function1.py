# Create a program that will ask how many apples and oranges you want to buy. 
# Display the total amount you need to pay if apple is P20 and orange is P25.
# Display the output in the following format: The total amount is ________.

# functions first.
def displayIntro():
    print(f"You're in a market because you need to buy fruits for your sick partner, an apple is 20 pesos and an orange is 25.")

def appleBuy():
    apples = int(input("How many apples you want to buy? "))
    return apples

def orangeBuy():
    oranges = int(input("How many oranges you want to buy? "))
    return oranges

def applePrice():
    price = 20
    return price

def orangePrice():
    price = 25
    return price

def displaySolution(apples, appleprice, oranges, orangeprice):
    print(f"(Solution: ({apples} x {appleprice}) + ({oranges} x {orangeprice}) = ?)")

def displayAmount(amountF):
    print(f"The total amount is {amountF}.")

# introduction
displayIntro()
# amount of apples you want to buy
appleB = appleBuy()
# amount of oranges you want to buy
orangeB = orangeBuy()
# prices of apple and orange
priceA = applePrice()
priceO = orangePrice()

# solution of the total amount for better understanding.
displaySolution(appleB, priceA, orangeB, priceO)

# display the output with its total amount
displayAmount(appleB*priceA + orangeB*priceO)