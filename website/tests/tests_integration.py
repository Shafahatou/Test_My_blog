import pytest
from django.test import TestCase, Client
from django.urls import reverse
from website.models import SiteInfo, SocialCount, Newsletter

class IntegrationTestModels(TestCase):
    def setUp(self):
        """Prépare les données nécessaires pour les tests."""
        self.site_info_data = {
            "email": "example@site.com",
            "nom": "Test Site",
            "telephone": 123456789,
            "description": "Ceci est un site de test",
            "logo": "path/to/logo.png",
            "status": True,
        }

        self.social_count_data = {
            "nom": "Facebook",
            "lien": "https://facebook.com/test",
            "icones": "facebook",
            "status": True,
        }

        self.newsletter_data = {
            "email": "subscriber@test.com",
            "status": True,
        }

    def test_site_info_creation(self):
        """Test de création pour le modèle SiteInfo."""
        site_info = SiteInfo.objects.create(**self.site_info_data)
        self.assertEqual(SiteInfo.objects.count(), 1)
        self.assertEqual(site_info.nom, "Test Site")
        self.assertTrue(site_info.status)

    def test_social_count_creation(self):
        """Test de création pour le modèle SocialCount."""
        social = SocialCount.objects.create(**self.social_count_data)
        self.assertEqual(SocialCount.objects.count(), 1)
        self.assertEqual(social.nom, "Facebook")
        self.assertEqual(social.icones, "facebook")

    def test_newsletter_creation(self):
        """Test de création pour le modèle Newsletter."""
        newsletter = Newsletter.objects.create(**self.newsletter_data)
        self.assertEqual(Newsletter.objects.count(), 1)
        self.assertEqual(newsletter.email, "subscriber@test.com")

    def test_site_info_update(self):
        """Test de mise à jour pour le modèle SiteInfo."""
        site_info = SiteInfo.objects.create(**self.site_info_data)
        site_info.nom = "Updated Site"
        site_info.save()
        updated_site = SiteInfo.objects.get(id=site_info.id)
        self.assertEqual(updated_site.nom, "Updated Site")

    def test_social_count_deletion(self):
        """Test de suppression pour le modèle SocialCount."""
        social = SocialCount.objects.create(**self.social_count_data)
        self.assertEqual(SocialCount.objects.count(), 1)
        social.delete()
        self.assertEqual(SocialCount.objects.count(), 0)

    def test_newsletter_deletion(self):
        """Test de suppression pour le modèle Newsletter."""
        newsletter = Newsletter.objects.create(**self.newsletter_data)
        self.assertEqual(Newsletter.objects.count(), 1)
        newsletter.delete()
        self.assertEqual(Newsletter.objects.count(), 0)
