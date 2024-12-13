import pandas as pd
import matplotlib.pyplot as plt
import json
import os

# Charger les données JSON
data_file = "data/job_results.json"

# Vérification de l'existence du fichier
if not os.path.exists(data_file):
    print(f"Erreur : Le fichier {data_file} est introuvable. Exécutez 'api_job_search.py' pour générer les données.")
    exit()

# Charger les données dans un DataFrame
with open(data_file, "r") as json_file:
    job_data = json.load(json_file)

df = pd.DataFrame(job_data)

# Vérifier que le DataFrame contient des données
if df.empty:
    print("Erreur : Aucune donnée disponible pour la visualisation.")
    exit()

# Analyse 1 : Nombre d'offres par localisation
location_counts = df['location'].value_counts()

# Création du graphique : Offres par localisation
plt.figure(figsize=(10, 6))
location_counts.plot(kind="bar", color="skyblue")
plt.title("Nombre d'Offres d'Emploi par Localisation")
plt.xlabel("Localisation")
plt.ylabel("Nombre d'Offres")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Sauvegarder le graphique
graph_path = "reports/location_counts.png"
os.makedirs("reports", exist_ok=True)  # Créer le dossier 'reports' si nécessaire
plt.savefig(graph_path)
print(f"Graphique sauvegardé dans {graph_path}.")

# Génération d'un rapport HTML
html_report_path = "reports/job_report.html"
with open(html_report_path, "w") as report:
    report.write("<h1>Rapport des Offres d'Emploi</h1>")
    report.write("<h2>Graphique : Nombre d'Offres par Localisation</h2>")
    report.write(f"<img src='location_counts.png' alt='Graphique des offres par localisation'><br><br>")
    report.write("<h2>Données des Offres</h2>")
    report.write(df.to_html(index=False))

print(f"Rapport HTML généré dans {html_report_path}.")
