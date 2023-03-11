import pytest
from flaskrn.app import *



def test_home_page():
    respone = app.test_client().get("/")
    res = respone.data.decode('utf-8')
    assert "blockcontent" in res
    assert "My Webpage" in res
    assert respone.status_code == 200
    assert "Landing Page!" in res
        
