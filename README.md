Summary
=======

This repository contains a small Search Engine developed in Python in a
few hours. The program can loop recursively in a specified directory
and index all the files. This index can be saved in a file for further use.
The program can then search in this index for the searched keywords.

A dataset can be found [here](http://people.csail.mit.edu/jrennie/20Newsgroups/20news-bydate.tar.gz).

Usage
======

```
usage: main.py [-h] [--datadir DATADIR] [--indexfile INDEXFILE] [--index]
   [WORDS [WORDS ...]]

   Small Search Engine

   positional arguments:
     WORDS                 Words for the search request.

   optional arguments:
     -h, --help            show this help message and exit

     --datadir DATADIR     Directory containing the files to index.
                           Default value is '../20news-bydate-test'.

     --indexfile INDEXFILE File where the indexed data is stored/loaded.
                           Default value is '../index.data'.

     --index               Activated file indexing. The program will index
                           files in datadir and store the indexed data in the
                           indexfile
```
