import numpy as np
import pandas as pd

df = pd.read_csv('Data/us_quotations.csv')

cmd = None
while True:
    index = np.random.randint(len(df))
    while df['target'].loc[index] != -1:
        print(df['target'].loc[index])
        index = np.random.randint(len(df))
    print(df['quotation'].loc[index], '1 o 0 o exit')
    cmd = input()
    if cmd == 'exit':
        break
    elif cmd == '1':
        df.at[index, 'target'] = 1
    else:
        df.at[index, 'target'] = 0

df.to_csv('data/us_quotations.csv', index=False)
