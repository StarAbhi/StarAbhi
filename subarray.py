# Function to find sublists with the given sum in a list
def findSublists(A, sum):
 
    for i in range(len(A)):
 
        sum_so_far = 0
 
        # consider all sublists starting from `i` and ending at `j`
        for j in range(i, len(A)):
 
            # sum of elements so far
            sum_so_far += A[j]
 
            # if the sum so far is equal to the given sum
            if sum_so_far == sum:
 
                # print sublist `A[i, j]`
                print(A[i:j+1])
 
 
if __name__ == '__main__':
 
    A = [3, 4, -7, 1, 3, 3, 1, -4]
    sum = 7
 
    findSublists(A, sum)