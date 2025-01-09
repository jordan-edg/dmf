import pandas as pd


df = pd.read_csv('Air_Quality_Continuous.csv')

first = '2015/01/01 00:00:00+00'
last =  '2023/10/23 00:00:00+00'

range = df[(df['Date_Time'] >= first) & (df['Date_Time'] <= last)]

range.to_csv('Air_Quality_Filtered.csv', index = False)

print(len(range))