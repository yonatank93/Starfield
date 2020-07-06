# Starfield
This as a simple starfield simulation written in Python using [PyGame](https://www.pygame.org/) package.

Import or run Starfield.py to start viewing the starfield.

# Instructions
``` python
from Starfield import Star

mystar = Star(500, 500, 50, 3)
mystar.run()
```
The arguments of `Star` class are the window width and height, number of stars in, and speed.
The method `Star.run` is used to start the starfield simulation.
As a default, the simulation will run for 60 s.
However, the user can also specify the duration in seconds via the keyword argument `duration`.
There is also an option to show the tail of the stars as they move, by specifying the boolean
argumen `show_tail`. The effect of the tails will look nicer in high speed.

# Run the Jupyter notebook
A Jupyter notebook [file](https://github.com/yonatank93/Starfield/blob/master/Starfield.ipynb)
to run the program in an interactive Python is also provided.

# Run in Gitpod
User can also run Starfield in Gitpod.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/yonatank93/Starfield/blob/master/Starfield.py)
