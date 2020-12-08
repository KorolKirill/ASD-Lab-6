import time

def insertion(inpvalue):
    for i in range(1, len(inpvalue)):
        temp = inpvalue[i]
        j = i - 1
        while (j >= 0 and temp < inpvalue[j]):
            inpvalue[j + 1] = inpvalue[j]
            j = j - 1
        inpvalue[j + 1] = temp

def bucket_sort(inpvalue):
    start = time.perf_counter()
    
    largest = max(inpvalue)
    length = len(inpvalue)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(inpvalue[i]/size)
        
        if j != length:
            buckets[j].append(inpvalue[i])
        else:
            buckets[length - 1].append(inpvalue[i])
 
    for i in range(length):
        insertion(buckets[i])
 
    res = []
    
    for i in range(length):
        res = res + buckets[i]
    


    end = time.perf_counter()
    finalTime = 1000 * (end - start)
    return "bucketsort for "+ str(len(inpvalue)) + " elements took "+ str(round(finalTime,3))+" miliseconds"
 
 

