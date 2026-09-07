import pandas as pd

# Echten Datensatz direkt aus dem Internet laden (Titanic-Datensatz)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.head())  # Zeigt die ersten 5 Zeilen des DataFrames an