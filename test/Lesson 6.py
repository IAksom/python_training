import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username='admin', password='secret')
    app.create_group(Group(name="testtest", head="23", footer="15"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username='admin', password='secret')
    app.create_group(Group(name="", head="", footer=""))
    app.session.logout()
