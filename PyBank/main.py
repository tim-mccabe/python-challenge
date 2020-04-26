# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = ("budget_data.csv")
with open(csvpath) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile)
    #read the header row
    header = next(csvreader)

#set variables to use as counters
    Months = 0
    Profit_Losses = 0
    Earlier_Profit = 0
    Month_Change = []
    Profit_List = []
    Greatest_Profit = ["", 0]
    Greatest_Loss = ["", 999999999]

    #extract the first row to avoid appending to Profit_List
    first_row = next(csvreader)
    Months = Months + 1
    Profit_Losses = Profit_Losses + int(first_row[1])
    Earlier_Profit = int(first_row[1])

#loop through all of the data in the workset
    for row in csvreader:

            #calculate the number of months in the data set
            Months = Months + 1

            #calculate the total amount in profit/losses
            Profit_Losses = Profit_Losses + int(row[1])

            #Calculate the change in profits from month to month
            Profit_Change = int(row[1]) - Earlier_Profit
            Earlier_Profit = int(row[1])
            Profit_List = Profit_List + [Profit_Change]
            Month_Change = Month_Change + [row[0]]

            #Calculate the greatest increase in profits (date and amount)
            if(Profit_Change > Greatest_Profit[1]):
                Greatest_Profit[0] = row[0]
                Greatest_Profit[1] = Profit_Change

            #Calculate the greatest decrease in profits (date and amount)
            if(Profit_Change < Greatest_Loss[1]):
                Greatest_Loss[0] = row[0]
                Greatest_Loss[1] = Profit_Change

#Calculate the average of the changes in "Profit/Losses"
Average = sum(Profit_List) / len(Profit_List)

#Print all of the Results
Final_Results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Months}\n"
    f"Total: ${Profit_Losses}\n"
    f"Average  Change: ${Average:.2f}\n"
    f"Greatest Increase in Profits: {Greatest_Profit[0]} (${Greatest_Profit[1]})\n"
    f"Greatest Decrease in Profits: {Greatest_Loss[0]} (${Greatest_Loss[1]})\n")

print(Final_Results)

#export the results to a text file
file_to_output = os.path.join("budget_analysis.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(Final_Results)