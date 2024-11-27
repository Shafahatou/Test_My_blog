from django.test import TestCase

import pytest
from django.test import Client
from django.urls import reverse
from oeuvre.models import MyModel # Remplacez par vos modèles
from oeuvre.forms import MyModelForm  # Remplacez par vos formulaires
from django.db.utils import IntegrityError


@pytest.mark.django_db
def test_model_creation():
    """Test unitaire pour la création d'un modèle valide."""
    obj = MyModel.objects.create(
        name="Test Name",
        description="Test description",
        status=True
    )
    assert obj.name == "Test Name"
    assert obj.description == "Test description"
    assert obj.status is True


@pytest.mark.django_db
def test_model_str():
    """Test unitaire pour la méthode __str__ d'un modèle."""
    obj = MyModel.objects.create(
        name="Readable Name",
        description="Another description",
        status=True
    )
    assert str(obj) == "Readable Name"


@pytest.mark.django_db
def test_model_missing_required_field():
    """Test unitaire pour vérifier les erreurs d'intégrité."""
    with pytest.raises(IntegrityError):
        MyModel.objects.create(description="Missing name")


@pytest.mark.django_db
def test_valid_form():
    """Test unitaire pour un formulaire valide."""
    form_data = {
        "name": "Valid Name",
        "description": "Valid Description",
        "status": True
    }
    form = MyModelForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
def test_invalid_form():
    """Test unitaire pour un formulaire invalide."""
    form_data = {
        "name": "",  # Nom manquant
        "description": "Invalid without name",
        "status": True
    }
    form = MyModelForm(data=form_data)
    assert not form.is_valid()


@pytest.mark.django_db
def test_view_model_list():
    """Test unitaire pour la vue liste."""
    client = Client()
    MyModel.objects.create(
        name="Test Entry",
        description="Test Description",
        status=True
    )
    response = client.get(reverse("app_name:model_list"))  # Remplacez avec votre nom d'URL
    assert response.status_code == 200
    assert "Test Entry" in response.content.decode()


@pytest.mark.django_db
def test_view_model_detail():
    """Test unitaire pour la vue détail."""
    client = Client()
    obj = MyModel.objects.create(
        name="Test Entry",
        description="Test Description",
        status=True
    )
    response = client.get(reverse("app_name:model_detail", args=[obj.id]))  # Remplacez avec votre nom d'URL
    assert response.status_code == 200
    assert "Test Description" in response.content.decode()
