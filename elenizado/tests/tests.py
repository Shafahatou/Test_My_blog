from django.test import TestCase
from django.utils import timezone
from elenizado.models import Categorie, Publication, Commentaire, ReponseCommentaire, Like, Evenement, Cours, Textes, Video

class CategorieTestCase(TestCase):
    def setUp(self):
        """Créer une catégorie pour les tests"""
        self.categorie = Categorie.objects.create(nom="Test Categorie", description="Une description de test")
    
    def test_categorie_creation(self):
        """Tester la création d'une catégorie"""
        self.assertEqual(self.categorie.nom, "Test Categorie")
        self.assertTrue(self.categorie.status)
    
    def test_categorie_str(self):
        """Tester la méthode __str__"""
        self.assertEqual(str(self.categorie), "Test Categorie")


class PublicationTestCase(TestCase):
    def setUp(self):
        """Créer une publication et une catégorie associée"""
        self.categorie = Categorie.objects.create(nom="Test Categorie", description="Une description de test")
        self.publication = Publication.objects.create(
            titre="Test Publication", 
            description="<p>Contenu de test</p>", 
            categorie=self.categorie
        )
    
    def test_publication_creation(self):
        """Tester la création d'une publication"""
        self.assertEqual(self.publication.titre, "Test Publication")
        self.assertEqual(self.publication.categorie, self.categorie)
    
    def test_publication_slug(self):
        """Tester que le slug est généré automatiquement"""
        self.assertIsNotNone(self.publication.slug)
    
    def test_publication_str(self):
        """Tester la méthode __str__"""
        self.assertEqual(str(self.publication), "Test Publication")


class CommentaireTestCase(TestCase):
    def setUp(self):
        """Créer un commentaire associé à une publication"""
        self.categorie = Categorie.objects.create(nom="Test Categorie", description="Une description de test")
        self.publication = Publication.objects.create(
            titre="Test Publication", 
            description="<p>Contenu de test</p>", 
            categorie=self.categorie
        )
        self.commentaire = Commentaire.objects.create(
            publication=self.publication,
            nom="Test User",
            email="testuser@example.com",
            commentaire="Ceci est un test"
        )
    
    def test_commentaire_creation(self):
        """Tester la création d'un commentaire"""
        self.assertEqual(self.commentaire.nom, "Test User")
        self.assertEqual(self.commentaire.commentaire, "Ceci est un test")
        self.assertEqual(self.commentaire.publication, self.publication)
    
    def test_commentaire_str(self):
        """Tester la méthode __str__"""
        self.assertEqual(str(self.commentaire), "Test User")


class ReponseCommentaireTestCase(TestCase):
    def setUp(self):
        """Créer une réponse à un commentaire"""
        self.categorie = Categorie.objects.create(nom="Test Categorie", description="Une description de test")
        self.publication = Publication.objects.create(
            titre="Test Publication", 
            description="<p>Contenu de test</p>", 
            categorie=self.categorie
        )
        self.commentaire = Commentaire.objects.create(
            publication=self.publication,
            nom="Test User",
            email="testuser@example.com",
            commentaire="Ceci est un test"
        )
        self.reponse_commentaire = ReponseCommentaire.objects.create(
            commentaire=self.commentaire,
            nom="Test Admin",
            email="testadmin@example.com",
            reponse="Réponse au commentaire"
        )
    
    def test_reponse_creation(self):
        """Tester la création d'une réponse"""
        self.assertEqual(self.reponse_commentaire.nom, "Test Admin")
        self.assertEqual(self.reponse_commentaire.reponse, "Réponse au commentaire")
        self.assertEqual(self.reponse_commentaire.commentaire, self.commentaire)
    
    def test_reponse_str(self):
        """Tester la méthode __str__"""
        self.assertEqual(str(self.reponse_commentaire), "Test Admin")


class LikeTestCase(TestCase):
    def setUp(self):
        """Créer un like pour une publication"""
        self.categorie = Categorie.objects.create(nom="Test Categorie", description="Une description de test")
        self.publication = Publication.objects.create(
            titre="Test Publication", 
            description="<p>Contenu de test</p>", 
            categorie=self.categorie
        )
        self.like = Like.objects.create(publication=self.publication)
    
    def test_like_creation(self):
        """Tester la création d'un like"""
        self.assertEqual(self.like.publication, self.publication)
    
    def test_like_str(self):
        """Tester la méthode __str__"""
        self.assertEqual(str(self.like), "Test Publication")


class EvenementTestCase(TestCase):
    def setUp(self):
        """Créer un événement"""
        self.evenement = Evenement.objects.create(
            titre="Test Evenement", 
            description="<p>Description de test d'événement</p>"
        )
    
    def test_evenement_creation(self):
        """Tester la création d'un événement"""
        self.assertEqual(self.evenement.titre, "Test Evenement")
    
    def test_evenement_slug(self):
        """Tester que le slug est généré automatiquement"""
        self.assertIsNotNone(self.evenement.slug)
    
    def test_evenement_str(self):
        """Tester la méthode __str__"""
        self.assertEqual(str(self.evenement), "Test Evenement")


class CoursTestCase(TestCase):
    def setUp(self):
        """Créer un cours"""
        self.cours = Cours.objects.create(
            titre="Test Cours", 
            niveau="Niveau 1", 
            annee=2024, 
            description="Description du cours"
        )
    
    def test_cours_creation(self):
        """Tester la création d'un cours"""
        self.assertEqual(self.cours.titre, "Test Cours")
        self.assertEqual(self.cours.niveau, "Niveau 1")
        self.assertEqual(self.cours.annee, 2024)
    
    def test_cours_str(self):
        """Tester la méthode __str__"""
        self.assertEqual(str(self.cours), "Test Cours")


class VideoTestCase(TestCase):
    def setUp(self):
        """Créer une vidéo"""
        self.video = Video.objects.create(
            titre="Test Vidéo", 
            description="Description de test de vidéo", 
            video="https://www.youtube.com/watch?v=12345"
        )
    
    def test_video_creation(self):
        """Tester la création d'une vidéo"""
        self.assertEqual(self.video.titre, "Test Vidéo")
    
    def test_video_str(self):
        """Tester la méthode __str__"""
        self.assertEqual(str(self.video), "Test Vidéo")
    
    def test_get_video(self):
        """Tester la méthode get_video pour extraire l'ID de la vidéo"""
        self.assertEqual(self.video.get_video, "12345")

