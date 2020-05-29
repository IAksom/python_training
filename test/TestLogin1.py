# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
     app.login(username="admin", password="secret")
     app.create_group(Group(name="testtest", head="23", footer="15"), "testtest", "23", "15")
     app.logout()

def test_login_empty(app):
     app.login(username="admin", password="secret")
     app.create_group(Group(name="", head="", footer=""), "testtest", "23", "15")
     app.logout()





