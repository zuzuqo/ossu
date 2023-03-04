import pandas as pd

rounds = ['Semis', 'Semis', '3rd Place', 'Championship']
teams = ['USA', 'Netherlands', 'Sweden', 'USA']
df = pd.DataFrame({'Round': rounds, 'Winner': teams})
end = '\n\n***\n'
# print(df, end=end)

df['W Goals'] = [2, 1, 0, 0]
# print(df, end=end)

# df = df.drop('Winner', axis='columns')
# print(df, end=end)

quarters_dict = {'Round': ['Quarters'] * 4, 'Winner': ['England', 'USA', 'Netherlands', 'Sweden'],
                 'W Goals': [3, 2, 2, 2]}
df = pd.concat([pd.DataFrame(quarters_dict), df], sort=True)
df = df.reset_index(drop=True)
# print(df, end=end)

# sum_goals = 0
# for i in df['W Goals']:
#     sum_goals += i
# print(sum_goals)


# print(df.loc[3:7:2], end=end)

grouped_by_round = df.groupby('Round')
print(grouped_by_round.sum())
