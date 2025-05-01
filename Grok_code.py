import math
import time
import pandas as pd
from deep_translator import GoogleTranslator


def translate(listwords,batch_size=3799) -> list[tuple[str, str]]:
    print("Traduction des mots...")
    start = time.time()
    num_batches = math.ceil(len(listwords) / batch_size)
    all_translations = []
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, len(listwords))
        batch_words = listwords[start_idx:end_idx]
        print(batch_size)
        print(f"Lot {i + 1}/{num_batches}: {len(batch_words)} mots")
        
        # À toi : Traduire batch_words
        try:
            print(f"params: {batch_words}")
            translations = GoogleTranslator(source='en',target='fr').translate_batch(batch_words)
            time.sleep(2)  # Pause de 1 seconde entre les traductions
        except Exception as e:
            print(f"Erreur lot {i + 1}: {e}")
            translations = [None] * len(batch_words)
        # À toi : Créer des paires (mot, traduction)
        pairs = list(zip(batch_words, translations))
        all_translations.extend(pairs)
        # À toi : Sauvegarder pairs dans translations_lot_{i + 1}.csv (Question 5)
        with open(f"translations_lot_{i+1}.csv", 'w') as f:
            for word, translated in pairs:
                f.write(f"{word},{translated}\n")
    # À toi : Sauvegarder all_translations dans translations.csv
    with open("translations.csv", 'w') as f:
        for word, translated in all_translations:
            f.write(f"{word},{translated}\n")
    # À toi : Afficher le temps total de traduction
    end = time.time()
    print(f"Temps total: {end - start:.2f} secondes")
    return all_translations

# Test de la fonction translate
if __name__ == "__main__":
    listwords = ["hello", "world", "test", "translation", "example"]
    translate(listwords, batch_size=2)
    # Test de la fonction translate avec une liste de mots 