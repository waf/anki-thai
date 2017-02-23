#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append('/Applications/Anki.app/Contents/Resources/lib/python2.7/site-packages.zip')
import anki
from anki.exporting import AnkiPackageExporter

TMPDIR="/tmp"
FBASENAME="thai"
FONAME="/Users/botbotbot/develop/hacknight-anki/thai.apkg"

collection = anki.Collection(os.path.join(TMPDIR, 'collection.anki2'))

deck_id = collection.decks.id(FBASENAME + "_deck")
deck = collection.decks.get(deck_id)

model = collection.models.new(FBASENAME + "_model")
model['tags'].append(FBASENAME + "_tag")
model['did'] = deck_id
model['css'] = """
.card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}
.from {
  font-style: italic;
}
"""

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

model['id'] = 12345678  # essential for upgrade detection
collection.models.update(model)
collection.models.setCurrent(model)
collection.models.save(model)

note = anki.notes.Note(collection, model)
note['en'] = "chicken"
note['th'] = u"ไก่"
note.guid = "xxx1"
collection.addNote(note)

note = collection.newNote()
note['en'] = "egg"
note['th'] = u"ไข่"
note.guid = "xxx2"
collection.addNote(note)

export = AnkiPackageExporter(collection)
export.exportInto(FONAME)
