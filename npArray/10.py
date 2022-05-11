import numpy as np
from numpy.core.records import array
def question_eight():
    arr=np.array([23,12,100,37,99,2,15,76,45,92])
    arr.sort()
    return arr[len(arr)-2:]

question_eight()
