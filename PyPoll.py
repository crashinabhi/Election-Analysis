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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

# Print each row in the CSV File
    headers = next(file_reader)
    print(headers)



