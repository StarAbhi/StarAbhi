import numpy as np
#create 2 matrix of size 4 by 5
mat1 = np.random.randint(10, size=(4, 5))
mat2 = np.random.randint(10, size=(4, 5))

#print both matrix 
print(mat1,"\n",mat2)
#add both matrix 
print(mat1+mat2)
#multiple matrix 
#print( np.dot(mat1,mat2))
#add col 1 from mat1 with col 2 from mat2
print( mat1[:,0] + mat2[:,1])
# mat1 ^ 2 + 5*mat2 + 6
result = np.linalg.matrix_power(mat1, 2) + 5 *mat2 +6
print(result)
