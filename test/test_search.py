import pytest

from fixture.application import Application
from model.search import Search


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_search_box(app):
    app.search.enter_search_phrase(Search(phrase="eur"))
    #app.search.open_first_return_result()

def test_empty_search(app):
    app.search.enter_search_phrase(Search(phrase=""))
    #app.search.open_first_return_result()


#def test_empty_search(app):
    #app.search.enter_search_phrase(Search(phrase=random_phrase()))
