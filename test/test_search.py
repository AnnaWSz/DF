import pytest

from model.search import Search
import string
import random


def random_phrase():
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 2
    return "".join([random.choice(symbols) for i in range(10)])


testdata = [Search(phrase = "")] + [Search(phrase= "eur")] + [Search(phrase = random_phrase()) for i in range (5)]


@pytest.mark.parametrize("search", testdata, ids  =[repr(x) for x in testdata])
def test_search_box(app, search):
    app.search.enter_search_phrase(search)
    #app.search.open_first_return_result()

