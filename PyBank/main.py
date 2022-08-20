# Import dependencies
import os
import csv

# Set path for file
budget_data = 'Resources/budget_data.csv'

# Set path for creating new text file
text_file = os.path.join("Analysis", "pybank_analysis.txt")


# Set variables 
month_count = 0                         # Integer counting number of months in data
p_and_l = 0                             # Integer of running Profit and loss actual
pl_month_change = 0                     # Profit/loss (change), from prior month. Resets each iteration
pl_month_change_all = []                # Profit/loss (change), from prior month. Permanent
pl_month_actual = 0                     # Array of, Profit/loss (current month). Resets each iteration
pl_month_actual_all = []                # Array of, all Profit/loss (monthly). Permanent
month_date_all =[]                      # Array of, all Month dates. Permanent



# Open the csv file in read mode
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip header and read remainder of data:
    header = next(csvreader)
    
    # Calc total profit by summing monthly p/l, and calc number of rows.
    for row in csvreader:
        month_date = str(row[0])                        # Capture month date
        month_date_all.append(month_date)               # Append current month date, into an array of all month dates
        month_count = month_count + 1                   # Track no. of months
        pl_month_actual = (int(row[1]))                 # Current month P/L. Load current into a singular array
        pl_month_actual_all.append(pl_month_actual)     # Append current month P/L to array for all months
        p_and_l = p_and_l + int(row[1])                 # Running sum of P/L



# Retrieve/Calc profit/loss monthly change
for i in range(month_count - 1):
    pl_month_change = pl_month_actual_all[i+1] - pl_month_actual_all[i]
    pl_month_change_all.append(pl_month_change)



# Further calcs
avg_change = round(sum(pl_month_change_all) / len(pl_month_change_all), 2)
max_change = max(pl_month_change_all)
min_change = min(pl_month_change_all)

# Retrieve index value for max,min profit change months
max_change_month = pl_month_change_all.index(max_change) + 1
min_change_month = pl_month_change_all.index(min_change) + 1



# Analysis
print(f"Financial Analysis")
print(f"----------------------------")
print("Total Months: " + str(month_count))
print(f"Total: ${p_and_l}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {month_date_all[max_change_month]} (${max_change})")
print(f"Greatest Decrease in Profits: {month_date_all[min_change_month]} (${min_change})")



# # Create a new text file and write output to file:
# with open(text_file, "w") as out_file:
#     out_file.writelinese("Financial Analysis"
#                           "----------------------------"
#                           "Total Months: {month_count}"
#                           "Total: ${p_and_l}"
#                           "Average Change: ${avg_change}"
#                           "Greatest Increase in Profits: {month_date_all[max_change_month]} (${max_change})"
#                           "Greatest Decrease in Profits: {month_date_all[min_change_month]} (${min_change})"
#     )