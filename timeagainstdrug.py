import csv
import matplotlib.pyplot as plt
import seaborn as sns

with open('weighted-to-timeline.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    
time_x=[]
admet_y=[]
swiss_y=[]
xundrug_y=[]

#print(data[1][3])
#print(len(data[1][3]))

for i in range(len(data)-1):
    row=data[i+1]
    date = row[3]
    countSlash = 0
    twoDigit = -1
    
    #For every character, if it's a / indicating date separator, then increment counter. Take the year after 2x / are found
    for j in range(len(date)):
        if (date[j] == '/'):
            countSlash += 1
        if (countSlash == 2):
            twoDigit = int(date[j + 1] + date[j + 2])
            #print(twoDigit)
            #time.sleep(20)
            break
        
    #If no date, no plot
    if (twoDigit == -1):
        print("Date not found")
        continue
    elif (twoDigit > 25):
        twoDigit += 1900
    else:
        twoDigit += 2000
        
    #print(row[7])
    time_x.append(twoDigit)
    
    #For each PK predictor, if no value given, add None
    try:
        admet_y.append(float(row[7]))
    except(ValueError):
        admet_y.append(None)
    try:
        swiss_y.append(float(row[11]))
    except(ValueError):
        swiss_y.append(None)
    try:
        xundrug_y.append(float(row[8]))
    except(ValueError):
        xundrug_y.append(None)
        
    '''
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
    '''
    
#print(len(time_x))
#print(len(admet_y))

# admet scatterplot
plt.plot(time_x, admet_y,'.')
# plotting the trend line using linear regression
plt.xlabel('years')
# naming the y axis 
plt.ylabel('Admetlab weighted score')

# giving a title to my graph 
plt.title('year vs Admetlab weighted score')

# plotting the trend line using linear regression
#sns.regplot(x = time_x, y = admet_y)
# function to show the plot
plt.show()

#swissadme scatterplot
plt.plot(time_x, swiss_y,'.')
plt.xlabel('years')
# naming the y axis
plt.ylabel('SwissADME weighted score')
  
# giving a title to my graph
plt.title('year vs SwissADME weighted score')
 
# plotting the trend line using linear regression
#sns.regplot(x = time_x, y = swiss_y)
# function to show the plot
plt.show()

#xundrug scatterplot
plt.plot(time_x, xundrug_y,'.')
plt.xlabel('years')
# naming the y axis
plt.ylabel('XunDrug weighted score')
  
# giving a title to my graph
plt.title('year vs XunDrug weighted score')

# plotting the trend line using linear regression
#sns.regplot(x = time_x, y = xundrug_y)
# function to show the plot
plt.show()
