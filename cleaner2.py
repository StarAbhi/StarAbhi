cols=int(input("Enter number of columns:"))
print(cols)
rows=int(input("Enter number of rows:"))
print(rows)
print()
for i in range(0,1):
    for j in range(0,cols):
        print("[{}][{}] is cleand".format(i,j))
    start = 1
    end=rows
    steps=1
    for j in range(cols-1,0,-1):
        for k in range(start,end,steps):
            print("[{}][{}] is cleand".format(k,j))
        temp=start
        start=end-1
        end=temp
        steps = -1*(steps)

