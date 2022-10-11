
def sort(li):
    if(len(li)<= 1):
        return li
    
    mid = len(li)//2
    left = li[0:mid]
    right=li[mid:]
    
    sorted_left = sort(left)
    sorted_right = sort(right)
    # print(merge([1,2],[5,4]));
    return merge(sorted_left,sorted_right)
    

def merge(left,right):
    result = []
    i=0
    j=0
    
    while(i <len(left) and j < len(right)):
        if(right[j]> left[i] ):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
   
    while(i< len(left)):
        result.append(left[i])
        i+=1
    
    while(j< len(right)):
        result.append(right[j])
        j+=1
    return result


print(sort([5,4,3,2,1]))
