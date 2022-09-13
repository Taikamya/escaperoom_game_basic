"""
Escape Room game sample - To be used as a tutorial for teaching.

author = Dimitri Dias Moreira @taikamya
"""


class GameObject:
    # Creates a game object
    def __init__(self, name: str, appearance: str, feel: str, smell: str) -> None:
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    # Returns a string describing the appearance of the object.
    def look(self):
        return f"You look at the {self.name}. {self.appearance}\n"

    # Returns a string describing the feel of the object.
    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    # Returns a string describing the smell of the object.
    def sniff(self):
        return f"You smell the {self.name}. {self.smell}\n"


class Room:
    # escape_code = 0
    # game_objects = []
    # Initializes an instance of a Room with a escape_code and game_objects

    def __init__(self, escape_code: int, game_objects) -> None:
        self.escape_code = escape_code
        self.game_objects = game_objects

    # Checks the code and returns True if the code is correct.
    def check_code(self, code):
        return self.escape_code == code

    # Gets a list of just the names of game_objects
    def get_game_object_names(self):
        names = []
        for name in self.game_objects:
            names.append(name)
        return names


class Game:
    def __init__(self) -> None:
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(7320, objects)

    # Creates 5 game objects with enough information to guess the code
    def create_objects(self):
        return [
            GameObject(
                "Jeans",
                "It's a pair of blue jeans. The tag says size 20.",
                "It looks rather small.",
                "It smells of fabric softener. Maybe lavanda?"),
            GameObject(
                "Desk",
                "It's a metal desk with only 3 legs.",
                "Someone deliberately snapped off one of the legs.",
                "It smells rusty."),
            GameObject(
                "Journal",
                "The final entry states that time should be hours then minutes then seconds. (H-M-S)",
                "The cover is worn and several pages are missing.",
                "It smells like musty leather."),
            GameObject(
                "Bowl of soup",
                "It appears to be tomato soup.",
                "It has cooled down to room temperature.",
                "You detect 7 different herbs and spices."),
            GameObject(
                "Clock",
                "The hour hand is pointing towards the soup, the minute hand towards the desk and the second hand towards the jeans.",
                "The battery compartment is open and empty.",
                "It smells of plastic.")
        ]

    def take_turn(self):
        prompt = self.get_room_prompt()
        selection = input(prompt)
        print(selection)

    def get_room_prompt(self):
        msg = "Enter the 4 digit lock code or choose an item to interact with:\n"
        names = self.room.get_game_object_names()
        for name in names:
            msg += f"{name}\n"
        return msg


# if __name__ == "__main__":
game = Game()
# game.take_turn()
print(game.room.game_objects)
