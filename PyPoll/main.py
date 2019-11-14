# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = ("election_data.csv")
with open(csvpath, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Create counter for total votes
    Total_Votes = 0

    #Creat counters for values of al Candidates and Votes
    Candidates = []
    Candidate_Votes = []

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
            Candidate_Votes.append(Candidate_Name)
            Candidate_Votes[Candidate_Name] = 0

        Candidate_Votes[Candidate_Name] = Candidate_Votes[Candidate_Name] + 1

# Print the results and export the data to our text file
with open(file_to_output, "w") as txt_file:

    Election_Results = (
        print("Total Votes: " + str(Total_Votes))
    ) 
    print(Election_Results)

    txt_file.write(election_results)

     # Determine the winner by looping through the counts
    for candidate in Candidate_Votes:

        Votes = Candidate_Votes.get(Candidate)
        Vote_Percentage = float(Votes) / float(Total_Votes) * 100

        if (Votes > Winning_Votes):
            Winning_Votes = Votes
            Winning_Candidate = Candidate
    
    Election_Results_2 = print("Candidate: " + str(Vote_Percentage) + "% " + str(Votes))
    print(Election_Results_2)

    txt_file.write(election_results_2)