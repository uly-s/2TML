
"""
    The idea here is the ground floor basis for a game instance, ie base game overview data,
    attribute / statblocks, classes, monsters, items, skills. For the time being
    D&D 5E will be a target of sorts to avoid trying to start with a universal solution
"""

# just a placeholder, should probably be a singleton
class Game:
    def __init__(self, name, ver, genre):
        self.name = name
        self.ver = ver
        self.genre = genre

# class for a campaign instance, top level view for state of a campaign
class Campaign:
    def __init__(self, system, title, setting):
        # baseline attributes, the system in use (game object), title, setting (world object?)
        self.system = system
        self.title = title
        self.setting = setting

        # dm and player names
        self.dm = ""
        self.players = [""]

        # player and non player characters, dictionaries of 'name : entity_object'
        self.PCs = {}
        self.NPCs = {}

        # date / timeline, date object and timeline object (specialized list?)
        self.date = ""
        self.timeline = [""]

        # location data, current location, dict of places with 'name : place_object'
        self.pcloc = ""
        self.places = {}

class StatBlock:
    def __init__(self):
        pass

class Entity:
    def __init__(self):
        self.stats = StatBlock()
        pass

class Class:
    def __init__(self):
        pass

class PC(Entity):
    def __init__(self):
        self._class = Class()

class NPC(Entity):
    def __init__(self):
        pass

