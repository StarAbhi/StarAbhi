fr=int(input("Input right fornt pressure "))
fl=int(input("Input left fornt pressure "))
rr=int(input("Input right rear pressure "))
rl=int(input("Input left rear pressure "))
if fr==fl and rr==rl:
    print("Inflation is OK ")
    avg=2*(fr+rr)/2
    print("Avrage Pressure ",avg)
else:
    print("Inflation is not OK ")
