import pandas as pd
import os

# Charger les données JSON
data_file = "data/job_results.json"

# Vérification de l'existence du fichier
if not os.path.exists(data_file):
    print(f"Erreur : Le fichier {data_file} est introuvable. Exécutez 'api_job_search.py' pour générer les données.")
    exit()

# Charger les données dans un DataFrame
df = pd.read_json(data_file)

# Vérifier que le DataFrame contient des données
if df.empty:
    print("Erreur : Aucune donnée disponible pour le nettoyage ou la compression.")
    exit()

# Nettoyage des données : Suppression des lignes avec des valeurs manquantes
cleaned_df = df.dropna()
print(f"Données nettoyées : {len(cleaned_df)} lignes après suppression des valeurs manquantes.")

# Vérifier et créer le dossier pour les fichiers compressés
compressed_dir = "compressed"
os.makedirs(compressed_dir, exist_ok=True)

# Sauvegarder les données nettoyées au format Parquet
parquet_file = os.path.join(compressed_dir, "job_results.parquet")
cleaned_df.to_parquet(parquet_file, index=False)
print(f"Données compressées et sauvegardées dans {parquet_file}.")
