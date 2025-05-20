data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

import pandas as pd
import re

all_rows = data.strip().split('\n')


rows = [row.split(';') for row in all_rows]

df = pd.DataFrame(rows[1:], columns = rows[0])

# fill in nulls
df['FlightCodes'] = pd.to_numeric(df['FlightCodes'])
df['FlightCodes'] = df['FlightCodes'].interpolate().astype(int)

#split columns and make capital
split = df['To_From'].str.upper().str.split('_', expand=True)
df['From'] = split[1]
df['To'] = split[0]
df.drop(columns='To_From', inplace = True)
# print(df[['From', 'To']])

#make on alpha numeric
df['Airline Code'] = df['Airline Code'].apply(lambda x: re.sub(r'[^A-Za-z]','', x))
#seperate with spaces
df['Airline Code'] = df['Airline Code'].apply(lambda x: re.sub(r'(\w)([A-Z])', r'\1 \2', x))
# print(df['Airline Code'])

print(df)