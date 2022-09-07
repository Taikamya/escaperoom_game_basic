"""
Escape Room game sample - To be used as a tutorial for teaching.

author = Dimitri Dias Moreira @taikamya
"""

class GameObject:
    def __init__(self, name: str, appearance: str, feel: str, smell: str) -> None:
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"

    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    def sniff(self):
        return f"You smell the {self.name}. {self.smell}\n"


class Room:
    def __init__(self, escape_code: int, game_objects) -> None:
        self.escape_code = escape_code
        self.game_objects = game_objects

    def check_code(self, code):
        return self.escape_code == code

    def get_game_object_names(self):
        names = []
        for name in self.game_objects:
            names.append(name)
        return names


class Game:
    def __init__(self) -> None:
        self.attempts = 0
        objects = self.create_objects
        self.room = Room(123, objects)

    def create_objects(self):
        return []
