import pandas as pd

xls = pd.ExcelFile ('dataset/Coherence_new.xlsx')

df1 = pd.read_excel(xls, 'VAW_label_lenght')

print(df1);

df1.loc[df1['Label'] == 'Coherent', 'label_match'] = '1'
df1.loc[df1['Label'] != 'Coherent', 'label_match'] = '0'

df2 = df1[['label_match', 'Length']]

#df3['lenght']='1:' + df3['lenght']

df2['vect'] = df1['Length'].apply(lambda x: "{}{}".format('1:', x))

df3 = df2[['label_match','vect']]

print(df3)

df3.to_csv('OAV_60000_lenght.tsv', sep = '\t', index=False, header=False)