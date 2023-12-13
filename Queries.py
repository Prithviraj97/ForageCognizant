def answerQueries(queries):
    
    arr = [False]*1000001
    ans = []
    true_indices = []
    
    for q in queries:
        
        # Set index to true 
        if q[0] == 1: 
            index = q[1] - 1
            arr[index] = True
            true_indices.append(index)
            
        # Get nearest true index  
        else:
            index = q[1] - 1 
            i = binarySearch(true_indices, index)
            if i != -1: 
                ans.append(i+1)
            else:
                ans.append(-1) 
                
    return ans

def binarySearch(arr, x):
    #Implement binary search   
    return index