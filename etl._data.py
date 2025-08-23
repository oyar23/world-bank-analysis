import pandas as pd
import wbgapi as wb 
import os
print("Iniciando proceso de ETL")

# Parámetros globales de análisis
countries = ['ARG', 'USA', 'CHL', 'BRA', 'URY'] # 'LCN' para bloques

# carpeta '/data'
if not os.path.exists('data'):
    os.makedirs('data')

# PIB per Cápita
print("Extract & Transform dates: PIB per Cápita")
indicators_pib_pc = ['NY.GDP.PCAP.CD']
df_pib_pc = wb.data.DataFrame(indicators_pib_pc, countries, mrv=20, labels=True)
df_pib_pc = pd.melt(df_pib_pc, id_vars=['Country'], var_name='time', value_name='value')
df_pib_pc['time'] = df_pib_pc['time'].str.replace('YR', '').astype(int)
df_pib_pc = df_pib_pc.dropna(subset=['value'])

# Renombramos la columna para que quede más clara
df_pib_pc = df_pib_pc.rename(columns={'value': 'PIB per Capita (USD)'})
df_pib_pc.to_csv('data/pib_per_capita.csv', index=False)
print("-> Archivo 'pib_per_capita.csv' generado con éxito.")


# EXPORTS
print("Extrayendo y transformando datos de Exportaciones...")
indicators_exports = ['BX.KLT.DINV.CD.WD']
df_exports = wb.data.DataFrame(indicators_exports, countries, mrv=20, labels=True)
df_exports = pd.melt(df_exports, id_vars=['Country'], var_name='time', value_name='value')
df_exports['time'] = df_exports['time'].str.replace('YR', '').astype(int)
df_exports = df_exports.dropna(subset=['value'])

df_exports = df_exports.rename(columns={'value': 'Exportaciones (USD)'})
df_exports.to_csv('data/exportaciones.csv', index=False)
print("-> Archivo 'exportaciones.csv' generado con éxito.")

# IMPORTS: 
print("Extrayendo y transformando datos de Importaciones...")
indicators_imports = ['BM.GSR.TOTL.CD'] 
df_imports = wb.data.DataFrame(indicators_imports, countries, mrv=20, labels=True)
df_imports = pd.melt(df_imports, id_vars=['Country'], var_name='time', value_name='value')
df_imports['time'] = df_imports['time'].str.replace('YR', '').astype(int)
df_imports = df_imports.dropna(subset=['value'])

df_imports = df_imports.rename(columns={'value': 'Importaciones (USD)'})
df_imports.to_csv('data/importaciones.csv', index=False)
print("-> Archivo 'importaciones.csv' generado con éxito.")

print("\nProceso ETL completado.")