#Defining a 2 dimensional array of doubles #Will need to change for a specific problem.
#Basic Info About the Matrix 
A = [[1, 1, 0, 3, 4],
    [2, 1, -1, 1, 1], 
    [3, -1, -1, 2, -3],
    [-1, 2, 3, -1, 4]] 
rows = len(A) 
cols = len(A[0]) 
print("Matrix" ) 
for i in range( rows):
    print (A[i])
#Number of rows of A 
#Number of columns of A is the number of elements in the first row
#Printing the matrix row by row
#Triangularize 
for c in range(cols-2):
    #Get zeros below pivot column by column 
    for r in range(c , rows-2):
    #For each column, add to rows below. Note that c+l is variable, not constant. 
    #Could add pivoting here to get a non-zero pivot 
        if A[c][c]==0: 
            multiple = A[r][c]/A[c][c] 
            #Multiple to get zeros below pivot 
            for k in range(cols-1):
                #Going down each column k in row r 
                A[r][k] = A[r][k] - multiple*A[c][k]
                #Add multiple of pivot row c to row r
                #Print the triangularized matrix 
print("Triangularized Matrix") 
for i in range(rows-2):
    print(A[i])
    #Printing the matrix row by row
    #Back-substitution 
x = [0, 0, 0, 0]
#1 dimensional array of individual variable solutions 
x[rows-2] = A[rows-2][cols-2]/A[rows-2][cols-3]
for r in range( rows-3,0,-1 ):
#Decrementing Up From 2nd to last eqn to oth eqn
    x[r] = A[r][cols-2]
        #Solution r starts with constant term 
    for c in range( r,cols-3):
        #Subtract all the variable terms to the right
        x[r] = x[r] - A[r][c]*x[c]
        #of the pivot column (r+1 is variable)
    x[r] = x[r]/A[r][r]
#Divide by coefficient of the pivot variable
#Print the solution 
print("Solution") 
print(x)