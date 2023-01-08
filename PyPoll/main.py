import os 
import csv

total_votes = 0 #set total votes to 0

votes ={} #creates dictionary for name and vote count

csvpath = os.path.join('Resources', 'election_data.csv') #identify path

#opens file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader) #skips header


    candidates = [row[2] for row in csvreader] 

    total_votes = len(candidates) # counts total votes for column 3 from 0 until.

    winner = max(set(candidates),key=candidates.count) #get max count out of all candidates 

    

    for y in candidates: # count votes. get returns item of specified key or candidate

        if not votes.get(y):
            votes[y] = 1
        else:
            votes[y] += 1

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:{(total_votes)}")
    print("-------------------------")


    #print candidate name percantage and vote total
    for c,v in votes.items(): 

        print(f"{c}:{round((v/total_votes),2)*100}% {v}")

    print("--------------------------")
    print(f"Winner:{(winner)}")
    print("--------------------------")

    #write text file 
with open("analysis/Election Results.txt", "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes:{(total_votes)}\n")
    textfile.write("-------------------------\n")

    for c,v in votes.items():

        textfile.write(f"{c}:{round((v/total_votes),2)*100}% {v}\n")

    textfile.write("------------------------\n")
    textfile.write(f"Winner:{(winner)}\n")
    textfile.write("------------------------\n")

