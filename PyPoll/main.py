import os
import csv

# Set file for path
# election_data = 'Resources/book2.csv'
csvpath = os.path.join("Resources", "election_data.csv")



# Set variable
rowcount = 0                # Integer counting number of votes
voter_ID = []               
county = []
candidate_list = []

# Dictionary of each candidates votes
counter = {
    "Correy": 0,
    "Khan": 0,
    "Li": 0,
    "OTooley": 0
}



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


