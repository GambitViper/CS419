# Nueral Network

This is a simple implementation of a utility for building and training neural networks on some data extracted from image files. This code allows the user to specify the structure of one or more multi-layer feed-forward neural networks. It will then train those networks by back-propagation.

The tool will also allow trained networks to be saved to files and loaded again for later re-use.

(Note: Since this is a tool meant to allow a user to explore different possible data-sets and structures, it will be possible to repeat this process ad-infinitum.)

### Prerequisites

[Python 3.7](https://www.python.org/downloads/) - programming language version used

## Running the program

The NeuralNetwork.py file is the main method driver of the program.
It is run using command-line, and handle all input/output using standard I/O
When the program is executed, it will ask the user to choose between three options:
* (a) The user can train a new network.
* (b) The user can load a previously trained network from a data-file. You can assume that this file, if it exists, is contained in the same directory as the operating program.
* (c) The user can quit the program.

```
python .\NeuralNetwork.py
```

## Author

* Author: **Zachary Baklund**
* Date-Last-Modified: *10/25/18*