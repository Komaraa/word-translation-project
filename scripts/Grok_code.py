import math
import time
import pandas as pd
import subprocess
from deep_translator import GoogleTranslator

def run_git_command(command):
    """Exécute une commande git et affiche le résultat."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Git: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur Git: {e.stderr}")

def translate(listwords, batch_size=3799):
    """Traduisez une liste de mots anglais en français par lots, sauvegardez en CSV, et committez sur GitHub."""
    print("Traduction des mots...")
    start = time.time()
    num_batches = math.ceil(len(listwords) / batch_size)
    all_translations = []
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, len(listwords))
        batch_words = listwords[start_idx:end_idx]
        # Nettoyage : garder les chaînes valides
        batch_words = [word for word in batch_words if isinstance(word, str) and word.strip()]
        print(f"Lot {i + 1}/{num_batches}: {len(batch_words)} mots")
        # Traduction
        try:
            translations = GoogleTranslator(source='en', target='fr').translate_batch(batch_words)
            print(f"Traduction lot {i + 1}: {translations}")
        except Exception as e:
            print(f"Erreur lot {i + 1}: {e}")
            translations = [None] * len(batch_words)
        # Paires
        pairs = list(zip(batch_words, translations))
        all_translations.extend(pairs)
        # Sauvegarde lot
        lot_file = f"translations_lot_{i+1}.csv"
        df = pd.DataFrame(pairs, columns=["english", "french_auto"])
        df.to_csv(lot_file, index=False, encoding="utf-8")
        # Pas de git add/commit pour les CSV (ignorés par .gitignore)
        time.sleep(2)  # Pause pour Google
    # Sauvegarde globale
    global_file = "translations.csv"
    df = pd.DataFrame(all_translations, columns=["english", "french_auto"])
    df.to_csv(global_file, index=False, encoding="utf-8")
    # Commit du code (pas des CSV)
    run_git_command("git add translate.py")
    run_git_command(f"git commit -m 'Mise à jour du script de traduction après {num_batches} lots'")
    run_git_command("git push origin main")
    end = time.time()
    print(f"Temps total: {end - start:.2f} secondes")
    return all_translations

# Test
if __name__ == "__main__":
    listwords = ["hello", "world", "test", "translation", "example"]
    translate(listwords, batch_size=2)