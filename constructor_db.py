import pandas as pd
import sqlite3

df = pd.read_csv('gaia.csv')
df = df.dropna()

conn = sqlite3.connect('database.db')

df.to_sql('HZ_diagram', conn, if_exists='replace', index=False)
conn.close()
print('Datos de gaia migrados a database.db exitosamente.')

