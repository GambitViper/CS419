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
It is run using command-line arguments to setup initial configuration
```
python .\KD_Builder.py .\inputData\2d_small.txt 4
```
Where *.\KD_Builder.py* is the name of the program
    *.\inputData\2d_small.txt* is the location of the data to cluster on
    *4* is the minimal-set size to constrain depth of recursive build cases

## Author

* Author: **Zachary Baklund**
* Date-Last-Modified: *10/17/18*