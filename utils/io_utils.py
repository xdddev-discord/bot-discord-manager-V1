# utils/io_utils.py
import json

def load(fichier):
    """Charge un fichier JSON et le retourne sous forme de dictionnaire."""
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
        return {}
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON dans le fichier {fichier}.")
        return {}
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return {}

def save(donnees, fichier):
    """Sauvegarde les données dans un fichier JSON."""
    try:
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, ensure_ascii=False, indent=4)
        print(f"Les données ont été sauvegardées dans {fichier}.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la sauvegarde : {e}")
