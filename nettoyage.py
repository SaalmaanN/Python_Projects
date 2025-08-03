# nettoyage.py
import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("data.csv")

# Supprimer les lignes avec des valeurs manquantes
df_clean = df.dropna()

# Enlever les doublons
df_clean = df_clean.drop_duplicates()

# Sauvegarder le résultat
df_clean.to_csv("data_clean.csv", index=False)

print("Nettoyage terminé. Données sauvegardées.")
