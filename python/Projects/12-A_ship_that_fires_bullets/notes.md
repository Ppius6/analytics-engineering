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

Each time we introduce new functionality into the game, we will typically create some new settings as well. Instead of adding the settings throughout the code, we can write a module called `settings` that contains a class called `Settings` to store all these values in one place. 

This approach will allow us to work with just one `settings` object anytime we need to access an individual setting, make it easier to modify the game's appearance and behavior as the project grows, and keep our code organized.

```python
class Settings:
    """
    A class to store all settings for Alien Invasion
    """

    def __init__(self):
        """
        Initialize the game's settings
        """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Light gray color
```

To make an instance of `Settings` in the project and use it to access our settings, we will modify the `AlienInvasion` class as follows:

```python
import sys

import pygame
from settings import Settings


class AlienInvasion:
    """
    Overall class to manage game assets and behavior
    """

    def __init__(self):
        """
        Initialize the game, and create game resources
        """
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width, self.settings.screen_height
            )
        )
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

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)  # Limit the frame rate to 60 frames per second


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

## Adding and Creating the Ship Class

After we chose the image of our ship, we need to display it on the screen, and to use our ship, we can create a new ship module that will contain the class `Ship` which will manage most of the behavior of the player's ship.

```python
import pygame

class Ship:
    """
    A class to manage the ship
    """

    def __init__(self, ai_game):
        """
        Initialize the ship and set its starting position
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """
        Draw the ship at its current location
        """
        self.screen.blit(self.image, self.rect)
```

`Pygame` efficiency allows us to treat all game elements like rectanges `(rect)`, even if they are not exactly shaped like rectanges. Treating an element as a rectangle is efficient since rectangles are simple geometric shapes. When `Pygame` needs to figure out whether two game elements have collided, for example, it can do this more quickly if it treats each object as a rectangle. 

To update and show the ship in our screen, we can import `Ship` and make an instance of `Ship` after the screen has been created. 

```python
import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """
    Overall class to manage game assets and behavior
    """

    def __init__(self):
        """
        Initialize the game, and create game resources
        """
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

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
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)  # Limit the frame rate to 60 frames per second


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

The call to `Ship()` requires one argument: an instance of `AlienInvasion`, with the self argument refering to the current instance of `AlienInvasion`, which is the parameter that gives `Ship` access to the game's resources, such as the screen object. We assign this `Ship` instance to `self.ship.

After filling the background, we draw the ship on the screen by calling `ship.blitme()`, so the ship appears on top of the background. 


## Refactoring: The _check_events() and _update_screen() Methods

In huge projects, we often refactor code we have written before adding more code. Refactoring means simplifying the structure of the code we have already written, making it easier to build on. 

Here, we break the `run_game()` method, which is getting lengthy to two helper methods. 

A `helper method` does work inside a class but is not meant to be used by code outside the class. 

In Python, a single leading underscore indicates a helper method.

### The _check_events() Method

We will move the code that manages events to a separate method called `_check_events()` which will simplify `run_game()` and isolate the event management loop. 

Isolating the event loop allows us to manage events separately from other aspects of the game, such as updating the screen.

```python
def run_game(self):
    """
    Start the main loop for the game
    """
    while True:
        self._check_events()

        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(60)  # Limit the frame rate to 60 frames per second

def _check_events(self):
    """
    Respond to keypresses and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
```

We make a new `_check_events()` method and move the lines that check whether the player has clicked to close the window into this new method. 

To call a method from within a class, we use a dot notation with the variable `self` and the name of the method. We call the method from inside the while loop in `run_game()`: `self._check_events()`

### The _update_screen() Method

We will also move the code for updating the screen to a separate method called `_update_screen()`

```python
def run_game(self):
    """
    Start the main loop for the game
    """
    while True:
        self._check_events()
        self._update_screen()
        self.clock.tick(60)

def _check_events(self):
    """
    Respond to keypresses and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def _update_screen(self):
    """
    Update images on the screen, and flip to the new screen
    """
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()
```

## Piloting the Ship

Next, we can add the ability to move the ship right and left. Here, we write code that responds when the player presses the right or left arrow key.

### Responding to a Keypress

Whenever the player presses a key, it is registered in Pygame as an event. Each event is picked up by the `pygame.event.get()` method. We need to specify in our `_check_events()` method what kinds of events we want the game to check for. Each keypress is registered as a `KEYDOWN` event.

When Pygame detects a `KEYDOWN` event, we need to check whether the key that was pressed is one that triggers a certain action. For example, if the player processes the right arrow key, we want to increase the ship's `rect.x` value to move the ship to the right:

```python
def _check_events(self):
    """
    Respond to keypresses and mouse events
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                self.ship.rect.x += 1
```

Inside `_check_events()` we add an elif block to the event loop, to respond when Pygame detects a `KEYDOWN` event. We check whether the key pressed, event.key, is the right arrow key. The right arrow key is represented by `pygame.K_RIGHT`. If the right arrow key was pressed, we move the ship to the right by increasing the value of `self.ship.rect.x` by 1.
