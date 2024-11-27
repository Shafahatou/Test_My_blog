import pytest
from django.utils.text import slugify
from datetime import datetime
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video
from django.test import TestCase


class CategorieIntegrationTest(TestCase):
    def setUp(self):
        """Créer une catégorie pour les tests."""
        self.categorie = Categorie.objects.create(
            nom="Sport",
            description="Catégorie liée au sport",
            status=True
        )

    def test_create_categorie(self):
        """Vérifie que la catégorie est créée avec succès."""
        self.assertEqual(Categorie.objects.count(), 1)
        self.assertEqual(self.categorie.nom, "Sport")

    def test_update_categorie(self):
        """Vérifie que la catégorie peut être mise à jour."""
        self.categorie.nom = "Culture"
        self.categorie.save()
        self.assertEqual(Categorie.objects.first().nom, "Culture")


class PublicationIntegrationTest(TestCase):
    def setUp(self):
        """Créer une catégorie et une publication pour les tests."""
        self.categorie = Categorie.objects.create(
            nom="Actualités",
            description="Catégorie d'actualités",
            status=True
        )
        self.publication = Publication.objects.create(
            titre="Nouvelle publication",
            description="Description de la publication",
            categorie=self.categorie,
            image="image.png",
            status=True
        )

    def test_create_publication(self):
        """Vérifie que la publication est créée avec succès."""
        self.assertEqual(Publication.objects.count(), 1)
        self.assertEqual(self.publication.titre, "Nouvelle publication")

    def test_slug_creation(self):
        """Vérifie que le slug est généré automatiquement."""
        self.assertIsNotNone(self.publication.slug)

    def test_update_publication(self):
        """Vérifie que la publication peut être mise à jour."""
        self.publication.titre = "Titre modifié"
        self.publication.save()
        self.assertEqual(Publication.objects.first().titre, "Titre modifié")


class CommentaireIntegrationTest(TestCase):
    def setUp(self):
        """Créer une publication et un commentaire pour les tests."""
        self.categorie = Categorie.objects.create(
            nom="Blog",
            description="Catégorie de blog",
            status=True
        )
        self.publication = Publication.objects.create(
            titre="Article",
            description="Un article intéressant",
            categorie=self.categorie,
            image="image.png",
            status=True
        )
        self.commentaire = Commentaire.objects.create(
            publication=self.publication,
            nom="Jean Dupont",
            email="jean@example.com",
            commentaire="Très intéressant !",
            status=True
        )

    def test_create_commentaire(self):
        """Vérifie que le commentaire est créé avec succès."""
        self.assertEqual(Commentaire.objects.count(), 1)
        self.assertEqual(self.commentaire.nom, "Jean Dupont")

    def test_association_commentaire_publication(self):
        """Vérifie que le commentaire est associé à la bonne publication."""
        self.assertEqual(self.commentaire.publication.titre, "Article")


class ReponseCommentaireIntegrationTest(TestCase):
    def setUp(self):
        """Créer un commentaire et une réponse pour les tests."""
        self.categorie = Categorie.objects.create(
            nom="Blog",
            description="Catégorie de blog",
            status=True
        )
        self.publication = Publication.objects.create(
            titre="Article",
            description="Un article intéressant",
            categorie=self.categorie,
            image="image.png",
            status=True
        )
        self.commentaire = Commentaire.objects.create(
            publication=self.publication,
            nom="Jean Dupont",
            email="jean@example.com",
            commentaire="Très intéressant !",
            status=True
        )
        self.reponse = ReponseCommentaire.objects.create(
            commentaire=self.commentaire,
            nom="Admin",
            email="admin@example.com",
            reponse="Merci pour votre retour !",
            status=True
        )

    def test_create_reponse(self):
        """Vérifie que la réponse est créée avec succès."""
        self.assertEqual(ReponseCommentaire.objects.count(), 1)
        self.assertEqual(self.reponse.nom, "Admin")


class LikeIntegrationTest(TestCase):
    def setUp(self):
        """Créer une publication et un like pour les tests."""
        self.categorie = Categorie.objects.create(
            nom="Blog",
            description="Catégorie de blog",
            status=True
        )
        self.publication = Publication.objects.create(
            titre="Article",
            description="Un article intéressant",
            categorie=self.categorie,
            image="image.png",
            status=True
        )
        self.like = Like.objects.create(publication=self.publication)

    def test_create_like(self):
        """Vérifie que le like est créé avec succès."""
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(self.like.publication.titre, "Article")


class EvenementIntegrationTest(TestCase):
    def setUp(self):
        """Créer un événement pour les tests."""
        self.evenement = Evenement.objects.create(
            titre="Conférence Django",
            description="Une conférence sur Django",
            image="conference.png",
            status=True
        )

    def test_create_evenement(self):
        """Vérifie que l'événement est créé avec succès."""
        self.assertEqual(Evenement.objects.count(), 1)
        self.assertEqual(self.evenement.titre, "Conférence Django")


class CoursIntegrationTest(TestCase):
    def setUp(self):
        """Créer un cours pour les tests."""
        self.cours = Cours.objects.create(
            titre="Apprendre Django",
            niveau="Débutant",
            annee=2024,
            description="Un cours pour apprendre Django",
            cours="cours.pdf",
            image="cours.png",
            status=True
        )

    def test_create_cours(self):
        """Vérifie que le cours est créé avec succès."""
        self.assertEqual(Cours.objects.count(), 1)
        self.assertEqual(self.cours.titre, "Apprendre Django")


class TextesIntegrationTest(TestCase):
    def setUp(self):
        """Créer un texte de référence pour les tests."""
        self.texte = Textes.objects.create(
            titre="Documentation Django",
            description="Documentation officielle de Django",
            pdf="documentation.pdf",
            image="documentation.png",
            status=True
        )

    def test_create_texte(self):
        """Vérifie que le texte est créé avec succès."""
        self.assertEqual(Textes.objects.count(), 1)
        self.assertEqual(self.texte.titre, "Documentation Django")


class VideoIntegrationTest(TestCase):
    def setUp(self):
        """Créer une vidéo pour les tests."""
        self.video = Video.objects.create(
            titre="Tutoriel Django",
            description="Un tutoriel vidéo pour Django",
            video="https://youtu.be/example",
            image="video.png",
            status=True
        )

    def test_create_video(self):
        """Vérifie que la vidéo est créée avec succès."""
        self.assertEqual(Video.objects.count(), 1)
        self.assertEqual(self.video.titre, "Tutoriel Django")
