import csv
import matplotlib.pyplot as plt 

with open('weighted-to-timeline.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
x=[]
y=[]

print(data[1][3])
print(len(data[1][3]))

for i in range(len(data)-1):
    row=data[i+1]
    try:
        if len(row[3])==11:
            if int(row[3][4]+row[3][5])>25:
                y.append(float(row[7]))
                x.append(int("19"+row[3][4]+row[3][5]))
                
            else:
                y.append(float(row[7]))
                x.append(int("20"+row[3][4]+row[3][5]))
                
                
        elif len(row[3])==12:
            if int(row[3][5]+row[3][6])>25:
                y.append(float(row[7]))
                x.append(int("19"+row[3][5]+row[3][6]))
                
            else:
                y.append(float(row[7]))
                x.append(int("20"+row[3][5]+row[3][6]))
                

        elif len(row[3])==12:
            if int(row[3][5]+row[3][6])>25:
                y.append(float(row[7]))
                x.append(int("19"+row[3][5]+row[3][6]))
                
            else:
                y.append(float(row[7]))
                x.append(int("20"+row[3][5]+row[3][6]))
                
        else:
            print("failed")
    except:
        print("error")
    
    
    if len(x) !=len(y):
        print(x)
        print(y)
        break

plt.plot(x, y,'.') 
plt.xlabel('years') 
# naming the y axis 
plt.ylabel('admet lab weighted score') 
  
# giving a title to my graph 
plt.title('year vs weighted score') 
  
# function to show the plot 
plt.show()

