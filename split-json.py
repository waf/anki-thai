#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
from pprint import pprint


def get_json(filename="resources/cards.sealang.json"):
    with open(filename) as data_file:
        data = json.load(data_file, strict=False)
    return data


def split(json_data, title=""):
    def condition(x):
        return x[u'source'].startswith(title)

    filtered = filter(condition, json_data)
    return filtered


def write_json_file(json_data, filename):
    with open(filename, 'w') as outfile:
        json.dump(json_data, outfile)


def list_source(data):
    # get only text before hypen - to group some source
    # SEAlang verb-walk, SEAlang verb-walk => SEAlang verb

    sources = set(map(lambda x: x[u'source'].split('-', 1)[0], data))
    pprint(sources)
    print("has {0} sources".format(len(sources)))


def spit_source(data, souce, outfile):
    filtered = split(data, souce)
    write_json_file(filtered, outfile)
    print("{0} items was written to {1}".format(len(filtered), outfile))


def main():
    data = get_json()
    argvlen = len(sys.argv)
    if(argvlen == 1 or sys.argv[1] == "list"):
        list_source(data)
    elif(argvlen >= 2 and sys.argv[1] == "split"):
        selected_souce = sys.argv[2] if len(sys.argv) > 2 else 'SEAlang verb'
        outfile = sys.argv[3] if len(sys.argv) > 3 else selected_souce + '.json'
        spit_source(data, selected_souce, outfile)

if __name__ == "__main__":
    main()
