from django.test import TestCase
from .models import Facture
from django.utils import timezone
from django.urls import reverse
from django.test import Client
from django.core.exceptions import ValidationError


""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """

# Test de models
class FactureModelTest(TestCase):

    def test_facture_creation(self):
        facture = Facture.objects.create(
            client="Michael",
            article_name="Table",
            article_quantity=10,
            ttc=100.00,
            ht=80.00,
            date=timezone.now()
        )
        self.assertEqual(facture.client, "Michael")
        self.assertEqual(facture.article_name, "Table")
        self.assertEqual(facture.article_quantity, 10)
        self.assertEqual(facture.ttc, 100.00)
        self.assertEqual(facture.ht, 80.00)
        self.assertEqual(facture.calculMontantTaxe(), 20)

    def test_facture_str(self):
        facture = Facture.objects.create(
            client="Janette",
            article_name="widget",
            article_quantity=5,
            ttc=50.00,
            ht=40.00,
            date=timezone.now()
        )
        expected_str = f"Facture {facture.id} - Janette - 50.00€ - en date du: {facture.date}"
        self.assertEqual(str(facture), expected_str)

    def test_facture_ordering(self):
        facture1 = Facture.objects.create(
            client="Junior",
            article_name="obj A",
            article_quantity=1,
            ttc=10.00,
            ht=8.00,
            date=timezone.now()
        )
        facture2 = Facture.objects.create(
            client="Claire",
            article_name="obj B",
            article_quantity=2,
            ttc=20.00,
            ht=16.00,
            date=timezone.now() - timezone.timedelta(days=1)
        )
        factures = Facture.objects.all()
        self.assertEqual(factures[0], facture1)
        self.assertEqual(factures[1], facture2)

    def test_facture_save(self):
        facture = Facture(
            client="Caddie",
            article_name="Bonbon",
            article_quantity=3,
            ttc=30.00,
            ht=24.00,
            date=timezone.now()
        )
        facture.save()
        saved_facture = Facture.objects.get(id=facture.id)
        self.assertEqual(saved_facture.client, "Caddie")
        self.assertEqual(saved_facture.article_name, "Bonbon")
        self.assertEqual(saved_facture.article_quantity, 3)
        self.assertEqual(saved_facture.ttc, 30.00)
        self.assertEqual(saved_facture.ht, 24.00)

    def test_facture_creation_with_null_client(self):
        facture = Facture(
            client=None,
            article_name="Tool",
            article_quantity=3,
            ttc=30.00,
            ht=24.00,
            date=timezone.now()
        )
        with self.assertRaises(ValidationError):
            facture.full_clean()

""" ------------------------------------------------- """
""" ------------------------------------------------- """
""" ------------------------------------------------- """


# Test de views

class FactureListViewTest(TestCase):

    def setUp(self):
        Facture.objects.create(client="John Doe", article_name="Widget", article_quantity=10, ttc=100.00, ht=80.00, date=timezone.now())
        Facture.objects.create(client="Jane Doe", article_name="Gadget", article_quantity=5, ttc=50.00, ht=40.00, date=timezone.now())
        Facture.objects.create(client="Alice", article_name="Tool", article_quantity=3, ttc=30.00, ht=24.00, date=timezone.now())

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/factures/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('facture-list'))
        self.assertTemplateUsed(response, 'facture_list.html')

    def test_filter_by_client(self):
        response = self.client.get('/factures/?client=John')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertNotContains(response, "Jane Doe")

    def test_filter_by_article_name(self):
        response = self.client.get('/factures/?article_name=Tool')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tool")
        self.assertNotContains(response, "Widget")

class FactureDetailViewTest(TestCase):

    def setUp(self):
        self.facture = Facture.objects.create(client="John Doe", article_name="Widget", article_quantity=10, ttc=100.00, ht=80.00, date=timezone.now())

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/factures/{self.facture.id}/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('facture-detail', args=[self.facture.id]))
        self.assertTemplateUsed(response, 'facture_detail.html')


class FactureCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('facture-create'))
        self.assertTemplateUsed(response, 'facture_form.html')

    def test_form_submission(self):
        response = self.client.post(reverse('facture-create'), {
            'client': 'Alice',
            'article_name': 'Tool',
            'article_quantity': 3,
            'ttc': 30.00,
            'ht': 24.00,
            'date': timezone.now()
        })
        self.assertEqual(response.status_code, 200)  # Redirect after successful creation



