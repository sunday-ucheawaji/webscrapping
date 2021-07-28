# Entry point of your application
import re
import requests
from bs4 import BeautifulSoup
from .utils import common_words
from collections import Counter


class Scraper:
    """ The Scraper class takes a URL, gets the page of the requested URL,
        cleans up the page and provides a
    """
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.common_words = common_words

    """This get the webpage of the URL and strips off the whitespace"""
    def get_page(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        body_portion = soup.find('body').text.strip()
        return body_portion

    """ The web page is cleaned up. Unnecessary words and special characters are removed"""
    def clean_up(self, page):
        first_filter = re.compile(r'[0-9~©ł!\\)\//…≡@$%^&*()_\-,+=\'\[\]:?..><>><<▲;\ł,]?')
        first_filtered_content = re.sub(first_filter, '', page)
        second_filter = re.compile(r'[ł]?')
        second_filtered_content = re.sub(second_filter, '', first_filtered_content)
        return second_filtered_content

    """The ten most common words are then selected and put in a dictionary with their
        respective frequency numbers
    """
    def key_value(self, clean_up_page):
        split_body = clean_up_page.lower().split()
        for i in split_body:
            if not i.isalnum():
                self.common_words.append(split_body.pop(split_body.index(i)))

        for index in self.common_words:
            for j in split_body:
                if index == j:
                    split_body.remove(index)
        collection_modified = Counter(split_body).most_common(10)
        return dict(collection_modified)