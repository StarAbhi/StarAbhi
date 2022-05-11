def exam(a,x):
    sqr=x+0.5*(a-x*x)/x
    return sqr
def main():
    a=int(input("Enter a positive integer "))
    sum=exam(a,2)
    print("Sum  ",sum)

main()
