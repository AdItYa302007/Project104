import csv

with open("HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

new_data=[]
sum=0
for i in range(len(file_data)):
    num=file_data[i][2]
    sum=sum+float(num)

mean=sum/(len(file_data))
print(mean)

