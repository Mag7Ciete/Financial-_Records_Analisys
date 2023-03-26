
import os
import csv

#called out file 
csvpath = os.path.join("Resources", "budget_data.csv")

#Create list 
with open(csvpath, 'r') as readfile:
  
    months = 0 
    prof_loss = 0 
    change = []
    previous = 0
    average = []
    date = []
#Read file 
    csvreader = csv.reader(readfile, delimiter=",")
    
    eachdate = []
    Increase = []
    Decrease = []
#determine first row as file header
    header = next(csvreader)
#find totals, transaction , total proft/loss , average
    for row in csvreader:
        months = months + 1
        prof_loss = prof_loss + int(row[1])
        lastprofit = int(row [1])
        change = int(row[1]) - previous 
        previous = int(row[1])
      
        average.append(change)
        eachdate.append(row[0]) 
    average.pop(0)              
#calculating  average 
    totalaverage = (sum(average) / (months-1))
date.append(row[0])
#calculating the increase total profit 
increaseprofit = max(average)
 #calculating the decrease total profit 
decreaseprofit = min(average)

#finding the date related t tthe incrersed total 
increased_date = eachdate[average.index(increaseprofit)]
decreased_date = eachdate[average.index(decreaseprofit)]


print("Total Months:", (months))
print("Total:",(f'${prof_loss:,.2f}'))
print("Total Average:", (f'${totalaverage:,.2f}'))
print("Greatest Increase in Profits: " + str(increased_date) + " ($" + str(increaseprofit) + ")")
print("Greatest Decrease in Profits: " + str(decreased_date) + " ($" + str(decreaseprofit) + ")")


Outputfile= os.path.join( "Resources" , "analysis")


with open(Outputfile, "w") as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f'----------------------------------------------\n')
    textfile.write(f'Total Months: {months}\n')
    textfile.write(f'Total: ${prof_loss:,.2f}\n')
    textfile.write(f'Average Change ${totalaverage:,.2f}\n')
    textfile.write(f'Greatest Increase in Profit: {increased_date} {increaseprofit}\n')
    textfile.write(f'Greatest Decrease in Profit: {decreased_date} {decreaseprofit}\n')

                   


    
         

