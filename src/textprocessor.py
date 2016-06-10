import unicodedata
from abc import ABCMeta, abstractmethod


class TextProcessor():
    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self, word):
        pass


class Normalizer(TextProcessor):
    def process(self, word):
        word = word.lower()
        unicodeform = unicodedata.normalize('NFKD', word)
        return u"".join([c for c in unicodeform if not unicodedata.combining(c)])


