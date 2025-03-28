#pytest tests/test.py

import pytest
import requests
from playwright.sync_api import sync_playwright

from django.test import TestCase
from django.urls import reverse
from djangotutorial.concerts.models import Concert

API_URL = "http://127.0.0.1:8000/concerts/reports/"
DASH_URL = "http://127.0.0.1:8050/"

def test_open_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/")
        assert page.title() == "Api Root – Django REST framework"
        browser.close()

@pytest.fixture
def api_data():
    """Получаем данные из API Django."""
    response = requests.get(API_URL)
    assert response.status_code == 200, "API не отвечает"
    data = response.json()
    assert isinstance(data, list), "API должен возвращать список"
    return data

