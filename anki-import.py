#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import hashlib
import itertools
import json

# this path should be to your Anki application install directory
# it allows us to import anki on the next line
currentDirectory = os.getcwd() 
sys.path.append('/Applications/Anki.app/Contents/Resources/lib/python2.7/site-packages.zip')
import anki
from anki.exporting import AnkiPackageExporter

def addCardToCollection(collection, thai, english):
    card = collection.newNote()
    card['th'] = thai
    card['en'] = english
    card.guid = hashlib.md5(english.encode('utf-8') + thai.encode('utf-8')).hexdigest()
    collection.addNote(card)

def createApkgFileFromCollection(collection, filename):
    export = AnkiPackageExporter(collection)
    export.exportInto(filename)

def addNewDeckToCollection(collection, deckName, cardStyle):
    deckId = collection.decks.id(deckName)
    deck = collection.decks.get(deckId)
    model = collection.models.new("thai_model")
    model['tags'].append("thai_tag")
    model['did'] = deckId
    model['css'] = cardStyle

    collection.models.addField(model, collection.models.newField('en'))
    collection.models.addField(model, collection.models.newField('th'))

    tmpl = collection.models.newTemplate('th → en')
    tmpl['qfmt'] = '<div id="thai">{{th}}</div>'
    tmpl['afmt'] = '{{FrontSide}}<hr id="answer"><div id="english">{{en}}</div>'
    collection.models.addTemplate(model, tmpl)

    tmpl = collection.models.newTemplate('en → th')
    tmpl['qfmt'] = '<div id="english">{{en}}</div>'
    tmpl['afmt'] = '{{FrontSide}}<hr id="answer"><div id="thai">{{th}}</div>'
    collection.models.addTemplate(model, tmpl)

    model['id'] = 1487859596  # essential for upgrade detection
    collection.models.update(model)
    collection.models.setCurrent(model)
    collection.models.save(model)

def distinct(cards):
    distinct = {}
    for card in cards:
        distinct[card["thai"]] = card
    return distinct.values()

def main():

    # read in the json data for our cards
    with open("resources/cards.sealang.json") as jsonData:
        cards = json.load(jsonData)
    with open("resources/source-map.json") as jsonData:
        sourceMap = json.load(jsonData)
    with open("resources/cards.css") as cssData:
        cardStyle = cssData.read()
    def cardGroupFunction(card):
        prefix = card['source'].split("-")[0]
        return sourceMap[prefix]["source"]

    cardsBySource = itertools.groupby(cards, cardGroupFunction)
    collection = anki.Collection('/tmp/collection.anki2')
    for source, cards in cardsBySource:
        if source == "SKIP":
            continue
        # :: has special meaning in Anki card names: it nests decks.
        addNewDeckToCollection(collection, "Thai::" + source, cardStyle)
        for card in distinct(cards):
            addCardToCollection(collection, card['thai'], card['english'])

    outputFile = currentDirectory + "/dist/thai.apkg"
    print outputFile
    createApkgFileFromCollection(collection, outputFile)

if __name__ == "__main__":
    main()

