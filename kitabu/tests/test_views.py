from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Customer, Order

class CustomerAPITests(APITestCase):

    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        # Create a sample customer
        self.customer = Customer.objects.create(name="John Doe", email="john@example.com", code="ABC123")

    def test_create_customer(self):
        url = reverse('customer-list') # '/api/customers/'
        data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "code": "XYZ789"
        }
        #response = self.client.post(url, data, format='json')
        response = self.client.post('/api/customers/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Jane Doe")
        self.assertEqual(response.data["email"], "jane@example.com")

    def test_list_customers(self):
        url = reverse('customer-list')  # Adjust based on your actual URL name
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "John Doe")

    def test_retrieve_customer(self):
        url = reverse('customer-detail', args=[self.customer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "John Doe")

    def test_update_customer(self):
        url = reverse('customer-detail', args=[self.customer.id])
        data = {"name": "John Updated", "email": "johnupdated@example.com"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "John Updated")
        self.assertEqual(response.data["email"], "johnupdated@example.com")

    def test_delete_customer(self):
        url = reverse('customer-detail', args=[self.customer.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.objects.filter(id=self.customer.id).exists())


class OrderAPITests(APITestCase):

    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        
        # Create sample customer and order
        self.customer = Customer.objects.create(name="John Doe", email="john@example.com", code="ABC123")
        self.order = Order.objects.create(item="Book", price="9.99", customer=self.customer)

    def test_create_order(self):
        url = reverse('order-list')
        data = {
            "item": "Pen",
            "price": "1.50",
            "customer_id": self.customer.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["item"], "Pen")
        self.assertEqual(response.data["price"], "1.50")
        self.assertEqual(response.data["customer"]["id"], self.customer.id)

    def test_list_orders(self):
        url = reverse('order-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["item"], "Book")

    def test_retrieve_order(self):
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["item"], "Book")

    def test_update_order(self):
        url = reverse('order-detail', args=[self.order.id])
        data = {"item": "Updated Book", "price": "10.99", "customer_id": self.customer.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["item"], "Updated Book")
        self.assertEqual(response.data["price"], "10.99")

    def test_delete_order(self):
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Order.objects.filter(id=self.order.id).exists())
