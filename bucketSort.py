def in_sort(array):
    for i in range(1,len(array)):
        x = array[i]
        j =  i - 1
        while x < array[j] and j >= 0:
            array[j + 1]=array[j]
            j -= 1
        array[j + 1] = x
    return array

def buckrt_sort(string_array):
    #create a bucket to hold the element
    b = []
    #create a empty buckets according to the length of the 
    #given string array length
    for i in range(len(string_array)):
        b.append([])
    
    #find max from string array 
    maxOfstring =max(string_array)
    #determine which value in string array goes which 
    # bucket in the above empty bucket
    #find size
    size = maxOfstring/len(string_array)
    #based on size insert element in bucket

    for i in range(len(string_array)):
        j=int (string_array[i]/size)
        if j != len(string_array):
            b[j].append(string_array[i])
        else:
            b[len(string_array) - 1].append(string_array[i])
        
    #sort element within the new buckets
    for x in range(len(string_array)):
        in_sort(b[x])
    
    final_sorted_list=[]
    for y in range(len(string_array)):
        final_sorted_list=final_sorted_list+b[y]
    return final_sorted_list

print(buckrt_sort(["jfd232", "abc123", "kjl532", "abd321", "bci992"]))