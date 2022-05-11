def calculateSeries(n):
    y=0
    k=0
    for i in range(1,n+1):
        k=i**(i+1)
        y +=k
    return y
def main():
    num=int(input('Enter value of "n": '))
    print("Y=",calculateSeries(num))
main()