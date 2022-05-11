import numpy as np
def question_six():
    arr=np.array([[19,52,3,48,5],
    [30,-3,30,4,5],
    [36,62,45,-4,5],
    [69,47,3,-6,5],
    [4,78,24,45,39]])

    positive=np.where(np.all(arr>0, axis=1))
    return positive
    
question_six()
