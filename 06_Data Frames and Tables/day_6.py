import pandas as pd

# Dictionary : Schlüssel = Spaltenname, Wert = Liste von Werten
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age":  [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# Dictionary in DataFrame umwandeln
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

# Zugriff auf eine einzelne Spalte → ergibt eine Series
print(df["Name"])

# Zugriff auf mehrere Spalten → ergibt einen DataFrame
print(df[["Name", "Age"]])

# Zugriff auf Zeilen über die Position
print(df.iloc[0])      # erste Zeile
print(df.iloc[1:3])    # zweite bis dritte Zeile

# Zuerst die DataFrame als CSV-Datei speichern
#df.to_csv("data.csv", index=False)


# Danach die Datei wieder einlesen
df_neu = pd.read_csv("data.csv")
print(df_neu.head())
