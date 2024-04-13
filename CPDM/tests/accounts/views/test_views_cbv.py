
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from CPDM.accounts.models import Profile
from CPDM.company.models import Company

UserModel = get_user_model()


class TestCompanyViews(TestCase):
    def setUp(self):
        user_data = {
            'email': 'example@email.com',
            'password': 'examplePassword123',
        }
        self.user = UserModel.objects.create_user(**user_data)

        profile_data = {
            'first_name': '',
            'last_name': '',
            'user': self.user,
        }
        self.profile = Profile.objects.create(**profile_data)

        company_data = {
            'type': 'Production',
            'name': 'CompanyName',
            'industry': 'IT',
            'website': 'https://example.com',
            'owner_id': self.user.pk,
        }

        self.company = Company.objects.create(**company_data)

    def test_company_create__with_valid_data__expect_success(self):
        # Arrange
        self.client.login(email=self.user.email, password='examplePassword123')
        company_data = {
            'type': 'Production',
            'name': 'CompanyName1',
            'industry': 'IT',
            'website': 'https://example.com',
        }

        url = reverse('company_create', kwargs={'pk': self.profile.pk})

        # Act
        response = self.client.post(url, company_data)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ['company/create_company.html'])

    def test_company_create__with_invalid_data__expect_exception(self):
        # Arrange
        self.client.login(email=self.user.email, password='examplePassword123')
        company_data = {
            'type': 'Production',
            'name': 'CompanyName1',
            'industry': 'IT',
            'website': 'https://examplecom',
        }

        url = reverse('company_create', kwargs={'pk': self.profile.pk})

        # Act
        self.client.post(url, company_data)

        # Assert
        company = Company.objects.filter(name=company_data['name']).first()
        self.assertIsNone(company)

    def test_company_details__with_valid_data__expect_success(self):
        # Arrange
        self.client.login(email=self.user.email, password='examplePassword123')
        url = reverse('company_details', kwargs={'pk': self.profile.pk, 'company_id': self.company.pk})

        # Act
        response = self.client.get(url)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'company/company_details.html')
        self.assertEqual(response.context['object'], self.company)
