import math

def calculateMean(arr):
    mean = 0
    for i in arr:
        mean += i
    mean = mean/len(arr)
    return mean


def calculateMedian(arr):
    arr.sort()
    median = 0.0
    if len(arr) % 2 == 0:
        sec1 = arr[:(len(arr)/2)]
        sec2 = arr[(len(arr)/2):]
        median = (sec1[len(sec1)-1] + sec2[len(sec2)-1])/2
    else:
        median = arr[int((len(arr)-1)/2)]
    return median


def calculateStdev(arr):
    arr.sort()
    difference_to_mean = [(i-calculateMean(arr)) for i in arr]
    stdev_step2 = [i**2 for i in difference_to_mean]
    stdev = 0.0
    for i in stdev_step2:
        stdev += i
    stdev = stdev/len(stdev_step2)
    stdev = math.sqrt(stdev)
    return stdev


def calculateMeanFromFreq(arr, freq):
    if len(arr) != len(freq):
        return -1
    divide = 0
    for i in freq:
        divide+=i
    mapped = zip(arr, freq)
    freq_vals = [key * value for key, value in dict(mapped).items()]
    conglomerate = 0
    for i in freq_vals:
        conglomerate += i
    return conglomerate/divide


def calculateMedianFromFreq(arr, freq):
    arr.sort()
    if len(arr) != len(freq):
        return -1
    


def calculateStdevFromFreq(arr, freq):
    arr.sort()
    if len(arr) != len(freq):
        return -1
