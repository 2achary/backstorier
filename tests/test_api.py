import pytest
from api import _get_wikipedia_page, _select_random_wiki_entry_from_page


def test_get_wikipedia_page_raises_if_not_alignment_instance():
    with pytest.raises(TypeError) as e:
        _get_wikipedia_page('test')

    assert 'Must provide a valid alignment' in str(e)


def test_select_random_wiki_entry_from_page_raises_if_not_string_instance():
    with pytest.raises(TypeError) as e:
        _select_random_wiki_entry_from_page(True)

    assert "Parameter 'wiki_page' must be a url string, found:" in str(e)