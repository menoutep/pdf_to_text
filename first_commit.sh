#!/bin/bash

# Récupérer le nom du dossier
nom_dossier=$(basename "$(pwd)")

# Ajouter la ligne au README.md
echo "# $nom_dossier" >> README.md

# Initialiser le dépôt Git

git remote remove origin
git init

# Ajouter et valider les changements
git add .gitignore
git add README.md
git add .
git commit -m "Premier commit"

# Créer une branche principale (main)
git branch -M main

# Ajouter le dépôt distant
git remote add origin https://github.com/menoutep/pdf_to_text.git

# Pousser les changements vers le dépôt distant
git push -u origin main
