import random
import itertools
import genanki
import json

def get_model(css):
    return genanki.Model(
        1487859596,
        'thai_model',
        fields = [
            {'name': 'th'},
            {'name': 'en'},
        ],
        templates = [
            {
                'name': 'th → en',
                'qfmt': '<div id="thai">{{th}}</div>',
                'afmt': '{{FrontSide}}<hr id="answer"><div id="english">{{en}}</div>',
            },
            {
                'name': 'en → th',
                'qfmt': '<div id="english">{{en}}</div>',
                'afmt': '{{FrontSide}}<hr id="answer"><div id="thai">{{th}}</div>',
            },
        ],
        css = css)


def new_deck(deck_name):
    random.seed(hash(deck_name))
    deck_id = random.randrange(1 << 30, 1 << 31)
    return genanki.Deck(deck_id, deck_name)

class Card(genanki.Note):
    @property
    def guid(self):
        return genanki.guid_for(self.fields[0]) # th

def new_card(model, thai, english):
    return Card(
        model = model,
        fields = [thai, english]
    )

def distinct(cards):
    distinct = {}
    for card in cards:
        distinct[card["thai"]] = card
    return distinct.values()

def main():

    # read in the input json data (a flat array of objects) for our cards
    with open("resources/cards.sealang.json") as json_data:
        cards = json.load(json_data)
    # read in the mapping of card's source property to the anki collection
    # this allows for hierarchical categories in the generated deck
    with open("resources/source-map.json") as json_data:
        source_map = json.load(json_data)
    with open("resources/cards.css") as cssData:
        card_style = cssData.read()

    # defines how to use card's source property to look up the collection name in the source-map file 
    # you'll probably need to rewrite this function for your specific data.
    def cardGroupFunction(card):
        prefix = card['source'].split("-")[0]
        return source_map[prefix]["source"]

    cardsBySource = itertools.groupby(cards, cardGroupFunction)
    decks = []
    model = get_model(card_style)
    for source, cards in cardsBySource:
        if source == "SKIP":
            continue
        # :: has special meaning in Anki card names: it nests decks.
        deck_name = "Thai::" + source
        print("creating... " + deck_name)
        deck = new_deck(deck_name)
        for card in distinct(cards):
            card = new_card(model, card['thai'], card['english'])
            deck.add_note(card)
        decks.append(deck)
    genanki.Package(decks).write_to_file('dist/thai.apkg')

if __name__ == "__main__":
    main()

