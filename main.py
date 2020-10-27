import pandas as pd

name_file = "C:/Users/Javier/Downloads/Casos_positivos_de_COVID-19_en_Colombia.csv"

data_df = pd.read_csv(name_file)

print("First data in dataframe: \n %s" %data_df.head(2))
print("List of data types in dataframe: \n %s" %data_df.dtypes)

fecha_notificacion = data_df['Fecha de notificacion']
print(fecha_notificacion)