# scripts/visualize.py

import matplotlib.pyplot as plt
import numpy as np

def create_graph():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y)
    plt.title('Graphique Sinus')
    plt.xlabel('x')
    plt.ylabel('sin(x)')

    # Enregistrer le graphique
    plt.savefig('graph.png')
    plt.close()  # Ferme la figure pour libérer les ressources
    print("Graphique généré et sauvegardé sous 'graph.png'")

# Appeler la fonction pour générer le graphique
if __name__ == "__main__":
    create_graph()
