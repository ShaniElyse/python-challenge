import pandas as pd
import numpy as 
data = pd.read_csv('PyBank\\Resources\\budget_data.csv')

#print(data.head())

#print(data.describe())

Total_Months=data['Date'].count()
total=data['Profit/Losses'].sum()

data['changes']=data['Profit/Losses'].diff()
average=data['changes'].mean()
greatest_increase=data['changes'].max()
greatest_decrease=data['changes'].min()
greatest_date=data[data['changes']==greatest_increase]['Date'].to_numpy()
smallest_date=data[data['changes']==greatest_decrease]['Date']

print(greatest_date)
print(smallest_date)

with open('PyBank\\Analysis\\output.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('_______________________________\n\n')
    f.write(f'Total Months: {Total_Months}\n\n')
    f.write(f'Total: ${total}\n\n')
    f.write(f'Average Change: ${average:.2f}\n\n')
    f.write(f'Greatest Increase in Profits: ({greatest_increase}) {greatest_date}')
    f.write(f'Greatest Decrease in Profits: ({greatest_decrease}) {smallest_date}')