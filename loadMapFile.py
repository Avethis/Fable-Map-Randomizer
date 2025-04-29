#!/usr/bin/python

import re
from uid import Uid

partial_regular_expression = (
    "UID (.*) GameMap (.*) OppositeDoor (.*)"
)
full_regular_expression = "UID (.*) GameMap (.*) OppositeDoor (.*) NeverBe (.*)"

uids = {}
uid_substitutions = {}


def loadMapFile(map_file):
    file = open(map_file, "r")
    lines = file.readlines()
    for line in lines:
        processLine(line)

    print("Loaded {} uid names from File".format(len(uids)))
    return uids, uid_substitutions


def processLine(line):
    uid = tryFullMatch(line)
    if uid is None:
        uid = tryPartialMatch(line)
    if uid is None:
        return
#    print("Loaded {}".format(str(uid)))
    uids[uid.name] = uid
    uid_substitutions[uid.game_map] = set()


def tryFullMatch(line):
    match = re.search(full_regular_expression, line)
    if match != None and len(match.groups()) == 4:
        uid = Uid(match.group(1), match.group(2), match.group(3), match.group(4))
        return uid
    else:
        return None


def tryPartialMatch(line):
    match = re.search(partial_regular_expression, line)
    if match != None and len(match.groups()) == 3:
        uid = Uid(match.group(1), match.group(2), match.group(3), None)
        return uid
    else:
        return None
