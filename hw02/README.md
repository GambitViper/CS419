# K-D Tree

This is a simple implementation for
constructing K-D trees and then finding neighbor sets
for some data along with the nearest neighbor in that set.
Classifying new data according to median values of tree. 

### Prerequisites

Python 3.7

```
[Python 3.7](https://www.python.org/downloads/) - programming language version used
```

## Running the tests

The KD_Builder.py file is the main method driver of the program.
It is run using command-line arguments to setup initial configuration.
When the program is executed, it is given two command-line arguments, in order:
* (a) A data-file from which to read. This file must exist in the same directory as the executing program
* (b) A minimal set-size (this is used by the algorithm to determine when to stop splitting data.) This parameter must be a positive integer value

```
python .\KD_Builder.py .\inputData\2d_small.txt 4
```
This would cause the program to build a tree using the 2-dimensional small data set found in the file **.\inputData\2d_small.txt**, and splitting the data up until each set of points had 4 or fewer members.

## Author

* Author: **Zachary Baklund**
* Date-Last-Modified: *10/17/18*