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

        self.screen = pygame.display.set_mode((1200, 800))
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

`AlienInvasion` is a class that manages game assets and behavior. The `__init__` method initializes the game and creates game resources. Inside this method, we call `pygame.init()` to initialize all the Pygame modules. Then we call `pygame.display.set_mode((1200, 800))` to create a display window, on which we will draw all the game's graphical elements. The argument `(1200, 800)` is a tuple that defines the dimensions of the game window, which will be 1,200 pixels wide an 800 pixels high, which we can definitely adjust later if needed. We assign the display window to the attribute `self.screen` so we can refer to it later and make it available to other parts of the program.

The object we assigned to `self.screen` is called a `Surface` in Pygame. A `Surface` is a 2D image that we can draw on. The display window is a special kind of `Surface` that is visible on the screen. The surface returned by `pygame.display.set_mode()` represents the entire game window.

The game is controlled by the `run_game()` method, which contains the main loop that runs continuously until the player quits the game. Inside this loop, we check for events, such as keyboard and mouse input, using `pygame.event.get()`. If the player clicks the window's close button, we call `sys.exit()` to exit the game.

Finally, we call `pygame.display.flip()` to update the entire display window to show any changes made to the screen.

At the end of the file, we create an instance of the game and then call the `run_game()` method to start the game loop. We place `run_game()` in an `if` block that only runs if the file is called directly, ensuring that the game starts only when we run this script.

### Controlling the Frame Rate

Ideally, games should run at the same speed, or `frame rate`, on all systems. Controlling the frame rate of a game that can run on multiple systems is a complex issue, but Pygame offers a relatively simple way to accomplish this goal. 

We will make a clock, and ensure the clock ticks once on each pass through the main loop. Anytime the loop processes faster than the rate we define, Pygame will calculate the correct amount of time to pause so that the game runs at a consistent rate.

```python
    def __init__(self):
        """
        Initialize the game, and create game resources
        """
        pygame.init()
        self.clock = pygame.time.Clock()
```

After initializing Pygame, we create an instance of the class `Clock` from the `pygame.time` module. Then we will make the clock tick at the end of the while loop in run_game():

```python
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
        self.clock.tick(60)  # Limit the frame rate to 60 frames per second
```

The `tick()` method takes one argument: the frame rate for the game. Here, we set the frame rate to 60 frames per second. This means that the game will not run faster than 60 frames per second, ensuring a consistent experience across different systems.

### Setting the Background Color

Pygame creates a black background by default. We can set a different background color at the end of the `__init__()` method.

```python
def __init__(self):
    """
    Initialize the game, and create game resources
    """
    pygame.init()
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color
    self.bg_color = (230, 230, 230)  # Light gray color

def run_game(self):
    """
    Start the main loop for the game
    """
    while True:
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(60)  # Limit the frame rate to 60 frames per second
```

Colors in Pygame are specified as RGB colors: a mix of red, green, and blue. Each color value can range from 0 to 255. The color value (255, 0, 0) is red, (0, 255, 0) is green, and (0, 0, 255) is blue. Here, we set the background color to a light gray by using the RGB value (230, 230, 230). You can mix different RGB values to create up to 16 million different colors!

### Creating a Settings Class

