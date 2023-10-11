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
total_months = [] # create variable to store total motnhs
net_total = [] #variable for TOTAL
average_change = [] #finds average change

monthly_change = 0
monthly_change_total = 0 #
profit_counter = 0 # counts the profits :^3

#open the CSV uisng the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        #make statistics scores
        total_months.append(row[0])
        SumMonths = len(total_months)
        net_total.append(float(row[1]))
        ProfitForMonth = int(row[1])
        monthly_change = float(ProfitForMonth)
        monthly_change_total += monthly_change
        profit_counter = int(row[1])
        average_change.append(monthly_change)
        MaxProfit = max(average_change)
        MaxIndex = average_change.index(MaxProfit)
        MinProfit = min(average_change)
        MinIndex = average_change.index(MinProfit)
        AverageChangeProfit = round(monthly_change_total/SumMonths)
        SumAmount = sum(net_total)

#output for the text file and terminal
output = "================\n"
output += f"Total Months :  {SumMonths}\n"           ###CHECK
output += f"Net Total : ${SumAmount}\n"                 ###CHECK
output += f"Average Change : ${AverageChangeProfit}\n"
output += f"GREATEST INCREASE : {total_months[MaxIndex]} (${MaxProfit})\n"
output += f"GREATEST DECREASE : {total_months[MinIndex]} (${MinProfit})\n"

output += "================"
print(output)
with open("./analysis/pythontxt.txt", "w") as txtfile:
    txtfile.write(output)
