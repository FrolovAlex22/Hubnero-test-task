from http import HTTPStatus
import json
import unittest
import time

from django.test import TestCase
from django.urls import reverse


class TZTesting(TestCase):

    def test_get_current_usd_have_attention(self):
        first_response = self.client.get("/get-current-usd/")
        time.sleep(3)
        second_response = self.client.get("/get-current-usd/")
        result2 = json.loads(second_response.content.decode("utf-8"))
        self.assertIn("attention", result2.keys())

    def test_get_current_usd_not_attention(self):
        time.sleep(10)
        first_response = self.client.get("/get-current-usd/")
        result = json.loads(first_response.content.decode("utf-8"))
        self.assertNotIn("attention", result.keys())

    def test_get_current_usd_status(self):
        response = self.client.get("/get-current-usd/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
