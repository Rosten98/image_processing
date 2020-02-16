import numpy as np


def euclidean2D_to_homogeneus(x):
    """
    Convert a 2D point in euclidean space to a projective space
    Parameters
    ----------
    x : np.Array
        Point in 2D euclidean space
    Returns
    -------
    x : np.Array
        Point in projective space
    """
    assert  (2 == len(x)), 'The argument is not a 2D Point'
    x = np.append(x,1)
    return x


def homogeneus_to_euclidean2D(x):
    """
    Convert a 2D point in projective space to euclidean space
    Parameters
    ----------
    x : np.Array
        Point in projective space
    Returns
    -------
    x : np.Array
        Point in 2D euclidean space
    """
    assert  (3 == len(x)), 'The argument is not a 3D Point'
    assert  (0 != x[2])  , 'x is a point in the infinite, it doesnt '
    x=x/x[2]
    x = np.delete(x,2)
    return x


def crossing_point(line_a, line_b):
    x = np.cross(line_a, line_b)
    return homogeneus_to_euclidean2D(x)


def create_line(point_a, point_b):
    a = euclidean2D_to_homogeneus(point_a)
    b = euclidean2D_to_homogeneus(point_b)
    return np.cross(a, b)


print(crossing_point( np.array([2,6,2]), np.array([-5,8,4]) ))
print(create_line( np.array([-7,-4]), np.array([3,1]) ))
