import argparse
import connecter
import tokenizer
import textprocessor
import indexer
import searcher

# -h or --help to see formatted usage

parser = argparse.ArgumentParser(description="Small Search Engine")

parser.add_argument("words", metavar="WORDS", type=str, nargs="*",
                    help="Words for the search request."
                    )

parser.add_argument("--datadir", dest="datadir", action="store",
                    help="Directory containing the files to index. "
                         "Default value is '../20news-bydate-test'."
                    )

parser.add_argument("--indexfile", dest="indexfile", action="store",
                    help="File where the indexed data is stored/loaded. "
                         "Default value is '../index.data'."
                    )

parser.add_argument("--index", action="store_true",
                    help="Activated file indexing. The program will index files"
                         "in datadir and store the indexed data in the indexfile"
                    )

args = parser.parse_args()

if not args.datadir:
    args.datadir = "../20news-bydate-test"
if not args.indexfile:
    args.indexfile = "../index.data"


# If the user wants to create the indexes
if args.index:
    # Open all the files
    documents = connecter.fetch(args.datadir)
    # Tokenize, lowercase, remove accents
    tokenizedDocs = tokenizer.analyze(documents, [textprocessor.Normalizer()])
    # Create index
    index = indexer.buildIndex(tokenizedDocs)
    # Serialize index in file
    index.save(args.indexfile)

# If the user passed search keywords as parameter
if args.words:
    # Read index from file
    index = indexer.loadIndex(args.indexfile)
    # Search in index with the specified keywords
    results = searcher.search(index, args.words)
    # Display the results
    print("Your request is matched in the following files:")
    if len(results) > 0:
        for r in results:
            print(r)
    else:
        print("No file matches your request.")


