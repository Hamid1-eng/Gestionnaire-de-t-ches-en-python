"""Gestionnaire de taches en ligne de commande.

Ce fichier est volontairement autonome afin de rester facile a lire quand on
debute en Python. Les donnees sont conservees dans un fichier JSON.
"""

# `json` permet de transformer des donnees Python en texte JSON et inversement.
import json
# `Path` facilite la manipulation des chemins de fichiers.
from pathlib import Path


# `__file__` contient le chemin de ce fichier Python.
# `.parent` recupere son dossier.
# `/ "taches.json"` construit le chemin du fichier de sauvegarde.
# Cette constante evite de repeter le meme chemin dans tout le programme.
FICHIER_TACHES = Path(__file__).parent / "taches.json"


def charger_taches(chemin=FICHIER_TACHES):
	"""Lit les taches depuis un fichier JSON.

	Si le fichier n'existe pas encore ou s'il est invalide, on commence avec
	une liste vide afin que l'application puisse quand meme demarrer.
	"""
	# Si le fichier n'existe pas, il n'y a encore aucune tache a charger.
	if not chemin.exists():
		return []

	try:
		# `with` ouvre le fichier et le referme automatiquement a la fin du bloc.
		# Le mode "r" signifie "read", c'est-a-dire lecture.
		with chemin.open("r", encoding="utf-8") as fichier:
			# `json.load` lit le texte JSON et le transforme en liste Python.
			donnees = json.load(fichier)
	except (json.JSONDecodeError, OSError):
		# JSONDecodeError signifie que le contenu n'est pas un JSON valide.
		# OSError couvre un probleme d'acces au fichier.
		# Dans les deux cas, on prefere demarrer avec une liste vide.
		return []

	# `isinstance` verifie le type de la valeur.
	# L'application attend une liste, par exemple [{"id": 1, ...}].
	if isinstance(donnees, list):
		return donnees
	# Si le JSON contient autre chose qu'une liste, on ignore son contenu.
	return []


def sauvegarder_taches(taches, chemin=FICHIER_TACHES):
	"""Enregistre les taches dans un fichier JSON lisible."""
	try:
		# Le mode "w" signifie "write", c'est-a-dire ecriture.
		with chemin.open("w", encoding="utf-8") as fichier:
			# `json.dump` transforme la liste Python en texte JSON.
			# `indent=4` ajoute une indentation pour rendre le fichier lisible.
			json.dump(taches, fichier, ensure_ascii=False, indent=4)
	except OSError as erreur:
		# Si l'ecriture echoue, on affiche la raison sans arreter brutalement le programme.
		print(f"Impossible de sauvegarder les taches : {erreur}")


def ajouter_tache(taches, titre):
	"""Ajoute une nouvelle tache et renvoie la tache creee."""
	# Un dictionnaire associe une cle (par exemple "titre") a une valeur.
	# Ici, chaque tache possede un identifiant, un titre et un etat.
	nouvelle_tache = {
		# On appelle une fonction pour trouver le prochain identifiant disponible.
		"id": trouver_prochain_id(taches),
		# `strip` retire les espaces inutiles au debut et a la fin du titre.
		"titre": titre.strip(),
		# Une tache nouvellement creee n'est pas encore terminee.
		"terminee": False,
	}
	# `append` ajoute la nouvelle tache a la fin de la liste.
	taches.append(nouvelle_tache)
	# `return` renvoie une valeur a la partie du programme qui a appele la fonction.
	return nouvelle_tache


def trouver_prochain_id(taches):
	"""Retourne un identifiant unique et simple pour la prochaine tache."""
	# Une liste vide ne contient aucun identifiant : le premier sera donc 1.
	if not taches:
		return 1
	# La comprehension recupere tous les identifiants.
	# `max` trouve le plus grand, puis on ajoute 1 pour le nouveau.
	return max(tache["id"] for tache in taches) + 1


def terminer_tache(taches, identifiant):
	"""Marque une tache comme terminee et renvoie True si elle existe."""
	# `for` parcourt les taches une par une.
	for tache in taches:
		# On compare l'identifiant recherche avec celui de la tache actuelle.
		if tache["id"] == identifiant:
			# On modifie la valeur associee a la cle "terminee".
			tache["terminee"] = True
			# `True` indique que la tache a bien ete trouvee.
			return True
	# Si la boucle finit sans trouver l'identifiant, la tache n'existe pas.
	return False


def supprimer_tache(taches, identifiant):
	"""Supprime une tache et renvoie True si elle existe."""
	for tache in taches:
		if tache["id"] == identifiant:
			# `remove` retire cet element precis de la liste.
			taches.remove(tache)
			return True
	return False


def afficher_taches(taches):
	"""Affiche les taches avec un symbole adapte a leur etat."""
	# `not taches` est vrai quand la liste est vide.
	if not taches:
		print("\nAucune tache pour le moment.")
		# `return` arrete cette fonction ici.
		return

	print("\nListe des taches :")
	for tache in taches:
		# Cette expression conditionnelle choisit "x" si la tache est terminee,
		# sinon elle choisit un espace.
		symbole = "x" if tache["terminee"] else " "
		# La f-string insere les valeurs dans le texte affiche.
		print(f"[{symbole}] {tache['id']} - {tache['titre']}")


def demander_identifiant():
	"""Demande un nombre entier a l'utilisateur.

	La boucle continue tant que l'utilisateur ne fournit pas un entier valide.
	"""
	while True:
		# `input` affiche une question et recupere une reponse sous forme de texte.
		valeur = input("Identifiant de la tache : ").strip()
		try:
			# `int` transforme le texte en nombre entier.
			return int(valeur)
		except ValueError:
			# Cette erreur arrive si l'utilisateur saisit par exemple "abc".
			# La boucle recommence alors avec une nouvelle question.
			print("Entre un nombre entier, par exemple 1.")


def afficher_menu():
	"""Affiche les choix possibles et renvoie le choix de l'utilisateur."""
	# Chaque `print` affiche une ligne dans le terminal.
	print("\n=== Mon gestionnaire de taches ===")
	print("1. Afficher les taches")
	print("2. Ajouter une tache")
	print("3. Terminer une tache")
	print("4. Supprimer une tache")
	print("5. Quitter")
	# Le choix est recupere comme texte, meme si l'utilisateur saisit un nombre.
	return input("Ton choix : ").strip()


def lancer_application():
	"""Lance la boucle principale de l'application."""
	# Au demarrage, on recupere les anciennes taches du fichier JSON.
	taches = charger_taches()

	# `while True` repete le menu jusqu'a l'execution de `break`.
	while True:
		choix = afficher_menu()

		# Chaque branche correspond a une option du menu.
		if choix == "1":
			afficher_taches(taches)
		elif choix == "2":
			# On demande le titre et on retire les espaces inutiles.
			titre = input("Titre de la nouvelle tache : ").strip()
			if titre:
				# Un titre non vide est ajoute, puis la liste est sauvegardee.
				tache = ajouter_tache(taches, titre)
				sauvegarder_taches(taches)
				print(f"Tache {tache['id']} ajoutee.")
			else:
				# Une chaine vide est consideree comme une saisie invalide.
				print("Le titre ne peut pas etre vide.")
		elif choix == "3":
			identifiant = demander_identifiant()
			if terminer_tache(taches, identifiant):
				# On sauvegarde uniquement si une modification a vraiment eu lieu.
				sauvegarder_taches(taches)
				print("Tache terminee.")
			else:
				print("Cette tache n'existe pas.")
		elif choix == "4":
			identifiant = demander_identifiant()
			if supprimer_tache(taches, identifiant):
				# La suppression est conservee dans le fichier JSON.
				sauvegarder_taches(taches)
				print("Tache supprimee.")
			else:
				print("Cette tache n'existe pas.")
		elif choix == "5":
			print("A bientot !")
			# `break` sort de la boucle `while` et termine l'application.
			break
		else:
			# Cette branche gere tous les choix qui ne sont pas compris entre 1 et 5.
			print("Choix invalide : selectionne un nombre de 1 a 5.")


# Cette condition evite de lancer l'application quand le fichier est importe
# par les tests ou par un autre programme.
if __name__ == "__main__":
	lancer_application()



