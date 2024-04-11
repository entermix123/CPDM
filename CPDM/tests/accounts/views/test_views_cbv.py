from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from CPDM.accounts.models import Profile

UserModel = get_user_model()


class TestUserProfileViews(TestCase):
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

    def test_register_user__with_valid_data__expect_success(self):

        user_data = {
            'email': 'example@email1.com',
            'password': 'examplePassword123',
        }

        response = self.client.post(reverse('register_user'), user_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ['accounts/register.html'])

    def test_profile_details__with_valid_data__expect_success(self):
        # Arrange
        self.client.login(email=self.user.email, password='examplePassword123')

        # Act
        response = self.client.get(reverse('profile_details', kwargs={'pk': self.user.pk}))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile_details.html')
        self.assertEqual(response.context['object'], self.profile)
        self.assertEqual(list(response.context['companies_owned']), list(self.user.companies.all()))
        self.assertEqual(list(response.context['activities_owned']), list(self.user.activities.all()))

    def test_update_profile__with_valid_data__expect_success(self):
        # Arrange
        self.client.login(email=self.user.email, password='examplePassword123')
        url = reverse('update_profile', kwargs={'pk': self.profile.pk})
        data = {'first_name': 'updated_f_name', 'last_name': 'updated_l_name'}

        # Act
        response = self.client.post(url, data, follow=True)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile_details.html')
        updated_profile = Profile.objects.get(pk=self.user.pk)
        self.assertEqual(updated_profile.first_name, 'updated_f_name')
        self.assertEqual(updated_profile.last_name, 'updated_l_name')

    def test_update_profile__with_invalid_data__expect_not_changed_data_in_db(self):
        # Arrange
        self.client.login(email=self.user.email, password='examplePassword123')
        url = reverse('update_profile', kwargs={'pk': self.profile.pk})
        profile_data = {
            'first_name': 'D',
            'last_name': 'Name'
        }

        # Act
        self.client.post(url, profile_data)

        # Assert that the profile data remains unchanged
        updated_profile = Profile.objects.get(user=self.user)
        self.assertNotEqual(updated_profile.first_name, profile_data['first_name'])


def test_update_profile__with_invalid_data__expect_exception(self):
    # Arrange
    self.client.login(email=self.user.email, password='examplePassword123')
    data = {'first_name': 'D', 'last_name': 'Name'}

    with self.assertRaises(ValidationError) as context:
        profile = Profile.objects.get(user=self.user)
        for field, value in data.items():
            setattr(profile, field, value)
        profile.full_clean()  # trigger validation

    # Ensure a validation error is raised
    self.assertTrue('first_name' in context.exception.error_dict)
    error_message = str(context.exception.error_dict['first_name'][0])  # Extract error message as a string
    self.assertEqual(error_message, "['Cannot have less than 3 characters']")
