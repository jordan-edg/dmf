import pandas as pd

aq_filtered = pd.read_csv('Air_Quality_Filtered.csv')

site_id_column = aq_filtered['Site_ID']

df = aq_filtered['Site_ID'].dropna()

cleansed = aq_filtered.loc[df.index]

cleansed['Site_ID'] = cleansed['Site_ID'].astype('int')

cleansed.to_csv('Air_Quality_Final.csv')

# Next, replace all empty values with 'NULL'






