import os
import csv
from pathlib import Path

csvpath = os.path.join('Resources/budget_data.csv')

total_months = []
total_profit = []
monthly_profit_change = []

with open(csvpath, newline="", encoding= "utf-8") as budget:
    csvreader = csv.reader(budget, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
