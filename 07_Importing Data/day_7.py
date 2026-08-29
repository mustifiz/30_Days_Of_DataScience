import pandas as pd

# Lesen der CSV-Datei in ein DataFrame
df = pd.read_csv('/Users/musticodes/Desktop/30_Days_Of_DataScience/07_Importing Data/data.csv')
print(df.head())  # Anzeigen der ersten fünf Zeilen des DataFrames

df = pd.read_csv("/Users/musticodes/Desktop/30_Days_Of_DataScience/07_Importing Data/data.csv", skiprows=2, names=["ID", "Name", "Age", "City"])
print(df)


## Lesen Json -Datei in ein DataFrame

# Beispiel für das Lesen einer JSON-Datei in ein DataFrame
data = {
    "Name": ["Alice", "Bob"],
    "Details": [
        {"Age": 25, "City": "New York"},
        {"Age": 30, "City": "Los Angeles"}]

        }

# Normalisieren der verschachtelten JSON-Daten in ein flaches DataFrame
df = pd.json_normalize(data, 'Details', ['Name'])
print(df)
