print("Enter number of columns:",end=" ")
cols=int(input())
print(cols)
print("Enter number of rows:",end=" ")
rows=int(input())
print(rows)
print()
side="left"
print("[0][0] is cleaned")
for i in range(0,rows-1):
    if side=="left":
        for j in range(1,cols):
            print("Move forward")
            print("[{i}][{j}] is cleaned".format(i=i,j=j))
    else:
        for j in range(cols-2,-1,-1):
            print("Move forward")

            print("[{i}][{j}] is cleaned".format(i=i,j=j))
    if(i!=rows-1):
        if side=="left":
            print("Turn right")
            print("[{i}][{j}] is cleaned".format(i=i+1,j=cols-1))
            side="right"
    else:
        print("Turn left")
        print("[{i}][{j}] is cleaned".format(i=i+1,j=0))
        side="left"