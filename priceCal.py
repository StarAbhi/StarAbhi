import os
def calculateAmount(prices):
    cost=[]
    for i in range(len(prices)):
        if i==0:
            cost.append(prices[0])
        else:
            d=prices[0:i]
            if prices[i]-min(d) > 0:
                cost.append(prices[i]-min(d))
            else:
                cost.append(0)

    return sum(cost)


if __name__ == '__main__':
    #i save the text file in my current folder
    #you can change according to your need
    fptr = open('pricecal.txt', 'w')
    prices_count = int(input().strip())
    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    result = calculateAmount(prices)
    fptr.write(str(result) + '\n')
    fptr.close()
