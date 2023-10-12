#PyPoll instructions!!

#Create file paths across operating systems
import os
#module for reading csv files
import csv
#derive data set from election_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

#Dictionary for candidates and their keys as vote count values
total_votes = 0

#variables for  candidates and their vote counts
candidates = []
candidate_votes = {}

#winning conditions
winning_candidate = ""
winning_count = 0

#read csv and convert to dictionaries
with open(file_to_load) as election_data:
    csvreader = csv.reader(election_data)
    header = next(csvreader)

    #for each row
    for row in csvreader:

        #every row add one to total votes
        total_votes += 1

        #extract candidate from each row
        candidate = row[2]

        #If candidate in row is NOT IN THE DICTIONARY
        if candidate not in candidates:
            #ADD THEM
            candidates.append(candidate)
            #AND TRACK THEIR COUNT
            candidate_votes[candidate] = 0
        #add vote to the candidates count
        candidate_votes[candidate] = candidate_votes[candidate] + 1

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:
   
    #determine winner
    for candidate in candidate_votes:
    #vote count and percentages
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

    #create final vote count and winner results
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)

    winoutput = "================\n"
    winoutput += "ELECTION RESULTS\n"
    winoutput += f"-------------------------\n"
    winoutput += f"Total Votes: {total_votes}\n"
    winoutput += f"-------------------------\n"
    winoutput += f"Winner: {winning_candidate}\n"
    winoutput += "================\n"
 
  # Save the final vote count to the text file
    txt_file.write(winoutput)

#print results
print(winoutput)
with open("./analysis/pythontxt.txt", "w") as txtfile:
    txtfile.write(winoutput)
