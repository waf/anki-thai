# anki-json
Build an Anki deck from a JSON file

# split-json

```sh
# list all sources
$ ./split-json.py list

# split source
$ ./split-json.py split $source $outfile

# example
$ ./split-json.py split SEAlang SEAlang.json
```

# anki-import

```sh
# generate cards from $source
$ ./anki-import.py $source

# example
$ ./anki-import.py resources/cards.sealang.json
```
