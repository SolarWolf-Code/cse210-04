from game.casting.actor import Actor

# Imported these for the game.
from game.shared.point import Point
from game.shared.color import Color
import random


class Artifact(Actor):
    """
    An item for gem and rock. 

    """

    def __init__(self):
        """
        The constructor for artifact
        """
        super().__init__()
        self._type = random.choice([True, False])
        self._text = "*" if self._type == True else "O"
        self._velocity = Point(0, 3)

    def get_type(self):
        """
        Gets the artifact's type.

        Returns:
            boolean: The type.
        """
        return self._type

    def set_new_color(self):
        """
        Sets color for artifact.

        """
        color = Color(random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))

        self.set_color(color)
