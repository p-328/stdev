import sys
import math
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
inputs.sort()
mean = 0
for i in inputs:
    mean += i
mean = mean/len(inputs)
print("Mean: {}".format(mean))
freqs = [inputs.count(i) for i in inputs]
num_freqs = dict(zip(inputs, freqs))
highest = [k for k, v in num_freqs.items() if v == max(freqs)]
print("Mode: {}".format(highest[0]))
median = 0.0
if len(inputs) % 2 == 0:
    sec1 = inputs[:(len(inputs)/2)]
    sec2 = inputs[(len(inputs)/2):]
    median = (sec1[len(sec1)-1] + sec2[len(sec2)-1])/2
else:
    median = inputs[int((len(inputs)-1)/2)]
print("Median: {}".format(median))
print("Range: {}".format(max(inputs) - min(inputs)))
difference_to_mean = [(i-mean) for i in inputs]
stdev_step2 = [i**2 for i in difference_to_mean]
stdev = 0
for i in stdev_step2:
    stdev += i
stdev = stdev/len(stdev_step2)
stdev = math.sqrt(stdev)
print("Standard deviation: {}".format(stdev))
