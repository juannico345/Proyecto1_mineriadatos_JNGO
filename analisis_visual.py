import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

con = sqlite3.connect('database.db')
consult = "SELECT * FROM HZ_diagram"

df =  pd.read_sql_query(consult, con)

con.close()

print("Datos extraidos de la base de datos:")
print(df)

condicion =  (df['radius_gspphot'] > 8.5) & (df['teff_gspphot'] < 6000) & (df['mg_gspphot'] < 3)
df_RBG = df[condicion]
df_nRBG = df[~condicion]

fig, ax = plt.subplots()

ax.scatter(df_nRBG['bp_rp'],df_nRBG['mg_gspphot'],color = 'blue',s = 1)
ax.scatter(df_RBG['bp_rp'],df_RBG['mg_gspphot'],color = 'red',s = 1,alpha = 0.5)

ax.invert_yaxis()

plt.savefig('resultado.png')

print('Se ha guardado la imagen con éxito: resultado.png')


