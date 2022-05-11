#function that return a new list of integers from lst 
def only_ints(lst):
    #create a empty list for int
    int_lst=[]
    #check all data from lst and check if any integer is in lst append in int_lst
    for i in lst:
        if isinstance(i, int):
            int_lst.append(i)
    #return the int_lst
    return int_lst
#main function that demonstrates how the function can be use 
if __name__ == "__main__":
    lst = [2.15, 3, 8.2, -1, 6]
    print("Original List : ",lst)
    print("Integers List From Original List : ",only_ints(lst))
    