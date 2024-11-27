from django.test import TestCase

import pytest
from django.core.exceptions import ValidationError
from about.models import Curriculum, Contact, Prestation, Presentation, Gallerie

@pytest.mark.django_db
class TestCurriculum:
    def test_curriculum_creation(self):
        curriculum = Curriculum.objects.create(
            photo='images/curriculum/photo.jpg',
            nom='John Doe',
            description='<p>Développeur Django</p>',
            cv='cv/curriculum/cv.pdf',
            status=True
        )
        assert curriculum.nom == 'John Doe'
        assert curriculum.description == '<p>Développeur Django</p>'
        assert curriculum.status is True

    def test_curriculum_str(self):
        curriculum = Curriculum.objects.create(
            nom='John Doe',
            description='<p>Développeur Django</p>',
            cv='cv/curriculum/cv.pdf',
            photo='images/curriculum/photo.jpg',
            status=True
        )
        assert str(curriculum) == 'John Doe'


@pytest.mark.django_db
class TestContact:
    def test_contact_creation(self):
        contact = Contact.objects.create(
            nom='Jane Smith',
            email='jane@example.com',
            subject='Question',
            telephone=123456789,
            message='I have a question about your service.',
            status=True
        )
        assert contact.nom == 'Jane Smith'
        assert contact.email == 'jane@example.com'
        assert contact.subject == 'Question'
        assert contact.telephone == 123456789
        assert contact.status is True

    def test_contact_str(self):
        contact = Contact.objects.create(
            nom='Jane Smith',
            email='jane@example.com',
            subject='Question',
            telephone=123456789,
            message='I have a question about your service.',
            status=True
        )
        assert str(contact) == 'Jane Smith'


@pytest.mark.django_db
class TestPrestation:
    def test_prestation_creation(self):
        prestation = Prestation.objects.create(
            titre='Web Development',
            description='Full-stack web development service.',
            image='images/prestations/service.jpg',
            status=True
        )
        assert prestation.titre == 'Web Development'
        assert prestation.description == 'Full-stack web development service.'
        assert prestation.status is True

    def test_prestation_str(self):
        prestation = Prestation.objects.create(
            titre='Web Development',
            description='Full-stack web development service.',
            image='images/prestations/service.jpg',
            status=True
        )
        assert str(prestation) == 'Web Development'


@pytest.mark.django_db
class TestPresentation:
    def test_presentation_creation(self):
        presentation = Presentation.objects.create(
            titre='About Us',
            description='<p>We are a web development company.</p>',
            image='image/presentation/about_us.jpg',
            status=True
        )
        assert presentation.titre == 'About Us'
        assert presentation.description == '<p>We are a web development company.</p>'
        assert presentation.status is True

    def test_presentation_str(self):
        presentation = Presentation.objects.create(
            titre='About Us',
            description='<p>We are a web development company.</p>',
            image='image/presentation/about_us.jpg',
            status=True
        )
        assert str(presentation) == 'About Us'


@pytest.mark.django_db
class TestGallerie:
    def test_gallerie_creation(self):
        gallerie = Gallerie.objects.create(
            titre='Beautiful Photos',
            gallerie='gallerie/image/photo1.jpg',
            status=True
        )
        assert gallerie.titre == 'Beautiful Photos'
        assert gallerie.status is True

    def test_gallerie_str(self):
        gallerie = Gallerie.objects.create(
            titre='Beautiful Photos',
            gallerie='gallerie/image/photo1.jpg',
            status=True
        )
        assert str(gallerie) == 'Beautiful Photos'

