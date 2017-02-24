This repository build an APKG file (for importing into Anki/AnkiDroid) from the JSON file `resources/cards.sealang.json`. It shouldn't be too hard to repurpose it for other JSON files.

# anki-import
Converts a json file to an APKG file, with support for nested decks.

```sh
# generate cards from $source
$ ./anki-import.py $source

# example
$ ./anki-import.py resources/cards.sealang.json
```

# split-json
A helper script for splitting large JSON files into smaller JSON files.

```sh
# list all sources
$ ./split-json.py list

# split source
$ ./split-json.py split $source $outfile

# example
$ ./split-json.py split SEAlang SEAlang.json
```

# SEALang deck

The SEALang deck generated from the cards.sealang.json file contains the following categories ("nested decks"):

- AUA Lessons
     - Chapter 01
     - ...
     - Chapter 60
- Common Parts of Speech
    - Adjective Comparisons
    - Adjective Stative Verbs
    - Adjectives
    - Classifiers
    - Nouns
    - Prefixes
    - Prepositions of Location
    - Verbs
- Phonology
    - Consonants - High Class 
    - Consonants - Low Class
    - Consonants - Middle Class
    - Long Vowels
    - Short Vowels
- Topics
    - Abbreviations
    - Academic Words
    - Alphabet Words
    - Animals
    - Art
    - Astronomy
    - Body
    - Books
    - Buddhism
    - Buildings
    - Business
    - Calendar
    - Cloth
    - Clothes
    - Colors
    - Compass
    - Computer
    - Construction
    - Containers
    - Court
    - Crime
    - Directions
    - Economics
    - Education
    - Elections
    - Emergencies
    - Emotion
    - Environment
    - Everyday Conversation
    - Family
    - Feelings
    - Food
    - Fruits and Vegetables
    - Fuel
    - Geography
    - Government
    - Heart
    - Home
    - Important Places
    - International Relations
    - Job Applications
    - Jobs
    - Maanii Book Vocab
    - Materials
    - Math
    - Measurement
    - Military
    - Ministries and Bureaucracy
    - Miscellaneous
    - Music
    - Narcotics
    - Nature
    - Numbers
    - Paperwork
    - People
    - Personal Information
    - Places
    - Politics
    - Questions
    - Reading Vocabulary
    - Religion
    - School
    - Senses
    - Situation
    - Sports
    - TV and News
    - Terrorism
    - Thai Geography
    - The King and Royal Family
    - Time
    - Transportation
    - Weapons
    - Weather
    - Web
    - Writing
