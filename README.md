# Mon gestionnaire de taches

Un petit projet Python pour apprendre les bases en construisant une application utile.

L'application permet de :

- ajouter une tache ;
- afficher les taches ;
- marquer une tache comme terminee ;
- supprimer une tache ;
- sauvegarder les donnees dans un fichier JSON.

## Prerequis

- Python 3.10 ou une version plus recente.
- Aucune bibliotheque externe n'est necessaire.

## Lancer le projet

Depuis ce dossier, execute :

```powershell
python debut.py
```

Sur certains ordinateurs Windows, cette commande peut etre necessaire :

```powershell
py debut.py
```

Un fichier `taches.json` sera cree automatiquement apres la premiere sauvegarde.

## Lancer les tests

```powershell
python -m unittest -v test_debut.py
```

## Organisation du code

- `debut.py` contient l'application complete et ses commentaires pedagogiques.
- `test_debut.py` contient des tests simples pour verifier les fonctions principales.
- `taches.json` est cree automatiquement pour conserver les taches entre deux executions.

## Notions Python pratiquees

- variables, listes et dictionnaires ;
- fonctions et valeurs de retour ;
- boucles et conditions ;
- exceptions avec `try` et `except` ;
- lecture et ecriture de fichiers ;
- format JSON avec le module standard `json` ;
- point d'entree avec `if __name__ == "__main__"` ;
- tests avec le module standard `unittest`.

Pour approfondir, consulte la documentation officielle :

- https://docs.python.org/fr/3/tutorial/
- https://docs.python.org/fr/3/library/json.html
- https://docs.python.org/fr/3/library/unittest.html
