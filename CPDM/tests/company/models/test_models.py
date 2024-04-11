from django.contrib.auth import get_user_model
from django.core import exceptions
from django.test import TestCase

from CPDM.accounts.models import Profile
from CPDM.company.models import Company

UserModel = get_user_model()


class TestCompany(TestCase):
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

    def test_company_create__with_valid_data__expect_success(self):
        self.client.login(email=self.user.email, password='examplePassword123')

        company_data = {
            'type': 'Production',
            'name': 'CompanyName',
            'industry': 'IT',
            'website': 'https://example.com',
            'owner_id': self.user.pk,
        }

        company = Company.objects.create(**company_data)

        self.assertEqual(company.type, 'Production')
        self.assertEqual(company.name, 'CompanyName')
        self.assertEqual(company.industry, 'IT')
        self.assertEqual(company.website, 'https://example.com')

    def test_company_create__with_invalid_data__expect_exception(self):
        # Arrange
        self.client.login(email=self.user.email, password='examplePassword123')
        company_data = {
            'type': 'Production',
            'name': 'CompanyName',
            'industry': 'IT',
            'website': 'https://examplecom',
            'owner_id': self.user.pk,
        }

        # Act
        with self.assertRaises(exceptions.ValidationError) as context:
            company = Company.objects.create(**company_data)
            company.full_clean()

        # Assert
        exception = context.exception
        email_exception = str(exception.error_dict['website'][0])
        self.assertEqual("['Enter a valid URL.']", email_exception)

    def test_company_str__with_valid_data__expect_success(self):
        # Arrange
        self.client.login(email=self.user.email, password='examplePassword123')
        company_data = {
            'type': 'Production',
            'name': 'CompanyName',
            'industry': 'IT',
            'website': 'https://examplecom',
            'owner_id': self.user.pk,
        }
        company = Company.objects.create(**company_data)

        # Act
        company_str = company.__str__()

        # Assert
        self.assertEqual('CompanyName', company_str)
