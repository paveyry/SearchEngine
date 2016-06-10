import os
import codecs


class Document:
    text = ""
    uri = ""

    def __init__(self, text, uri):
        self.text = text
        self.uri = uri


# Open all the files in path and store their content in an array of strings
def fetch(path):
    print("Fetching data files...")
    documents = []
    for path, dirs, files in os.walk(path):
        for filename in files:
            fullpath = os.path.join(path, filename)
            with codecs.open(fullpath, "r", encoding="utf-8", errors="ignore") as f:
                documents.append(Document(f.read(), fullpath))
    return documents
