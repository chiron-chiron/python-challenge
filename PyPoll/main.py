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