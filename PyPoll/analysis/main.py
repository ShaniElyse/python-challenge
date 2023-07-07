import pandas as pd
import numpy as np
data = pd.read_csv('Resources\\election_data.csv')

Total_Votes=data['Ballot ID'].count()
Candidates=data['Candidate'].unique()

votes_by_candidate = data.groupby(['Candidate'])['Ballot ID'].count().reset_index()
votes_by_candidate['percent'] = votes_by_candidate['Ballot ID']/Total_Votes*100
winner = votes_by_candidate[votes_by_candidate['percent'] == votes_by_candidate['percent'].max()]['Candidate'].to_numpy()[0]

print('\n\nElection Results\n')
print('_______________________________\n\n')
print(f'Total Votes: {Total_Votes}\n\n')
print('_______________________________\n\n')
print(f'{Candidates[0]}: {votes_by_candidate.iloc[0].to_numpy()[2]:.3f}% ({votes_by_candidate.iloc[0].to_numpy()[1]})\n\n')
print(f'{Candidates[1]}: {votes_by_candidate.iloc[1].to_numpy()[2]:.3f}% ({votes_by_candidate.iloc[1].to_numpy()[1]})\n\n')
print(f'{Candidates[2]}: {votes_by_candidate.iloc[2].to_numpy()[2]:.3f}% ({votes_by_candidate.iloc[2].to_numpy()[1]})\n\n')
print('_______________________________\n\n')
print(f'Winner: {winner}\n\n')
print('_______________________________\n\n')

with open('Analysis\\output.txt', 'w') as f:
    f.write('Election Results\n')
    f.write('_______________________________\n\n')
    f.write(f'Total Votes: {Total_Votes}\n\n')
    f.write('_______________________________\n\n')
    f.write(f'{Candidates[0]}: {votes_by_candidate.iloc[0].to_numpy()[2]:.3f}% ({votes_by_candidate.iloc[0].to_numpy()[1]})\n\n')
    f.write(f'{Candidates[1]}: {votes_by_candidate.iloc[1].to_numpy()[2]:.3f}% ({votes_by_candidate.iloc[1].to_numpy()[1]})\n\n')
    f.write(f'{Candidates[2]}: {votes_by_candidate.iloc[2].to_numpy()[2]:.3f}% ({votes_by_candidate.iloc[2].to_numpy()[1]})\n\n')
    f.write('_______________________________\n\n')
    f.write(f'Winner: {winner}\n\n')
    f.write('_______________________________\n\n')
