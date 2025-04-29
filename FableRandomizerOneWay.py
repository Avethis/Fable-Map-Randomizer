#!/usr/bin/python

import sys, getopt
import os, os.path
import re
from random import choice
from uid import Uid
from loadMapFile import loadMapFile

map_file = r"map\UIDList.txt"
target_dir = r"TNGS"
help_message = "FableRandomizerOneWay.py -m <mapfile> -t <targetDir>"

uids = {}
uid_substitutions = {}
spent_uids = set()
uid_map = {}

def captureClp(argv):
    global map_file
    global target_dir
    try:
        opts, args = getopt.getopt(argv, "hm:t:", ["mapfile=", "targetDir="])
    except getopt.GetoptError:
        printHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            printHelp()
            sys.exit()
        elif opt in ("-m", "--mapfile"):
            map_file = arg
            print("Map file is {}".format(map_file))
        elif opt in ("-t", "--targetDir"):
            target_dir = arg
            print("Target file is {}".format(target_dir))


def validateClp():
    if not map_file:
        print("Map file is required")
        printHelp()
        sys.exit(-1)
    else:
        validateFile(map_file)
    if not target_dir:
        print("Target file is required")
        printHelp()
        sys.exit(-1)
    else:
        validateDir(target_dir)


def printHelp():
    print(help_message)

def cleanUp():
    files_in_directory = os.listdir(target_dir)
    levs = [file for file in files_in_directory if file.endswith(".lev")]
    for file in levs:
        path_to_file = os.path.join(target_dir, file)
        os.remove(path_to_file)
    print("Deleted .levs successfully.")
    
    cheat_sheet = open("cheatsheet.txt","w")
    cheat_sheet.close()
    print("Removed prior contents of cheatsheet.txt")

def validateDir(dir_name):
    if not os.path.isdir(dir_name):
        print("{} is not a valid dirrectory".format(dir_name))
        sys.exit(-1)


def validateFile(file_name):
    if not os.path.isfile(file_name):
        print("Could not access file {}".format(file_name))
        sys.exit(-1)


def processTargetDir():
    for file in os.listdir(target_dir):
        file_path = os.path.join(target_dir, file)
        if file_path == map_file:
            continue
        if not os.path.isfile(file_path):
            continue
        processTargetFile(target_dir, file)


def processTargetFile(target_dir, file):
    target_file = os.path.join(target_dir, file)
    out_file_name = os.path.join(target_dir, "FinalAlbion", file)
    out_file = open(out_file_name, "w")
    print("Processing {}, output file is {}".format(target_file, out_file_name))
    in_file = open(target_file, "r")

    lines = in_file.read().splitlines()
    for line in lines:
        if line.endswith(";"):
            line = line[:-1]
        updated_line = processTargetLine(line)
        out_file.write(updated_line)
        if updated_line:
            out_file.write(";")
        out_file.write("\n")


def processTargetLine(line):
    out_line = []
    for word in line.split():
        uid = uids.get(word)
        if uid == None:
            out_line.append(word)
        else:
            different_uid = uid_map.get(uid.name)
            out_line.append(different_uid)
    return " ".join(out_line)


def getUidName(uid):
    uid = uids.get(uid.name)
    return getRandomUid(uid)


def getRandomUid(uid):
    max_iters = 1000
    iters = 0
    replace_with = None
    while replace_with is None and iters < max_iters:
        iters = iters + 1
        replace_with = choice(list(uids.values()))
        if uid.never_be == replace_with.name:
            replace_with = None
        elif replace_with.name in spent_uids:
            replace_with = None

    return replace_with


def buildMap():
    global uid_map
    for uid in uids.values():
        if uid.name in uid_map:
            continue
        replacement = getRandomUid(uid)
        with open("cheatsheet.txt", "a") as cheat_sheet:
            original_stdout = sys.stdout
            sys.stdout = cheat_sheet
            print("Will replace {} with {}".format(uid.name, replacement.name))
            cheat_sheet.close()
            sys.stdout = original_stdout
        uid_map[uid.name] = replacement.name
        uid_substitutions.get(uid.game_map).add(replacement.game_map)
        spent_uids.add(replacement.name)

def main(argv):
    global uids
    global uid_substitutions
    captureClp(argv)
    validateClp()
    cleanUp()
    uids, uid_substitutions = loadMapFile(map_file)
    buildMap()
    processTargetDir()


if __name__ == "__main__":
    main(sys.argv[1:])
