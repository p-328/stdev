import sys
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
def main():
    try:
        print("How many numbers do you have in your set?")
        length = int(input())
    except ValueError:
        print("Please enter a valid number")
        sys.exit(-1)
    try:
        print("Enter nums: ")
        inputs = [float(input()) for _ in range(length)]
    except ValueError:
        print("Please enter a valid number")
        sys.exit(-1)
    mean = mean(inputs)
    print("Mean: {}".format(mean))
    freqs = [inputs.count(i) for i in inputs]
    num_freqs = dict(zip(inputs, freqs))
    highest = [k for k, v in num_freqs.items() if v == max(freqs)]
    print("Mode: {}".format(highest[0]))
    median = calculateMedian(inputs)
    print("Median: {}".format(median))
    print("Range: {}".format(max(inputs) - min(inputs)))
    stdev = calculateStdev(inputs)
    print("Standard deviation: {}".format(stdev))
if __name__ == "__main__":
    main()
