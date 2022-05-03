import sys
# import math
from func_utils import *
def main():
    if sys.argv[1] == '-m':
        pass
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
