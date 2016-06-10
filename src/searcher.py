# Search for the documents that contain all the words in the index
def search(index, words):
    print("Searching in indexed data...")

    # if only one word in words
    if isinstance(words, str):
        return index.wordToUrls[words]

    # if several words
    urls = []
    for w in words:
        if index.wordToUrls[w] and len(urls) == 0:
            urls = index.wordToUrls[w]
        elif index.wordToUrls[w]:
            urls = list(set(urls) & set(index.wordToUrls[w]))
    return urls