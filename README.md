This is a draft game engine proposal by Cucumbis

Run src/init.py to test the game

Design)

Each section of the game has a "frame". Each frame of the game is self-contained, it has a render and update function that allows it to update. Some example frames...

	- Loading Screen
	- Main Menu
	- Actual Game

Frames invoke other frames using the *frameController*. This allows the game to move through stages and menus.

Conventions)

Variables, Functions and Modules, regardless of scope, are to be written in camel case.

	- toString
	- timeToLaunch
	- itsATrap

Classes are also camel-case, but with the first letter capitalized

	- V2
	- GameFrame
	- MainMenuFrame

Constants (in settings/constants.py) and settings (settings/setting.py) are to entirely upper case, with underscores separating words

	- FRAME_RATE
	- WINDOW_HEIGHT
	- TILE_SIZE
