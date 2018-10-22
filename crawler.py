"""crawler.py

Web crawler using Requests library. Backend is in store.py.

@author: Tobias Thelen
@contact: tobias.thelen@uni-osnabrueck.de
@licence: public domain
@status: completed
@version: 1 (10/2018)

Sie KÖNNEN die hier vorgeschlagene Struktur nutzen, müssen das aber nicht.
Alle Vorschläge sollen nur eine Hilfe für diejenigen sein, die lieber mit
etwas mehr Anleitung vorgehen wollen.

"""

import urllib.parse  # parse urls
import posixpath  # path related functions
import re  # regular expressions

import requests  # the requests library for reliable http client code


class Crawler:
    """Fetches pages, extracts links and feeds the search index."""

    def __init__(self, store):
        self.store = store  # the Store object as search index
        self.queue = ['/']  # we start at root
        self.visited = []   # and have not visited anything yet

    def get_links(self, html, path):
        """Extract links to other pages (same domain only) from html and adds to quere. Normalizes links.

        :param html string The cleaned html content of a page.
        :param path string The current page's absolute path.
        :return None
        """
        pass

    @staticmethod
    def get_title(html):
        """Extract title from raw html.

        :param html string The raw page content.
        :return string The title.
        """
        pass

    @staticmethod
    def clean(raw_html):
        """Remove unwanted content from html file.
           Steps are:
           1. Remove script, style and head tags and their content
           2. Remove html comments
           3. Remove all HTML tags
           4. Collapse all white space to single spaces

        :param raw_html string The raw page content.
        :return string The cleaned html.
        """
        pass

    def fetch(self, path):
        """Fetch a url and store page.

        :param path string the (absolute) url to fetch.
        :return None
        """
        pass

    def crawl(self):
        """Fetch pages and follow links. Build search database."""
        pass
