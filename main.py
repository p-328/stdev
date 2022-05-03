import sys
# import math
from func_utils import *
def main():
    mode = input("Select mode:")
    if mode == 'frequency table':
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
        try:
            print("Enter frequencies:")
            frequencies = [int(input()) for _ in range(length)]
        except ValueError:
            print("Please enter a valid number")
            sys.exit(-1)
        print("Mean: {}".format(calculateMeanFromFreq(inputs, frequencies)))
        print("Median: {}".format(calculateMedianFromFreq(inputs, frequencies)))
        print("Mode: {}".format(calculateModeFromFreq(inputs, frequencies)))
        print("Range: {}".format(max(inputs)-min(inputs)))
        print("Stdev: {}".format(calculateStdevFromFreq(inputs, frequencies)))
    else:
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
        print("Mode: {}".format(calculateMode(inputs)))
        median = calculateMedian(inputs)
        print("Median: {}".format(median))
        print("Range: {}".format(max(inputs) - min(inputs)))
        stdev = calculateStdev(inputs)
        print("Standard deviation: {}".format(stdev))
if __name__ == "__main__":
    main()
