import pytest
from django.test import TestCase
from oeuvre.models import Poesie

class IntegrationTestPoesie(TestCase):
    def setUp(self):
        """Prépare les données nécessaires pour les tests."""
        self.poesie_data = {
            "titre": "Le Voyage",
            "description": "Un poème sur le voyage et l'aventure.",
            "poeme": "<p>Le voyage est une aventure,<br>Qui mène vers de nouvelles découvertes.</p>",
            "status": True,
        }

    def test_poesie_creation(self):
        """Test de création pour le modèle Poesie."""
        poesie = Poesie.objects.create(**self.poesie_data)
        self.assertEqual(Poesie.objects.count(), 1)
        self.assertEqual(poesie.titre, "Le Voyage")
        self.assertTrue(poesie.status)
        self.assertEqual(poesie.description, "Un poème sur le voyage et l'aventure.")
        self.assertIn("<p>Le voyage est une aventure", poesie.poeme)

    def test_poesie_update(self):
        """Test de mise à jour pour le modèle Poesie."""
        poesie = Poesie.objects.create(**self.poesie_data)
        poesie.titre = "Le Voyage à Paris"
        poesie.save()
        updated_poesie = Poesie.objects.get(id=poesie.id)
        self.assertEqual(updated_poesie.titre, "Le Voyage à Paris")

    def test_poesie_deletion(self):
        """Test de suppression pour le modèle Poesie."""
        poesie = Poesie.objects.create(**self.poesie_data)
        self.assertEqual(Poesie.objects.count(), 1)
        poesie.delete()
        self.assertEqual(Poesie.objects.count(), 0)

    def test_poesie_status(self):
        """Test pour vérifier que l'attribut status fonctionne correctement."""
        poesie = Poesie.objects.create(**self.poesie_data)
        self.assertTrue(poesie.status)
        poesie.status = False
        poesie.save()
        updated_poesie = Poesie.objects.get(id=poesie.id)
        self.assertFalse(updated_poesie.status)
