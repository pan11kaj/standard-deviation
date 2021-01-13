import csv;
import math;
f = open("data.csv")
reader = csv.reader(f)
file_data = list(reader)
data = file_data[0]
def calculateMean(data):
    total = 0
    for x in data:
        total+=int(x)
    mean = total/10
    return mean
square_list =[]
for number in data:
    x = int(number)-calculateMean(data)
    x = (x**2)
    square_list.append(x)
Sum = 0
for x in square_list:
    Sum = Sum+x
rslt = Sum/(len(data)-1)
std = math.sqrt(rslt)
print("your standard Deviation is-> "+str(std))