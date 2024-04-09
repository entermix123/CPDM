from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core import exceptions

from CPDM.accounts.models import Profile

UserModel = get_user_model()


class TestAccounts(TestCase):

    def test_create_account_profile__with_valid_data__expect_success(self):
        # Arrange
        user_data = {
            'email': 'example@email.com',
            'password': 'examplePassword123',
        }

        # Act
        account = UserModel.objects.create(**user_data)

        # Assert
        self.assertEqual(account.email, user_data['email'])
        self.assertEqual(account.password, user_data['password'])

    def test_create_account_profile__with_invalid_data__expect_failure(self):
        # Arrange
        user_data = {
            'email': 'exampleemail.com',
            'password': 'examplePassword123',
        }

        # Act
        with self.assertRaises(exceptions.ValidationError) as context:
            book = UserModel.objects.create(**user_data)
            book.full_clean()  # call validators

        # Assert
        exception = context.exception
        title_exception = str(exception.error_dict['email'][0])
        self.assertEqual("['Enter a valid email address.']", title_exception)

    def test_profile_str__with_valid_data__expect_success(self):
        # Arrange

        password = 'examplePassword123',
        users = [
            UserModel.objects.create(email=f'example@email.com-{index}', password=password)
            for index in range(1, 5)
        ]

        profile1 = Profile.objects.create(first_name='John', last_name='Doe', user=users[0])
        profile2 = Profile.objects.create(first_name='John', last_name='', user=users[1])
        profile3 = Profile.objects.create(first_name='', last_name='Doe', user=users[2])
        profile4 = Profile.objects.create(first_name='', last_name='', user=users[3])

        # Act
        profile1_str = profile1.__str__()
        profile2_str = profile2.__str__()
        profile3_str = profile3.__str__()
        profile4_str = profile4.__str__()

        # Assert
        self.assertEqual(profile1_str, 'John Doe')
        self.assertEqual(profile2_str, 'John')
        self.assertEqual(profile3_str, 'Doe')
        self.assertEqual(profile4_str, 'example@email.com-4')
