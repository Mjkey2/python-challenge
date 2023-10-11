#PyPoll instructions!!

#Create file paths across operating systems
import os
#module for reading csv files
import csv
#derive data set from election_data.csv
csvpath = os.path.join('Resources', 'election_data.csv')




#create a script that analyzes and calculates the following:

#Dictionary for candidates and their keys as vote count values
Candidates = {'Charles': 0, 
              'Diana': 0, 
              'Raymon': 0,
              }


with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#create these three variables
    #voter ID
    voter_idvar = []
    #county
    countyvar = []
    #candidate
    candidatevar = []
    candidateTOTAL = []
    #run through the datasheet and if charles has a vote per row add +1 to charles if not diana elif Raymon
    candidatevar.append(row[2])
    Candidates.len(candidatevar)
    
    #count number of instances for candidates
    #for row in csvreader:
        #if row[2].count("Charles"):
            #Candidates['Charles'] + 1

    Candidates['Charles'] + 1
    print(Candidates['Charles'])
#calculate the percentages. Sum all three and then find the percentages for the three


#The total number of votes cast
#count_votes.append(row[0])
#sumvotes = len(count_votes)

    #A complete list of candidates who received votes

    #The percentage of votes each candidate won

    #The total number of votes each candidate won

    #The winner of the election based on popular vote
        
###Analysis should align with the following results
    #Election Results
    
    #Total Votes: 369711
  
    #Charles Casper Stockham: 23.049% (85213)
    #Diana DeGette: 73.812% (272892)
    #Raymon Anthony Doane: 3.139% (11606)

    #Winner: Diana DeGette

#the final script should both print the analysis to the terminal and export a TEXT FILE with the results


#output = "================\n"
#output += "Election Results\n"
#output += "----------------\n"
#output += f"Total Votes: {votetotal}\n"
#output += "----------------\n"
#output += f"{Charles alphabetical order} \\\PERCENT AND TOTAL COUNT \n"
#output += f"{Diana alphabetical order} \\\PERCENT AND TOTAL COUNT \n"
#output += f"{Raymon alphabetical order} \\\PERCENT AND TOTAL COUNT \n"
#output += "----------------\n"
#output += "Winner :" + winner \n"
#output += "================"

#print(output)
#with open("./analysis/pythonpolltxt.txt", "w") as txtfile:
    #txtfile.write(output)