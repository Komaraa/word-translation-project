# Portfolio : Traduction et Scraping de Mots

## Description

Ce projet scrape **136,764 mots anglais** depuis [Simple Wikipedia](https://simple.wikipedia.org/wiki/Wikipedia:BASIC_English_alphabetical_wordlist), les traduit en français par lots de **3,799 mots** avec `GoogleTranslator`, et sauvegarde les résultats en CSV. L’objectif est de créer une liste de mots **transparents** (similaires orthographiquement et sémantiquement) pour des textes lisibles par des anglophones. Ce projet est conçu comme un **portfolio** pour démontrer mes compétences en Python, scraping, et gestion de projets Git.

**Technologies** : Python, pandas, deep-translator, requests, BeautifulSoup, Git.

## Compétences démontrées

- **Python** : Gestion de données avec pandas, traduction par lots, scraping avec BeautifulSoup.
- **Web Scraping** : Extraction et nettoyage de mots depuis Simple Wikipedia.
- **Git/GitHub** : Commits, .gitignore, synchronisation avec VS Code.
- **Architecture** : Organisation modulaire avec dossiers (`scripts/`, `source/`).
- **Apprentissage** : Gestion des erreurs HTTP, authentification GitHub, structure de projet pro.

## Installation

1. **Prérequis** : Python 3.8+, pip.
2. Clonez le dépôt :

   ```bash
   git clone https://github.com/Komaraa/word-translation-project.git
   ```

3.Installez les dépendances:

```bash
pip install -r requirements.txt
```

## Utilisation

- Scraper les mots français :

```bash
python scripts/ScrapingToutFrancais.py
```

Sortie : source/french_words.txt (mot uniques)

- Traduire en anglais / en francais :

```bash
python scripts/translate.py
```

Sortie: translation_lot_X.csv (lots) et translations.csv (global).

## Structure du dépôt

- scripts/ : Scripts Python (translate.py, scrape_words.py).
- source/ : Données brutes (ignorées via .gitignore).
- requirements.txt : Dépendances du projet.
- .gitignore : Exclut les fichiers temporaires et données.
- README.md : Documentation du projet.

Cette structure est conçue pour être modulaire et propre, avec des données brutes séparées du code pour un dépôt léger.

## Progrès

- [x] Scraper les mots anglais depuis Simple Wikipedia.
- [x] Traduire par lots de 3,799 mots avec GoogleTranslator.
- [x] Sauvegarder les traductions en CSV avec pandas.
- [] Comparer les mots anglais/français avec Jaro-Winkler ou Levenshtein.
- [] Ajouter des tests unitaires dans tests/.

## Contact 
- GitHub:[Komara](https://github.com/Komaraa)
- Email: [steve.haidara@gmail.com]