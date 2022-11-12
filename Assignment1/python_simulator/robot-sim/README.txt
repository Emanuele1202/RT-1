# Research Track: Assignment #1
## Python Robotics Simulator
### Professor [Carmine Recchiuto](https://github.com/CarmineD8), Student: [Matteo Maragliano](https://github.com/mmatteo-hub)

## Running the code <img src="https://user-images.githubusercontent.com/62358773/139832114-25715dd0-508b-4fca-9c20-05c2cc74376f.gif" width="35" height="35"></h2>

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Once the dependencies are installed, simply run the `test.py` script to test out the simulator as: `python2 run.py file.py` where `file.py` contains the code.

## Goal of the assignment
The goal for this assignment is to make a robot move continuously around a specific arena: the robot cannot touch any wall, represented by golden tokens, while has to grab all the silver tokens met along the path and put them backward. Once it has completed this action it has to move on and continues as before with the remanining tokens.

## Elements in the project
### Arena
The arena has a given shape, with walls represented by golden tokens and the presence of silver tokens, as follows:
![arena](https://user-images.githubusercontent.com/62358773/139511599-a028eff0-8865-4ff4-8896-819c297a69df.jpg)

### Robot
#### Physical structure
The robot is the following:

![robot](https://user-images.githubusercontent.com/62358773/139828348-cc5e2ea0-5f71-447a-ac7f-8b7ef74f3324.png)

It has distance sensors on all sides, so it can detect a wall from -180° to 180°; the reference of 0° is the front direction and the angle increases by moving in clockwise direction taking as reference the 0° position and decreases in the other rotation direction.
