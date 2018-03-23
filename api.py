from enum import Enum
import logging

LOG = logging.getLogger(__name__)


def get_deets(name='', gender='', alignment=''):
    """
    Get a random wikipedia entry background for a given gender and alignment.
    The name in the entry will be replaced with the name provided.

    Note: Gender makes it easier to get an entry with the proper pronouns.
    """

    # TODO: get a random wikipedia page entry from the list corresponding to the provided alignment
    # TODO: extract the background section from that page
    # TODO: replace the name in the section with the name provided
    pass


class Alignment(Enum):
    Good_Male = ['url page for good']
    Good_Female = ['url page for good']
    Neutral_Male = ['url page for neutral']
    Neutral_Female = ['url page for neutral']
    Evil_Male = ['url page for evil']
    Evil_Female = ['url page for evil']


BACKGROUND_SECTION_NAMES = [
    'background',
    'early life'
]


def _get_wikipedia_page(alignment: Alignment=None) -> str:
    if not isinstance(alignment, Alignment):
        raise TypeError("Must provide a valid alignment: {!s}".format(alignment))


def _select_random_wiki_entry_from_page(wiki_page: str=None) -> str:
    if not isinstance(str, wiki_page):
        raise TypeError("Parameter 'wiki_page' must be a url string, found: <{!s}>".format(type(wiki_page)))

    # TODO: Find the links and choose a random one


def _replace_name_in_text(text: str=None, name: str=None) -> str:
    if not isinstance(text, str):
        raise TypeError("Parameter 'text' must be a str, found: <{!s}>".format(type(text)))
    if not isinstance(name, str):
        raise TypeError("Parameter 'name' must be a str, found: <{!s}>".format(type(name)))

    # TODO: do a basic string replace


def _get_background_section_from_wiki_page(wiki_page: str=None) -> str:
    if not isinstance():
        raise TypeError("Parameter 'wiki_page' must be a url string, found: <{!s}>".format(type(wiki_page)))

    # TODO: search for section with title in BACKGROUND_SECTION_NAMES
