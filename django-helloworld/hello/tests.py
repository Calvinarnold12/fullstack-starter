import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
class TestHelloWorldView:
    """Test suite for the Hello World view"""
    
    def setup_method(self):
        """Setup for each test"""
        self.client = Client()
    
    def test_hello_world_view_returns_200(self):
        """Test that the hello world view returns a 200 status code"""
        response = self.client.get('/')
        assert response.status_code == 200
    
    def test_hello_world_view_contains_message(self):
        """Test that the response contains the 'Hello World!' message"""
        response = self.client.get('/')
        assert 'Hello World!' in response.content.decode()
    
    def test_hello_world_view_uses_correct_template(self):
        """Test that the view uses the correct template"""
        response = self.client.get('/')
        assert 'hello/index.html' in [t.name for t in response.templates]
    
    def test_hello_world_view_contains_bootstrap(self):
        """Test that Bootstrap CSS is included"""
        response = self.client.get('/')
        assert 'bootstrap' in response.content.decode()
    
    def test_context_contains_message(self):
        """Test that context contains the message variable"""
        response = self.client.get('/')
        assert 'message' in response.context
        assert response.context['message'] == 'Hello World!'
