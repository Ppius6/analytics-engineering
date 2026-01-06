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

### Allowing Continous Movement

Now, when the player holds down the right arrow key, we want the ship to continue moving right until the player releases the key. We will have the game detect a `pygame.KEYUP` event so we will know when the right arrow key is released; then we will use the `KEYDOWN` AND `KEYUP` events together with a flag called `moving_right` to implement continous motion. 

When the `moving_right` flag is `False`, the ship will be motionless. When the player presses the right arrow key, we will set the flag to `True`, and when the player releases the key, we will set the flag to `False` again.

The `Ship` class controls all attributes of the ship, so we will give it an attribute called `moving_right` and an `update()` method to check the status of the `moving_right` flag. The `update()` method will change the position of the ship if the flag is set to `True`. This method will be called once on each pass through the while loop to update the position of the ship.

```python
class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """
        Initialize the ship and set its starting position
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag; start with a ship that is not moving
        self.moving_right = False

    def update(self):
        """
        Update the ship's position based on the movement flag
        """
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """
        Draw the ship at its current location
        """
        self.screen.blit(self.image, self.rect)
```

The `update()` method will be called from outside the class, so it is not considered a helper method.

Now, we modify `_check_events()` so that `moving_right` is set to `True` when the right arrow key is pressed and `False` when the key is released:

```python

    def _check_events(self):
        """
        Respond to keypresses and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.type == pygame.K_RIGHT:
                    self.ship.moving_right = False
```

Next, we set the while loop in `run_game()` such that it calls the ship's `update()` method on each pass through the loop:

```python

    def run_game(self):
        """
        Start the main loop for the game
        """
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

```

The ship's position will be updated after we have checked for keyboard events and before we update the screen. This allows the ship's position to be updated in response to player input and ensures the updated position will be used when drawing the ship to the screen.

### Moving Both Left and Right

Now that the ship can move continuously to the right, adding movement to the left is straightforward; we modify the `Ship` class and the `_check_events()` method.

```python
class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """
        Initialize the ship and set its starting position
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag; start with a ship that is not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update the ship's position based on the movement flag
        """
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
```

In `__init__()` method, we add a `self.moving_left` flag. In `update()` we use two separate if blocks which makes movements more accurate when the player might momentarily hold down both keys when changing directions.

```python
    def _check_events(self):
        """
        Respond to keypresses and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
```

### Adjusting the Ship's Speed

Currently, the ship moves one pixel per cycle through the while loop, but we can take finer control of the ship's speed by adding a `ship_speed` attribute to the `Settings` class. 

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
        self.bg_color = (0, 0, 255)  # blue background
        self.ship_speed = 1.5
```

Now, when the ship moves, its position is adjusted by 1.5 pixels, rather than 1 pixel on each pass through the loop.

We are using a float for the speed setting to give us finer control of the ship's speed when we increase the tempo of the game later on. However, `rect` attributes such as x store only integer values, so we need to make some modifications to the `Ship`:

```python
class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """
        Initialize the ship and set its starting position
        """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that is not moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update the ship's position based on the movement flag
        """
        # Update the ship's x value, not the rect
        if self.moving_right:
            self.x += self.settings.ship_speed

        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update rect objects from self.x
        self.rect.x = self.x

    def blitme(self):
        """
        Draw the ship at its current location
        """
        self.screen.blit(self.image, self.rect)
```

### Limiting the Ship's Range

The ship may disappear off either edge of the screen if you hold hold down an arrow key long enough. We can correct this so the ship stops moving when it reaches the screen's edge in the `update()` method:

```python
    def update(self):
        """
        Update the ship's position based on the movement flag
        """
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect objects from self.x
        self.rect.x = self.x
```

### Refactoring `_check_events()`

The `_check_events()` method will increase in length as we continue to develop the game, so we break it into two separate methods; one that handles `KEYDOWN` events and another that handles `KEYUP` events:

```python
    def _check_events(self):
        """
        Respond to keypresses and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
```

### Pressing Q to Quit

To end our game, we can add the following in `alient_invasion.py`

```python
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
```

In ` _check_keydown_events()`, we add a new block that ends the game when the player presses Q. Now, when testing, we can press Q to close the game instead of using our cursor to close the window.

### Running the Game in Fullscreen Mode

We can use the fullscreen mode which would allow for better engagement by modifying the `__init__()` method:

```python

    def __init__(self):
        """
        Initialize the game, and create game resources
        """
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN
        )
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
```

## Shooting Bullets

We can add the ability to shoot bullets; code that is represented by a small rectangle when the player presses the spacebar. Bullets will travel straight up the screen until they disappear off the top of the screen.

```python
In `settings.py`;

    def __init__(self):
        """
        Initialize the game's settings
        """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)  # blue background
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

```

These settomgs create dark gray bullets with a width of 3 pixels and a height of 15 pixels. The bullets will travel faster that the ship.

### Creating the Bullet Class

We then add a new `Bullet` class;

```python

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float
        self.y = float(self.rect.y)

```

The `Bullet` class inherits from `Sprite`, which we import from the `pygame.sprite` module. When we use sprites, we can group related elements in our game and act on all the grouped elements at once. To create a bullet instance, __init__() needs the current instance of `AlientInvasion` and we call `super()` to inherit properly from `Sprite`. We also set attributes for the screen and settings objects, and for the bullet's color.

We then specify the position using the rect attribute and specify the bullet's midtop attribute to match the ship's midtop attribute. 

```python

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

```

The `update()` method manages the bullet's position. When a bullet is fired, it moves up the screen, which corresponds to a decreasing y-coordinate value. To update the position, we subtract the amount stored in `settings.bullet_speedf` from `self.y`. We then use the value of `self.y` to set the value of `self.rect.y`

When we want to draw a bullet, we call `draw_bullet()`. The `draw.rect()` function fills the part of the screen defined by the bullet's `rect` with the color stored in `self.color`


### Storing Bullets in a Group

We update the code to fire a bullet each time a player presses the spacebar. We will create a group in `AlienInvasion` to store all the active bullets so we can manage the bullets that have already been fired. The group will be an instance of the `pygame.sprite.Group` class, which behaves like a list with some extra functionality that is helpful when building games. We will use this group to draw bullets to the screen one each pass through the main loop and to update each bullet's position.

In `alien_invasion.py`, we add;

```python

from bullet import Bullet #

---

    def __init__(self):
        """
        Initialize the game, and create game resources
        """
        ---
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() #

    def run_game(self):
        """
        Start the main loop for the game
        """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update() #
            self._update_screen()
            self.clock.tick(60)

```

When we call `update()` on a group, the group automatically calls `update()` for each sprite in the group. The line `self.bullets.update()` calls `bullet.update()` for each bullet we place in the group `bullets`.

### Firing Bullets

In `AlienInvasion`, we need to modify `_check_keydown_events()` to fire a bullet when the player presses the spacebar. We do not need to change `_check_keyup_events()` because nothing happens when the spacebar is released. We also need to modify `_update_screen()` to make sure each bullet is drawn to the screen before we call `flip()`. 

We add a new method `_fire_bullet()` to handle the work of firing a bullet:

```python

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """
        Update images on the screen, and flip to the new screen
        """
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

```

### Deleting Old Bullets

At the moment, the bullets disappear when they reach the top, but only because Pygame cannot draw them above the top of the screen. The bullets actually continue to exist; their y-coordinate values just grow increasingly negative. This is a problem because they continue to consume memory and processing power.

We need to get rid of these old bullets, or the game will slow down from doing so much unnecessary work. To do this, we need to detect when the bottom value of a bullet's rect has a value of 0, which indicates the bullet has passed off the top of the screen:

```python


    def run_game(self):
        """
        Start the main loop for the game
        """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            self._update_screen()
            self.clock.tick(60)

```

### Limiting the Number of Bullets

Many shooting games limit the number of bullets a player can have on the screen at one time; doing so encourages players to shoot accurately. We will do the same for `AlienInvasion`

We first store the number of bullets allowed in `settings.py`

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
        self.bg_color = (0, 0, 255)  # blue background
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

```

We then use this setting in AlienInvasion to check how many bullets exist before creating a new bullet in `_fire_bullet()`:

```python

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

```

When the player presses the spacebar, we check the length of bullets. If `len(self.bullets)` is less than three, we create a new bullet. But if three bullets are already active, nothing happens when the spacebar is pressed. When we run the game now, we should only be able to fire bullets in groups of three.

### Creating the `_update_bullets()` Method

To keep our code more organized, we can move the bullet management code and add it to a separate method. We will create a new method called `_update_bullets()` and add it just before `_update_screen()`:

```python

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have dissapeared
        for bullet in self.bullets.copy:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

```

The code for `_update_bullets()` is cut and pasted from `run_game()`; all we have done here is clarify the comments.

The while loop in `run_game()` now looks simple:

```python

    def run_game(self):
        """
        Start the main loop for the game
        """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
            
```