#PyBank Instructions!!
#Create variables for the values
#Total Number of months in the dataset
#Net TOTAL amount of Profit/losses over the entire period
#changes in profit/losses over the entire period, then AVERAGED
#greatest INCREASE in profits (date and amount) over entire period
#greatest DECREASE in profits (date and amount) over entire period

    #YOUR ANALYSIS SHOULD ALIGN WITH THE FOLLOWING RESULTS
    #__________________________________________________________________________
    #Total Months : 86
    # Total: $22564198
    #Average Change: $-8311.11
    #Greatest INCREASE: Aug-16 ($1862002)
    #Greatest DECREASE: Feb-14 ($-1825558)
#in addiction, your final script should both print the analysis to the terminal and export a text file with the results
#_______________________________________________________________________________________

#Create file paths across operating systems
import os
#module for reading csv files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#variables
total_months = 0 # create variable to store total motnhs
net_total = 0 #variable for TOTAL
total_profits = 0 # profits
total_losses = 0 # losses
greatinc = 0 #holds the number for the greatest profit increase
greatdec = 0 #holds the number for the greatest profit decrease

#open the CSV uisng the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        profits = row[1]
        date = row[0]
        #make statistics scores
        attributes = {
        #"avgchange" : 1.0 * sum(profits) / len(profits),
        "greatinc" : max(profits),
        "greatdec" : min(profits)
        }
        greatinc = attributes["greatinc"]
        greatdec = attributes["greatdec"]

        #loop through, and calculate data
                        #for row in csvreader:  NOT NEEDED BC LINE 40 
        total_months += 1 #counts total months

        #checks b column for its numbers
        if int(row[1]) > 0:
            total_profits += int(row[1])
        else : total_losses += int(row[1])

        if int(row[1]) == greatinc:
            greatincdate = row[0]
        else : greatdecdate = row[0]

        net_total = total_profits + total_losses #net gains minus net losses
        profitaverage = total_profits + total_losses / total_months

    ##TEST PRINT CSV CODE
    #print()

#output for the text file and terminal
output = "================\n"
output += f"Total Months :  {total_months}\n"
output += f"Net Total : ${net_total}\n"
output += f"Average Change : ${profitaverage}\n"
output += f"GREATEST INCREASE : {date} (${greatinc})\n"
output += f"GREATEST DECREASE : {date} (${greatdec})\n"
output += f"Net Money Gained : ${total_profits}\n"
output += f"Net Money Lossed : ${total_losses}\n"
output += "================"
print(output)
with open("./analysis/pythontxt.txt", "w") as txtfile:
    txtfile.write(output)
