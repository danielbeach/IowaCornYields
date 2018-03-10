import pandas as pd

df = pd.read_csv('C://Iowa Corn Yields.csv')
total = df.groupby(['Year','County'])[['Value']].sum()
print(total.query('Year==2017').sort_values('Value', ascending=False).head(10))