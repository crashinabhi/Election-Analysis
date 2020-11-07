# # The Data we need to retrieve
# # 1. Total number of votes cast
# # 2. A complete list of candidates who received votes
# # 3. Percentage of votes each candidte won
# # 4. THe total number of votes each candidate won
# # 5. The winner of election based on popular vote

# # Import the datetime class from the datetime module.
# import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# #Import CSV
# import csv
# print(dir(csv))

# # Assign a variable for the file to load and the path.
# file_to_load = 'election_results.csv'

# # Open the election results and read the file.
# with open(file_to_load) as election_data:

# # To do: perform analysis.
#     print(election_data)

# # Close the file.
# election_data.close()

# import os
# dir(os)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Counties in the Election\n----\nArapahoe\nDenver\nJefferson")

# # Close the file
# outfile.close()

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = 'election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vot counter
total_votes = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary
candidates_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

# Read the header now
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # 2 . Begin tracking that candidates's vote count
            candidates_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidates_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate the candidates list
for candidate_name in candidates_votes:
    # 2. retrieve the vote count of a candidate.
    votes = candidates_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidates name.
        winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)





# # 3. Print the total votes
# print(candidates_votes)











