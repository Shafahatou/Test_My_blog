import pytest
from about.models import Curriculum, Contact, Prestation, Presentation, Gallerie
from django.db import IntegrityError

@pytest.mark.django_db
class TestIntegration:
    
    def test_create_curriculum_and_contact(self):
        curriculum = Curriculum.objects.create(
            photo='images/curriculum/photo.jpg',
            nom='John Doe',
            description='<p>Développeur Django</p>',
            cv='cv/curriculum/cv.pdf',
            status=True
        )
        contact = Contact.objects.create(
            nom='Jane Smith',
            email='jane@example.com',
            subject='Question',
            telephone=123456789,
            message='I have a question about your service.',
            status=True
        )

        # Vérification de la création des objets
        assert Curriculum.objects.count() == 1
        assert Contact.objects.count() == 1
        assert contact.email == 'jane@example.com'

    def test_create_prestation_and_presentation(self):
        prestation = Prestation.objects.create(
            titre='Web Development',
            description='Full-stack web development service.',
            image='images/prestations/service.jpg',
            status=True
        )
        presentation = Presentation.objects.create(
            titre='About Us',
            description='<p>We are a web development company.</p>',
            image='image/presentation/about_us.jpg',
            status=True
        )

        # Vérification de la création des objets
        assert Prestation.objects.count() == 1
        assert Presentation.objects.count() == 1
        assert prestation.titre == 'Web Development'

    def test_create_gallerie_and_verify(self):
        gallerie = Gallerie.objects.create(
            titre='Beautiful Photos',
            gallerie='gallerie/image/photo1.jpg',
            status=True
        )
        
        # Vérification de la création de l'objet gallerie
        assert Gallerie.objects.count() == 1
        assert gallerie.titre == 'Beautiful Photos'

    def test_integrity_error_on_missing_required_fields(self):
        with pytest.raises(IntegrityError):
            Curriculum.objects.create(
                nom='John Doe',
                description='<p>Développeur Django</p>',
                cv='cv/curriculum/cv.pdf',
                status=True
            )
