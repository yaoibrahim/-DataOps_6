import requests
import json
import os

# Vérifier et créer le répertoire 'data' si nécessaire
os.makedirs("data", exist_ok=True)

# Clé API SerpAPI
api_key = "dc2b0990500dc905ca9c51ac3ad947c6ecede372037a0ddb9530d3b9111026b5"
api_url = "https://serpapi.com/search"

# Paramètres de recherche des emplois
params = {
    "engine": "google_jobs",  # Utilisation de Google Jobs via SerpAPI
    "q": "developer",  # Mots-clés pour la recherche
    "location": "France",  # Localisation des offres d'emploi
    "api_key": api_key,  # Clé API SerpAPI
}

# Envoi de la requête à l'API
response = requests.get(api_url, params=params)

# Affichage du statut HTTP et de la réponse brute pour debugging
print(f"Statut HTTP : {response.status_code}")

# Sauvegarder la réponse brute dans un fichier pour analyse
with open("data/api_response.json", "w") as raw_file:
    json.dump(response.json(), raw_file, indent=4)
print("Réponse brute sauvegardée dans 'data/api_response.json'.")

# Vérification de la réponse
if response.status_code == 200:
    # Récupérer les résultats des emplois
    jobs = response.json().get("jobs_results", [])
    
    if jobs:
        # Sauvegarde des données dans un fichier JSON
        job_data = []
        for job in jobs:
            # Gestion des champs manquants
            title = job.get('title', 'Non disponible')
            company_name = job.get('company_name', 'Non disponible')
            location = job.get('location', 'Non disponible')
            job_link = job.get('job_link', 'Non disponible')

            print(f"Job Title: {title}")
            print(f"Company: {company_name}")
            print(f"Location: {location}")
            print(f"Link: {job_link}")
            print("-" * 50)

            job_data.append({
                "title": title,
                "company_name": company_name,
                "location": location,
                "job_link": job_link
            })

        # Sauvegarder les résultats des emplois dans un fichier JSON
        with open("data/job_results.json", "w") as job_file:
            json.dump(job_data, job_file, indent=4)
        print("Données des emplois sauvegardées dans 'data/job_results.json'.")
    else:
        print("Aucun résultat trouvé pour cette recherche.")
else:
    print(f"Erreur lors de la récupération des données: {response.status_code}")
