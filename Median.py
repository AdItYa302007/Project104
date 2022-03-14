import csv
import statistics

with open("HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
sum=0
n=len(file_data)
file_data.sort()

new_data=[]
sum=0
for i in range(len(file_data)):
    num=file_data[i][2]
    new_data.append(num)

if(n%2==0):
    m1=float(new_data[n//2])
    m2=float(new_data[n//2-1])
    median=(m1+m2)/2
else:
    median=float(new_data[n//2])    
   
print(median)
