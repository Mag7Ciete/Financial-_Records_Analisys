import os
import csv

#initialize variables
candidates = []
votes = 0
vote_tot = []

#set path
#file_name = "Resources", "election_data.csv"
csvfile = os.path.join("Resources", "election_data.csv")

#open the file
with open(csvfile,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the header
    line = next(csvreader,None)

    #go line by line and process each vote
    for line in csvreader:

        #add to total number of votes
        votes = votes + 1

        #candidate voted for
        candidate = line[2]

        #if candidate has other votes then add to vote tally
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_tot[candidate_index] = vote_tot[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_tot.append(1)

percentages = []
max_votes = vote_tot[0]
max_index = 0
#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_tot[count]/votes*100
    percentages.append(vote_percentage)
    if vote_tot[count] > max_votes:
        max_votes = vote_tot[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]:,.3f}% ({vote_tot[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_results_summary.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]:,.3f}% ({vote_tot[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()