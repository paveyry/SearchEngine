import pickle


class Index:
    wordToUrls = dict()

    def __init__(self, dict):
        self.wordToUrls = dict

    # Serialize the Index instance
    def save(self, path):
        print("Saving index to " + path + "...")
        f = open(path, "wb")
        # pickle allows to marshal user-defined classes...
        pickle.dump(self, f)


# Create Index (reverse list) from tokenized documents
def buildIndex(token_docs):
    print("Building index...")
    dictionary = {}
    for td in token_docs:
        for w in td.words:
            if w in dictionary and dictionary[w] is not None:
                if td.uri not in dictionary[w]:
                    dictionary[w].append(td.uri)
            else:
                dictionary[w] = [td.uri]
    return Index(dictionary)


# Deserialize an Index
def loadIndex(path):
    print("Loading index from " + path + "...")
    f = open(path, "rb")
    return pickle.load(f)

