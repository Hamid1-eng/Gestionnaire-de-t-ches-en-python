"""Tests simples du gestionnaire de taches."""

# `json` sert ici a fabriquer un exemple de fichier JSON pour un test.
import json
# `tempfile` cree un dossier temporaire qui sera supprime automatiquement.
import tempfile
# `unittest` est la bibliotheque standard de Python pour ecrire des tests.
import unittest
# `Path` represente proprement le chemin du fichier temporaire.
from pathlib import Path

# On importe uniquement les fonctions que l'on veut tester.
from debut import (
    ajouter_tache,
    charger_taches,
    supprimer_tache,
    terminer_tache,
)


class TestGestionnaireTaches(unittest.TestCase):
    """Verifie les comportements principaux de l'application."""

    def test_ajouter_tache(self):
        # On prepare une liste vide, comme au premier demarrage de l'application.
        taches = []

        # On execute la fonction a tester.
        tache = ajouter_tache(taches, "Apprendre les listes")

        # `assertEqual` verifie que deux valeurs sont identiques.
        self.assertEqual(tache["id"], 1)
        self.assertEqual(tache["titre"], "Apprendre les listes")
        # `assertFalse` verifie qu'une valeur est fausse.
        self.assertFalse(tache["terminee"])

    def test_terminer_tache_existante(self):
        # Cette tache existe deja et n'est pas terminee.
        taches = [{"id": 1, "titre": "Lire", "terminee": False}]

        # La fonction doit trouver la tache et modifier son etat.
        resultat = terminer_tache(taches, 1)

        # On verifie le resultat de la fonction et la modification de la liste.
        self.assertTrue(resultat)
        self.assertTrue(taches[0]["terminee"])

    def test_supprimer_tache_inexistante(self):
        # La liste contient seulement la tache numero 1.
        taches = [{"id": 1, "titre": "Lire", "terminee": False}]

        # L'identifiant 99 n'existe pas : rien ne doit etre supprime.
        resultat = supprimer_tache(taches, 99)

        self.assertFalse(resultat)
        # La liste doit toujours contenir une tache.
        self.assertEqual(len(taches), 1)

    def test_charger_taches(self):
        # `TemporaryDirectory` prepare un dossier de test, puis le nettoie.
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "taches.json"
            # On ecrit un exemple de donnees dans le fichier temporaire.
            chemin.write_text(
                json.dumps([{"id": 1, "titre": "Tester", "terminee": True}]),
                encoding="utf-8",
            )

            # On utilise la fonction reelle pour relire ce fichier.
            taches = charger_taches(chemin)

        # On verifie que les donnees ont ete correctement relues.
        self.assertEqual(taches[0]["titre"], "Tester")
        self.assertTrue(taches[0]["terminee"])


# Ce bloc lance les tests si on execute directement `py test_debut.py`.
if __name__ == "__main__":
    unittest.main()