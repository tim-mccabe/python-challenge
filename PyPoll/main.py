# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = ("election_data.csv")
with open(csvpath) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile)

    #Read the header
    header = next(csvreader)

    #Create counter for total votes
    Total_Votes = 0

    #Creat counters for values of al Candidates and Votes
    Candidates = []
    Candidate_Votes = {}

    #Counters for winning votes
    Winning_Votes = 0
    Winning_Candidate = ""

    #Loop through the entire data set
    for row in csvreader:

        #Count total votes
        Total_Votes = Total_Votes + 1

        #Find the candidates name in each row
        Candidate_Name = row[2]

        #Add each new candidate to a list of candidates and count votes
        if Candidate_Name not in Candidate_Votes:
            Candidates.append(Candidate_Name)
            Candidate_Votes[Candidate_Name] = 0

        Candidate_Votes[Candidate_Name] = Candidate_Votes[Candidate_Name] + 1

# Print the results and export the data to our text file
#with open(file_to_output, "w") as txt_file:

    Election_Results = (
        f"\n\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {Total_Votes}\n"
        f"--------------------------\n"
    )
    print(Election_Results, end="")

    #txt_file.write(election_results)

     # Determine the winner by looping through the counts
    for Candidate in Candidate_Votes:

        Votes = Candidate_Votes.get(Candidate)
        Vote_Percentage = float(Votes) / float(Total_Votes) * 100

        if (Votes > Winning_Votes):
            Winning_Votes = Votes
            Winning_Candidate = Candidate
    
        #Print out each candidates results
        Election_Results_2 = f"{Candidate}: {Vote_Percentage:.3f}% ({Votes})\n"
        print(Election_Results_2, end="")

    #Print the winning candidate (to terminal)
    Winning_Candidate_Summary = (
        f"--------------------------\n"
        f"Winner: {Winning_Candidate}\n"
        f"--------------------------\n"
    )
    print(Winning_Candidate_Summary)

    #Save the winning candidate's name to the text file
    #txt_file.write(Winning_Candidate_Summary)