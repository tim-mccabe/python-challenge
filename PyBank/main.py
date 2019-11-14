# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = ("budget_data.csv")
with open(csvpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #header = next(csvreader)

#set variables to use as counters
    Months = 0
    Profit_Losses = 0
    Earlier_Profit = 0
    Month_Change = []
    Profit_List = []
    Greatest_Profit = ["", 0]
    Greatest_Loss = ["", 999999999]

#loop through all of the data in the workset
    for row in csvreader:

            #calculate the number of months in the data set
            Months = Months + 1

            #calculate the total amount in profit/losses
            Profit_Losses = Profit_Losses + int(row["Profit/Losses"])

            #Calculate the change in profits from month to month
            Profit_Change = int(row["Profit/Losses"]) - Earlier_Profit
            Earlier_Profit = int(row["Profit/Losses"])
            Profit_List = Profit_List + [Profit_Change]
            Month_Change = Month_Change + [row["Date"]]

            #Calculate the greatest increase in profits (date and amount)
            if(Profit_Change > Greatest_Profit[1]):
                Greatest_Profit[0] = row["Date"]
                Greatest_Profit[1] = Profit_Change

            #Calculate the greatest decrease in profits (date and amount)
            if(Profit_Change < Greatest_Loss[1]):
                Greatest_Loss[0] = row["Date"]
                Greatest_Loss[1] = Profit_Change

#Calculate the average of the changes in "Profit/Losses"
Average = sum(Profit_List) / len(Profit_List)

#Print all of the Results
Final_Results = (
    print("Total Months: " + str(Months))
    print("Total: $" + str(Profit_Losses))
    print("Average Change: " + str(Average))
    print("Greatest Increase in Profits: " + str(Greatest_Profit[0]) + " $" + str(Greatest_Profit[1]))
    print("Greatest Decrease in Profits: " + str(Greatest_Loss[0]) + " $" + str(Greatest_Loss[1])))

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)