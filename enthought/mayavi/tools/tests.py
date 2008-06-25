"""
Module full of tests. nose should pick these up.
"""

from numpy import atleast_2d, ogrid, mgrid

from sources import array2dsource

def test_array2dsource_input_shapes():
    """ Test strange input shapes for array2dsource
    """
    x, y = ogrid[1:10, 1:10]
    array2dsource(x, y, x+y)
    array2dsource(x.squeeze(), y.squeeze(), x+y)

    X, Y = mgrid[1:10, 1:10]
    array2dsource(X, Y, X+Y)
    array2dsource(x, Y, X+Y)
    array2dsource(X, x, X+Y)


if __name__ == "__main__":
    test_array2dsource_input_shapes()
