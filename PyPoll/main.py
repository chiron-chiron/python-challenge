import os
import csv

# election_data = 'Resources/book2.csv'
csvpath = os.path.join("Resources", "election_data.csv")

rowcount = 0
Voter_ID = []
County = []
Candidate_list = []

# Open the csv file in read mode
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)                #Skip header and read remainder of data

# Unique names
    # for row in csvreader:
    #     if row[2] not in Candidate_list:
    #         Candidate_list.append(row[2])
    # print(Candidate_list)

# How many total votes cast?
    for row in csvreader:
        rowcount = rowcount + 1


print(rowcount)
# print(f"Election Results")
# print(f"-------------------------")
print(f"Total Votes: {rowcount}")
# print(f"-------------------------")

# Unique names
file.close()


