import pytest
from django.test import TestCase
from website.models import SiteInfo, SocialCount, Newsletter

# Django TestCase for SiteInfo
class TestSiteInfoModel(TestCase):
    def setUp(self):
        self.site_info = SiteInfo.objects.create(
            email="test@example.com",
            nom="Test Site",
            telephone=123456789,
            description="Description of the site.",
            logo="logo/site/test_logo.png",
            status=True,
        )

    def test_site_info_creation(self):
        self.assertEqual(self.site_info.nom, "Test Site")
        self.assertTrue(self.site_info.status)
        self.assertIsInstance(self.site_info, SiteInfo)

    def test_site_info_str_method(self):
        self.assertEqual(str(self.site_info), "Test Site")


# Django TestCase for SocialCount
class TestSocialCountModel(TestCase):
    def setUp(self):
        self.social_count = SocialCount.objects.create(
            nom="Facebook",
            lien="https://facebook.com",
            icones="facebook",
            status=True,
        )

    def test_social_count_creation(self):
        self.assertEqual(self.social_count.nom, "Facebook")
        self.assertEqual(self.social_count.icones, "facebook")
        self.assertTrue(self.social_count.status)

    def test_social_count_str_method(self):
        self.assertEqual(str(self.social_count), "Facebook")


# Django TestCase for Newsletter
class TestNewsletterModel(TestCase):
    def setUp(self):
        self.newsletter = Newsletter.objects.create(
            email="subscriber@example.com", status=True
        )

    def test_newsletter_creation(self):
        self.assertEqual(self.newsletter.email, "subscriber@example.com")
        self.assertTrue(self.newsletter.status)

    def test_newsletter_str_method(self):
        self.assertEqual(str(self.newsletter), "subscriber@example.com")


# Pytest examples for models
@pytest.mark.django_db
def test_site_info_creation():
    site_info = SiteInfo.objects.create(
        email="pytest@example.com",
        nom="Pytest Site",
        telephone=987654321,
        description="Pytest Description",
        logo="logo/site/pytest_logo.png",
        status=False,
    )
    assert site_info.nom == "Pytest Site"
    assert not site_info.status


@pytest.mark.django_db
def test_social_count_creation():
    social_count = SocialCount.objects.create(
        nom="Twitter",
        lien="https://twitter.com",
        icones="twitter",
        status=True,
    )
    assert social_count.nom == "Twitter"
    assert social_count.icones == "twitter"


@pytest.mark.django_db
def test_newsletter_creation():
    newsletter = Newsletter.objects.create(
        email="pytest_subscriber@example.com", status=True
    )
    assert newsletter.email == "pytest_subscriber@example.com"
    assert newsletter.status
