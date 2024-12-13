import pandas as pd
import time
import os
import psutil

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
    print("Erreur : Aucune donnée disponible pour le benchmark.")
    exit()

# Mesurer le temps de transformation : Tri des offres par localisation
start_time = time.time()
sorted_df = df.sort_values(by="location")
end_time = time.time()

# Temps d'exécution
execution_time = end_time - start_time
print(f"Temps d'exécution pour le tri : {execution_time:.4f} secondes.")

# Mesurer l'utilisation des ressources
process = psutil.Process(os.getpid())
memory_usage = process.memory_info().rss / (1024 ** 2)  # Convertir en Mo
cpu_usage = process.cpu_percent(interval=1)

print(f"Utilisation mémoire : {memory_usage:.2f} Mo.")
print(f"Utilisation CPU : {cpu_usage:.2f} %.")

# Sauvegarder le rapport dans un fichier texte
benchmark_report = f"""
Benchmark Report
================
Temps d'exécution : {execution_time:.4f} secondes
Utilisation mémoire : {memory_usage:.2f} Mo
Utilisation CPU : {cpu_usage:.2f} %
"""
report_file = "reports/benchmark_report.txt"
os.makedirs("reports", exist_ok=True)
with open(report_file, "w") as file:
    file.write(benchmark_report)

print(f"Rapport de benchmark sauvegardé dans {report_file}.")
