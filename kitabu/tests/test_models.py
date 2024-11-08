from django.test import TestCase
from ..models import Customer, Order
from django.utils import timezone


class CustomerModelTest(TestCase):

    def setUp(self):
        # Create a customer object for testing
        self.customer = Customer.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            code='CUST123'
        )

    def test_customer_creation(self):
        """Test that a customer object is created successfully"""
        self.assertEqual(self.customer.name, 'John Doe')
        self.assertEqual(self.customer.email, 'johndoe@example.com')
        self.assertEqual(self.customer.code, 'CUST123')
