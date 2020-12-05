import time

def bucketSort(array):
    start = time.perf_counter()

    end = time.perf_counter()
    finalTime = 1000 * (end - start)
    return "RadixSort for "+ str(len(array)) + " elements took "+ str(round(finalTime,10))+" miliseconds"
