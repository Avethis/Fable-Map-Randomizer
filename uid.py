#!/usr/bin/python


class Uid:
    def __init__(self, name, game_map, opposite_door, never_be):
        self.name = name
        self.game_map = game_map
        self.opposite_door = opposite_door
        self.never_be = never_be
        self.replaced_with = None

    def __str__(self):
        return "Uid : [UID : {}, Game Map : {}, Opposite Door : {}, Never Be : {}, Replaced With : {}]".format(
            self.name,
            self.game_map,
            self.opposite_door,
            self.never_be,
            self.replaced_with,
        )
