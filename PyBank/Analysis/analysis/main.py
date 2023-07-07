import pandas as pd
import numpy as np
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
smallest_date=data[data['changes']==greatest_decrease]['Date'].to_numpy()


print('\n\nFinancial Analysis\n')
print('_______________________________\n\n')
print(f'Total Months: {Total_Months}\n\n')
print(f'Total: ${total}\n\n')
print(f'Average Change: ${average:.2f}\n\n')
print(f'Greatest Increase in Profits: {greatest_date[0]} ({greatest_increase:0.0f})\n\n')
print(f'Greatest Decrease in Profits: {smallest_date[0]} ({greatest_decrease:0.0f})\n\n')


with open('PyBank\\Analysis\\output.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('_______________________________\n\n')
    f.write(f'Total Months: {Total_Months}\n\n')
    f.write(f'Total: ${total}\n\n')
    f.write(f'Average Change: ${average:.2f}\n\n')
    f.write(f'Greatest Increase in Profits: {greatest_date[0]} ({greatest_increase:0.0f})\n\n')
    f.write(f'Greatest Decrease in Profits: {smallest_date[0]} ({greatest_decrease:0.0f})')