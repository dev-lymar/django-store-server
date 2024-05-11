from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from orders.models import Order

User = get_user_model()


class SuccessTemplateViewTestCase(TestCase):
    def test_view(self):
        path = reverse("orders:order_success")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "orders/success.html")


class CanceledTemplateViewTestCase(TestCase):
    def test_view(self):
        path = reverse("orders:order_canceled")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "orders/canceled.html")


class OrderListViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

    def test_list(self):
        path = reverse("orders:orders_list")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "orders/orders.html")


class OrderDetailViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.order = Order.objects.create(initiator=self.user)
        self.client.login(username="testuser", password="12345")

    def test_detail(self):
        path = reverse("orders:order", kwargs={"pk": self.order.pk})
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "orders/order.html")
