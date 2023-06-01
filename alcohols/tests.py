import pytest
from django.test import Client
from django.urls import reverse
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject.settings")
django.setup()

from alcohols.forms import *
from alcohols.models import *
from alcohols.views import *

@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

