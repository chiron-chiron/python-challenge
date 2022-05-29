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
        




    # Open csv file, prep for reading, delimit on comma, skip header
    # Put monthly pl data into list
    # with open(budget_data, newline='') as csvfile:
    #     reader = csv.reader(csvfile, delimiter=",")
    #     next(reader)                                                    #Skip header row
    #     pl_monthly = list(reader)

    #Capture difference b/w monthly profit/loss amounts
    pl_change = []
    for index,element in enumerate(pl_monthly[1:]):                 #[1:] does loop on numbers field, ignores month
        pl_change.append(int(element[1])-int(pl_monthly[index][1])) # element 1 is 2nd number, index 1 is first number in list

    average = sum(pl_change)/len(pl_change)                         #Divide 85, b/c calcs start from 2nd month, to find m:m change
    average_formatted = "${:,.2f}".format(average)
    # max_formatted = "${:,.2f}".format(max)
    # max_value = max(pl_change)

    # print(pl_change)
    # print(f"Average Change: {average_formatted}")
    # print(pl_monthly)
    # print(f"Greatest Increase in Profits: {max_formatted}")



print(f"Financial Analysis")
print(f"----------------------------")
print("Total Months: " + str(rowcount))
print(f"Total: ${pandl}")
print(f"Average Change: {average_formatted}")
# print(f"Average Change: {}")
# print(f"Greatest Increase in Profits: {} (${})")
# print(f"Greatest Decrease in Profits: {} (${})")

number_list = pl_change
max_value = max(number_list)
max_index = number_list.index(max_value)
print(max_index)
