import pandas as pd

df = pd.read_excel ('dataset/Coherence_new.xlsx', sheet_name='VAW_labelled', skiprows='1')

df2 = df[['subject','Label']]

print(df2)

df2.to_csv('VAW.csv',index=False)