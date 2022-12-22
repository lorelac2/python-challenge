# Import modules
import os
import csv

# Open csv file
pypollcsv = os.path.join('ucb', 'homework', '03-python', 'python-challenge', 'PyPoll', 
                         'resources', 'election_data.csv')

# Name variables
row_count = 0
candidate = []
can0_total = 0
can1_total = 0
can2_total = 0
can_total_list = []
can_pop_vote = {}

# Open csv file
with open(pypollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Store header row
    csv_header = next(csvreader)

    # Read each row of data after the header 
    for row in csvreader:
        # Calculate total rows (total number of votes)
        row_count = row_count + 1
        # Add all candidates to a list
        if row[2] not in candidate:
            candidate.append(row[2])
        # Add up each candidates votes 
        if row[2] == candidate[0]:
            can0_total = can0_total + 1
        elif row[2] == candidate[1]:
            can1_total = can1_total + 1
        elif row[2] == candidate[2]:
            can2_total = can2_total + 1

    # Create list of each candidates total votes
    can_total_list.append(can0_total)
    can_total_list.append(can1_total)
    can_total_list.append(can2_total)

    # Calculate each candidates percentage of votes
    can0_percent = can_total_list[0]/sum(can_total_list)
    can1_percent = can_total_list[1]/sum(can_total_list)
    can2_percent = can_total_list[2]/sum(can_total_list)

    # Create dictionary of each candidates popular vote count and name winner
    can_pop_vote = {candidate[0]: can0_total, candidate[1]: can1_total, candidate[2]:can2_total}
    winner = max(can_pop_vote, key=can_pop_vote.get)

# Print summary of findings
print(" ")
print("Election Results")
print("------------------------")
print("Total Votes: " + str(row_count))
print("------------------------")
print(candidate[0] + " " + str(f"{can0_percent:.3%}") + " (" + str(can0_total) + ")")
print(candidate[1] + " " + str(f"{can1_percent:.3%}") + " (" + str(can1_total) + ")")
print(candidate[2] + " " + str(f"{can2_percent:.3%}") + " (" + str(can2_total) + ")")
print("------------------------")
print("Winner: " + str(winner))
print("------------------------")

# Export to text file
with open("ppanalysis.txt", 'w') as textfile:
    textfile.write("Election Results" + '\n')
    textfile.write("------------------------" + '\n')
    textfile.write("Total Votes: " + str(row_count) + '\n')
    textfile.write("------------------------" + '\n')
    textfile.write(candidate[0] + " " + str(f"{can0_percent:.3%}") + " (" + str(can0_total) + ")" + '\n')
    textfile.write(candidate[1] + " " + str(f"{can1_percent:.3%}") + " (" + str(can1_total) + ")" + '\n')
    textfile.write(candidate[2] + " " + str(f"{can2_percent:.3%}") + " (" + str(can2_total) + ")" + '\n')
    textfile.write("------------------------" + '\n')
    textfile.write("Winner: " + str(winner) + '\n')
    textfile.write("------------------------" + '\n')