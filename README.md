# Gestionnaire de taches en Python

## Presentation

Ce projet est une application en ligne de commande qui permet de gerer une
liste de taches. Il a ete realise pour mettre en pratique les bases de Python
au travers d'une application concrete, simple a utiliser et facile a faire
evoluer.

Les taches sont conservees dans un fichier JSON : elles restent donc
disponibles apres la fermeture puis le redemarrage du programme.

## Fonctionnalites

L'application permet de :

- afficher toutes les taches et leur etat ;
- ajouter une tache avec un identifiant genere automatiquement ;
- refuser un titre vide ;
- marquer une tache comme terminee ;
- supprimer une tache ;
- sauvegarder automatiquement chaque modification dans `taches.json` ;
- gerer les identifiants inexistants et les saisies qui ne sont pas des nombres ;
- demarrer avec une liste vide si le fichier JSON est absent, invalide ou inaccessible.

Chaque tache est representee par trois informations :

```json
{
		"id": 1,
		"titre": "Apprendre Python",
		"terminee": false
}
```

## Prerequis

- Python 3.10 ou une version plus recente ;
- aucune bibliotheque externe : le projet utilise uniquement la bibliotheque
	standard de Python.

## Installation et lancement

1. Ouvrir un terminal dans le dossier du projet.
2. Lancer l'application avec l'une des commandes suivantes :

```powershell
python debut.py
```

Sous Windows, cette variante peut aussi etre utilisee :

```powershell
py debut.py
```

Le menu propose les actions suivantes :

```text
1. Afficher les taches
2. Ajouter une tache
3. Terminer une tache
4. Supprimer une tache
5. Quitter
```

Le fichier `taches.json` est cree ou mis a jour automatiquement lors d'une
ajout, d'une terminaison ou d'une suppression.

## Exemple d'utilisation

```text
=== Mon gestionnaire de taches ===
1. Afficher les taches
2. Ajouter une tache
3. Terminer une tache
4. Supprimer une tache
5. Quitter
Ton choix : 2
Titre de la nouvelle tache : Relire mon cours Python
Tache 2 ajoutee.
```

Une tache terminee est affichee avec le symbole `x` :

```text
[x] 1 - Nouveau cours en python
[ ] 2 - Relire mon cours Python
```

## Organisation du projet

| Fichier | Role |
| --- | --- |
| `debut.py` | Application principale et fonctions de gestion des taches. |
| `test_debut.py` | Tests unitaires des fonctions principales. |
| `taches.json` | Donnees sauvegardees entre les executions. |
| `README.md` | Documentation du projet. |

## Fonctionnement technique

Le programme est organise autour de fonctions courtes et specialisees :

- `charger_taches()` lit le fichier JSON et retourne une liste de taches ;
- `sauvegarder_taches()` ecrit la liste dans le fichier JSON ;
- `ajouter_tache()` cree une tache et lui attribue un nouvel identifiant ;
- `terminer_tache()` modifie l'etat d'une tache ;
- `supprimer_tache()` retire une tache de la liste ;
- `afficher_taches()` presente les taches dans le terminal ;
- `lancer_application()` gere la boucle principale et le menu.

Le chemin de `taches.json` est construit avec `pathlib` a partir du dossier de
`debut.py`. L'application peut ainsi etre lancee depuis un autre dossier sans
perdre le fichier de donnees.

## Lancer les tests

Pour executer les tests avec des informations detaillees :

```powershell
python -m unittest -v test_debut.py
```

Les tests verifient notamment :

- l'ajout d'une tache avec les bonnes valeurs ;
- la terminaison d'une tache existante ;
- le comportement lorsqu'une tache a supprimer n'existe pas ;
- la lecture de taches depuis un fichier JSON temporaire.

Les tests utilisent un dossier temporaire afin de ne pas modifier le vrai
fichier `taches.json`.

## Ce que j'ai appris

Ce projet m'a permis de pratiquer :

- les variables, listes, dictionnaires et chaines de caracteres ;
- les fonctions, les parametres et les valeurs de retour ;
- les conditions, les boucles et les comprehensions ;
- la validation des saisies utilisateur ;
- la lecture et l'ecriture de fichiers avec `with` ;
- la manipulation des chemins avec `pathlib.Path` ;
- la conversion de donnees avec le module `json` ;
- la gestion des erreurs avec `try` et `except` ;
- les f-strings pour afficher des informations dynamiques ;
- le point d'entree `if __name__ == "__main__"` ;
- l'ecriture de tests avec le module `unittest`.

## Limites actuelles

- l'application fonctionne uniquement dans le terminal ;
- les taches ne possedent pas encore de date, de priorite ou de categorie ;
- il n'est pas possible de modifier le titre d'une tache existante ;
- les tests ne couvrent pas encore tous les cas d'erreur, comme un JSON invalide.

## Pistes d'amelioration

- ajouter la modification d'une tache ;
- filtrer les taches par etat ;
- ajouter des priorites, des categories et des dates limites ;
- renforcer la validation et la structure des donnees JSON ;
- completer la couverture de tests ;
- separer davantage la logique metier et l'interface utilisateur ;
- creer une interface graphique ou une API.

## Ressources

- [Tutoriel officiel Python](https://docs.python.org/fr/3/tutorial/)
- [Documentation du module JSON](https://docs.python.org/fr/3/library/json.html)
- [Documentation du module unittest](https://docs.python.org/fr/3/library/unittest.html)
