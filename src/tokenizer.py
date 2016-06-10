import re


class TokenizedDocument:
    words = []
    uri = ""

    def __init__(self, words, uri):
        self.words = words
        self.uri = uri


def analyze(documents, processors):
    tokenizedocuments = []
    for doc in documents:
        text = doc.text
        for processor in processors:
            text = processor.process(text)
        words = re.split('[ ,;.?!\"/\*\(\)%#\n><(\-\-)~\|=^$\t@`:+_&\[\]\\ 1-9]+', text)
        tokenizedocuments.append(TokenizedDocument(words, doc.uri))
    return tokenizedocuments
