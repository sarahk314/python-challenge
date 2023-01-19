import os
import csv
from pathlib import Path

csvpath = os.path.join('Resources/election_data.csv')

total_votes = 0 
stockham_votes = 0
degette_votes = 0
doane_votes = 0

with open(csvpath, newline= "", encoding= "utf-8") as elections:
    csvreader = csv.reader(elections, delimiter=",")
    header = next(csvreader) 

    for row in csvreader:
        total_votes +=1
        if row[2] == "Charles Casper Stockham": 
            stockham_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane_votes +=1

candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [stockham_votes, degette_votes, doane_votes]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

stockham_percent = (stockham_votes/total_votes) *100
degette_percent = (degette_votes/total_votes) * 100
doane_percent = (doane_votes/total_votes)* 100

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"DeGette: {degette_percent:.3f}% ({degette_votes})")
print(f"Doane: {doane_percent:.3f}% ({doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

with open("Analysis.txt","w") as file:
    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------")
    print(f"Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    print(f"DeGette: {degette_percent:.3f}% ({degette_votes})")
    print(f"Doane: {doane_percent:.3f}% ({doane_votes})")
    print(f"----------------------------")
    print(f"Winner: {key}")
    print(f"----------------------------")
