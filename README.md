# python-challenge

PYBANK
# import os module to create file path
import os 

# module for reading CSV file 
import csv

#create variables and paramenters
months_total = 0
total_profit= 0
month_list = []
profit_list = []

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader) 

    first_row = next(csvreader)
    
    months_total += 1
    total_profit += int(first_row[1])
    prev_net = int(first_row[1])
    
    #read each row and write data
    for row in csvreader:

        months_total += 1 #add months to each other by line
        total_profit += int(row[1]) #add profit together line by line to get total
        net_change = int(row[1]) - prev_net #subtract profit from line above to get net change throughout entire list
        prev_net = int(row[1]) 
        profit_list += [net_change] #create a new list with net change
        month_list += [row[0]] #create month list


    net_monthly_average = sum(profit_list)/len(profit_list)    #finding avg net change
    greatest_increase = max(profit_list) #max
    greatest_decrease = min(profit_list) #min

  #index greatest increase and decrease amount to indicate the month associated with profit number on the same line  
greatest_increase_month = month_list[(profit_list.index(greatest_increase))] 
greatest_decrease_month = month_list[(profit_list.index(greatest_decrease))]

#print solution to terminal
print ("Financial Analysis")
print ("----------------------")
print (f"Total Months:{(months_total)}")
print (f"Total: ${(total_profit)}")
print (f"Average Change: ${round(net_monthly_average)}")
print (f"Greatest Increase In Profits: {greatest_increase_month} (${greatest_increase})")    
print (f"Greatest Decrease In Profits: {greatest_decrease_month} (${greatest_decrease})")
#write to new file
with open("analysis/Financial Analysis.txt", "w") as textfile:
    textfile.write ("Financial Analysis\n")
    textfile.write ("----------------------\n")
    textfile.write(f"Total Months:{(months_total)}\n")
    textfile.write (f"Total: ${(total_profit)}\n")
    textfile.write(f"Average Change: ${round(net_monthly_average)}\n")
    textfile.write (f"Greatest Increase In Profits: {greatest_increase_month} (${greatest_increase})\n")    
    textfile.write(f"Greatest Decrease In Profits: {greatest_decrease_month} (${greatest_decrease})\n")
