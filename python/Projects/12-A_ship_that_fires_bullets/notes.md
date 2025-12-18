# A ship that fires bullets

Here, we will set up `Pygame` and then create a rocket ship that moves right and left and fires bullets in response to player input. 

## Planning Your Project

When building a large project, it is important to prepare a plan before we begin to write code. It will keep us focused and make it more likely that we complete the project.

We could use the following description of the general gameplay.

    In `Alien Invasion`, the player controls a rocket ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player shoots and destroys the alients. If the player destroys all the aliens, a new fleet appears that moves faster than the previous fleet. If any alien touches hits the player's ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends.

For the first development phase, we will make a ship that can move right and left when the player presses the arrow keys and fire bullets when the player presses the spacebar.

After setting up this behavior, we can create the aliens and refine the gameplay further.

## Installing Pygame

To install `Pygame`, open a terminal window and enter the following command:

    $ python -m pip install --user pygame

This command installs `Pygame` for the current user. If you are using a virtual environment, make sure it is activated before running the command.

## Starting the Game Project

We will begin building the game by creating an empty Pygame window. Later, we will draw the game elements, such as the ship and the aliens, on this window. We will also make our game respond to user input, set the background color, and load a ship image.

### Creating a Pygame Window and Responding to User Input

```python
import sys

import pygame


class AlienInvasion:
    """
    Overall class to manage game assets and behavior
    """

    def __init__(self):
        """
        Initialize the game, and create game resources
        """
        pygame.init()

        self.screen = pygame.display.set_mode(1200, 800)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """
        Start the main loop for the game
        """
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

The `pygame` module contains the functionality we need to build our game. We start by importing this module and the `sys` module, which will allow us to exit the game when the player wants to quit.
