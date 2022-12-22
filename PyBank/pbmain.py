# Import modules
import os
import csv

# Open csv file
pybankcsv = os.path.join('ucb', 'homework', '03-python', 'python-challenge', 'PyBank', 
                         'resources', 'budget_data.csv')

# Name variables
row_count = 0
price_total = 0
date = []
profit = []
profit_change = []

# Open csv file
with open(pybankcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Store header row
    csv_header = next(csvreader)

    # Read each row of data after the header 
    # Calculate total number of rows (total months) and total profit
    # Create lists for dates and profits
    for row in csvreader:
        row_count = row_count + 1
        price_total = price_total + int(row[1])
        date.append(str(row[0]))
        profit.append(int(row[1]))

    # Calculate changes in profit and calculate average change in profit
    for i in range(1, len(profit)):
        profit_change.append(profit[i] - profit[i-1])
        avg_profit = sum(profit_change)/len(profit_change)

    # Calculate greatest increase and decrease of profit
    gprofit = max(profit_change)
    lprofit = min(profit_change)

    # Find date of greatest increase and decrease of profit
    gdate = date[profit_change.index(gprofit) + 1]
    ldate = date[profit_change.index(lprofit) + 1]
    
# Print summary of findings        
print(" ")
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(price_total))
print("Average Change: $" + str(round(avg_profit, 2)))
print("Greatest Increase in Profit:  " + gdate + " ($" + str(gprofit) + ")")
print("Greatest Decrease in Profit: " + ldate + " ($" + str(lprofit) + ")")

# Export as text file
with open("pbanalysis.txt", 'w') as textfile:
    textfile.write("Financial Analysis" + '\n')
    textfile.write("------------------------" + '\n')
    textfile.write("Total Months: " + str(row_count) + '\n')
    textfile.write("Total: $" + str(price_total) + '\n')
    textfile.write("Average Change: $" + str(round(avg_profit, 2)) + '\n')
    textfile.write("Greatest Increase in Profit: " + gdate + " ($" + str(gprofit) + ")" + '\n')
    textfile.write("Greatest Decrease in Profit: " + ldate + " ($" + str(lprofit) + ")" + '\n')
    

