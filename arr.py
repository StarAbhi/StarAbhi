#by using  numpy.subtract() function 
  
import numpy as np 
new = np.zeros((256,256))
rms = np.arange(256)
print ("1st Input array : ", new)
print ("2nd Input array : ", rms)
   
for i in range(0,256):
    for j in range(0,256):
        new[i][j]=new[i][j]-rms[j];
print ("Output array: ",new ) 

