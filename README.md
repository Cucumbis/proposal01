This is a draft game engine proposal by Cucumbis

Run src/init.py to test the game

Design)

Each section of the game has a "frame". Each frame of the game is self-contained, it has a render and update function that allows it to update. Some example frames...

	- Loading Screen
	- Main Menu
	- Actual Game

Conventions)

Variables and Functions, regardless of scope, are to be written in camel case.

	- toString
	- timeToLaunch
	- itsATrap

Constants (in settings/constants.py) and settings (settings/setting.py) are to entirely upper case, with underscores separating words

	- FRAME_RATE
	- WINDOW_HEIGHT
	- TILE_SIZE
