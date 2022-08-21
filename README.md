## python-challenge

### Purpose
Bootcamp homework assignment aimed at creating scripts to analyse to seperate data sets.
Summarised financial statement data and election poll data.

### Languages used
Python

### Objectives

1. PyBank:
    Create a Python script for analysing the financial records of a fictious company.
    Financial data in the form of budget_data.csv is provided to analyse.
    Data consists of two columns, date and profit/loss.

    Create Python script that analyses the records and calcualtes the following:
    * The total number of months included in the dataset
    * The net total amount of "Profit/Losses" over the entire period
    * The average of the changes in "Profit/Losses" over the entire period
    * The greatest increase in profits (date and amount) over the entire period
    * The greatest decrease in losses (date and amount) over the entire period


2. PyPoll:
    Create a Python script to modernise a small rural towns, vote counting process.
    Poll data is provided in the form of election_data.csv, to analyse.
    Data consists of three columns, voter id, county, candidate.

    Create Python script that calculates the following:
      * The total number of votes cast
      * A complete list of candidates who received votes
      * The percentage of votes each candidate won
      * The total number of votes each candidate won
      * The winner of the election based on popular vote.


### Code: PyBank
```Python
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
```

```Python
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average Change: $-2315.12
# Greatest Increase in Profits: Feb-12 ($1926159)
# Greatest Decrease in Profits: Sep-13 ($-2196167)
```


### Code: PyPoll
```Python
# Dependecies
import os
import csv



# Set variables
candidate_name_votes = []                   # Array of all votes cast, as expressed by candidate name. So an array of all 
vote_data = []                              # Array all voting data
votes_total = 0                             # Integer for tallying total votes
vote_percent_candidate_sorted = []          # Array of percentages (of votes won) for each candidate (sorted descending)



# Set file for path
from typing import OrderedDict

# Set variable for csv path
csvpath = os.path.join("Resources", "election_data.csv")


# Open the csv file in read mode
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)                        #Skip header and read remainder of data
    
    # Retrieve csv file into vote_date, and print candidate name from votes, into seperate array
    for row in csvreader:
        vote_data.append(row)                           # Array all voting data
        candidate_name_votes.append(row[2])             # Retieve candiate voted for from each vote cast, i.e Candidate column



# Remove duplicates form candidate_list array, to get clean list of all candidates
candidate_list_clean = list(OrderedDict.fromkeys(candidate_name_votes))


# Convert list to dictionary, assign 0 values (i.e votes) for each key (i.e. candidate)
vote_counter = dict.fromkeys(candidate_list_clean, 0)



# Iterate on clean dictionary of candidates, and iterate on array of all votes (as captured by candidate name), and tally votes.
for key in vote_counter:
    
    votes = 0                                           # By placing here, will reset vote counter to 0, for proceeding candidate loop in vote_counter.
    
    for vote in candidate_name_votes:
        if key == vote:                                 # vote represents cast vote, as expressed in candidates name. So if dictionary key matches vote,
            vote_counter[key] = vote_counter[key] + 1   # Add 1 vote to dictionary value for current iteration (i.e. candidate)
            votes = votes + 1                           # Track votes for current iteration (i.e. candidate)
    
    votes_total = votes_total + votes                   # This will tally all votes, for each iteration (i.e. candidate)



# Sort dictionary by values descending, so highest votes to lowest votes.
vote_counter_sorted = dict(sorted(vote_counter.items(), key=lambda x:x[1], reverse = True))



# Print results

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {votes_total}")
print(f"-------------------------")

# For loop on key and value of sorted (descending by votes) dictionary, print each candidates results.
for key, value in vote_counter_sorted.items():
    vote_percent = round(((value) / votes_total * 100), 3)
    vote_percent_candidate_sorted.append(vote_percent)
    print(f'{key}: {vote_percent}% ({value})')
    
print(f"-------------------------")

# Retrieve 1st key from sorted (descending by votes) dictionary, print key (i.e name of candidate that got most votes)
print(f"Winner: {list(vote_counter_sorted.keys())[0]}")
print(f"-------------------------")
```


``` Python
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.0% (2218231)
# Correy: 20.0% (704200)
# Li: 14.0% (492940)
# O'Tooley: 3.0% (105630)
# -------------------------
# Winner: Khan
# -------------------------
```