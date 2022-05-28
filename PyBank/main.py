# **Q1** How many months of data?
# 1st Import dependencies
import os
import csv

# Set variables
rowcount = 0        #B/c using next.., this can start at 0. Integer
pandl = 0           #Profit and loss
changein = 0        #Change in profit from m to m. Temp counter, resets every loop
changein_list = []  #Array of each monthly change in profit. Permanent.

# Set path for file
budget_data = 'Resources/budget_data.csv'

# Open the csv file in read mode
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)    #Skip header and read remainder of data
    
    for row in csvreader:
        rowcount = rowcount + 1
        pandl = (pandl + int(row[1]))       #used int, as raw data doesn't show decimals
        
    for index, row in enumerate(row, start=2):
        changein = row - row[-1]
                
        #Retrieve change in monthly profit, current - previous, starting from row 3
        #  = int(row)
        #  append.changein_list
        


print(f"Financial Analysis")
print(f"----------------------------")
print("Total Months: " + str(rowcount))
print(f"Total: ${pandl}")
# print(f"Average Change: {}")
# print(f"Greatest Increase in Profits: {} (${})")
# print(f"Greatest Decrease in Profits: {} (${})")
