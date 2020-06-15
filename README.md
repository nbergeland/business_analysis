# business_analysis
# Import our dependencies
import os
import numpy
import csv
import pandas as pd

file = open('./03-Python_Python-HW_Instructions_PyBank_Resources_budget_data.csv', "rU")
reader = csv.reader(file, delimiter=',')

month_set = {}
average_list = []
total_profit = 0
greatest_date = 0
greatest_tuple = None
lowest_date = 0
lowest_tuple = None
total = 0
count = 0
 
for column in reader:
    #make sure not to iterate on the column names
    if count >= 1:
        temp_profit = float(column[1])
        total = total + temp_profit
        #Keep track of all of our values for an average later. 
        average_list.append(temp_profit)
        
        #keep track of the largest amount.
        if temp_profit > greatest_date:
            greatest_date = temp_profit
            greatest_tuple = column
            
        #keep track of the lowest amount.
        if temp_profit < lowest_date:
            lowest_date = temp_profit
            lowest_tuple = column
        
    count+=1
    
    
#generate the average.
temp_average = sum(average_list) / len(average_list)

print('!!!!!!!!!!!!!!!!!!!!!!!!!!')   
print('total number of months : ' + str(len(average_list)))
print('net total amount : ' + str(total))
print('Average : ' + str(temp_average))
print('greatest value: ' + str(greatest_tuple))
print('Lowest value: ' + str(lowest_tuple))



text_file = open("pybank_output.txt", "w")
text_file.write('total number of months : ' + str(len(average_list)))
text_file.write('\n')
text_file.write('net total amount : ' + str(total))
text_file.write('\n')
text_file.write('Average : ' + str(temp_average))
text_file.write('\n')
text_file.write('greatest value: ' + str(greatest_tuple))
text_file.write('\n')
text_file.write('Lowest value: ' + str(lowest_tuple))
text_file.close()



