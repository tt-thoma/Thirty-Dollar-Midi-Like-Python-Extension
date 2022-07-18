# -*- encoding: utf-8 -*-

"""
THIRTY DOLLAR MIDI EXTENSION
----------------------------
Thirty dollar reader & exporter by @tt_thoma
Inspired by @GDColon's work
"""

import os
import json

# Integrity check
assert os.path.isfile("data.json"), "Couldn't reach database"
assert os.path.isdir("data"), "Couldn't reach data"

# Open the database
db_file = open("data.json", "r", encoding="utf-8")
__database__ = json.load(db_file)
__database__["path"] = os.path.abspath("data")
db_file.close()
del db_file


class TDNote:
    def __init__(self, data: str or list = None):
        """
        A good old thirty dollar note.

        Data types:
        -----------
        * str: Raw data only (eg: "_pause=5")
        * list: In order:
                   - Name
                   - Type
                   - Count
                   - Arguments:
                        - Argument 1 (sound: pitch)
                        - Argument 2

        :param data: data (supports list and str)
        """
        # Decoding
        if isinstance(data, str):
            self.data = data

            # Detect the type
            if self.data.startswith("_"):
                self.type = "pause"
            elif self.data.startswith("!"):
                self.type = "action"
            else:
                self.type = "sound"

            # Detects the count
            i = None
            try:
                i, self.count = self.data.split("=")
            except ValueError:
                if len(self.data.split("=")) > 0:  # too munch durations...
                    raise ValueError("Too munch durations referenced")

                # There is simply one
                self.count = 1

            # Removes the prefix
            if self.type != "sound":
                if i:  # If data is defined
                    i = i[1:]
                else:
                    i = self.data[1:]

            # Define the arguments needed
            self.args = i.split("@")

            # Define the name
            self.name = self.args[0]

            # Obtain the id
            assert self.name in __database__["id"][self.type], f"Invalid name given ({self.name}) for type ({self.type})"

            i = 0
            for i in range(len(__database__["id"][self.type])):
                if self.name == __database__["id"][self.type][i]:
                    break

            self.id = i

            # Test if the arguments have the correct lenght
            i = len(self.args) - 1
            if self.type == "sound":
                i_ = [0, 1]
            else:
                i_ = __database__["args"][self.type][self.id]
            assert i in i_, f"Note {self.name} needed more/less arguments than the {i} given."

        elif isinstance(data, list or tuple):
            # Checking the arguments lenght
            assert 2 < len(data) < 5, f"List needed from 2 to 5 arguments, but {len(data)} were given."

            # Parsing the arguments
            self.name = data[0]
            self.type = data[1]

            try:
                self.count = data[2]
            except ValueError:
                self.count = 1

            try:
                self.args = list(data[3])
            except ValueError:
                self.args = []
            except TypeError:
                raise TypeError(f"Non-iterable object ({type(data[3])}) given instead of an iterable."
                                "Are you braindead ?")

            # Obtain the prefix
            if self.type == "action":
                prefix = "!"
            elif self.type == "pause":
                prefix = "_"
            elif self.type == "sound":
                prefix = ""
            else:
                raise ValueError(f"Invalid sound type: {self.type}")

            # Builds the data
            self.data = prefix + self.name
            for i in self.args:
                self.data += "@" + i

            if self.count > 1:
                self.data += "=" + str(self.count)
        else:
            raise TypeError(f"Unexpected type: {type(data)}")


class TDFile:
    def __init__(self, name: str):
        self.file = open(name, "w+", encoding="utf-8")
        self.data = self.file.read()

        # Sequence parser
        self.raw = self.data.split("|")


e = TDNote("!speed@6@x=5")
f = TDNote(["speed", "action", 1, None])
print(e.args, e.id)
