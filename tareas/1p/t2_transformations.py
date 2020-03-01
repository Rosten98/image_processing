import numpy as np
from tarea1 import *

def grades_to_radians(deg):
    rad = (deg*np.pi)/180
    return rad


def translate(point, new_point):
    assert (len(point) == 2), ' Original point is not a 2D point '
    assert (len(new_point) == 2), ' Translated point is not a 2D point '

    point = np.array([[1, 0, point[0]],[0, 1, point[1]]])
    new_point = euclidean2D_to_homogeneus(new_point)
    return point@new_point


def rotate(point, deg):
    assert (len(point) == 2), ' Point is not a 2D point '
    angle = grades_to_radians(deg)
    rotation_matrix = np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
    return point@rotation_matrix


def rotate_translate(point, new_point, deg):
    assert (len(point) == 2), ' Original Point is not a 2D point '
    assert (len(new_point) == 2), ' Translated point is not a 2D point '
    angle = grades_to_radians(deg)
    RT = np.array([[np.cos(angle),-np.sin(angle),new_point[0]],[np.sin(angle),np.cos(angle),new_point[1]]])
    point = euclidean2D_to_homogeneus(point)
    return RT@point


def rot_tra_scale(point, new_point, deg, scale_factor):
    assert (len(point) == 2), ' Original Point is not a 2D point '
    assert (len(new_point) == 2), ' Translated point is not a 2D point '
    angle = grades_to_radians(deg)
    sRT = np.array([[np.cos(angle),-np.sin(angle),new_point[0]],[np.sin(angle),np.cos(angle),new_point[1]]])
    sRT *= scale_factor
    point = euclidean2D_to_homogeneus(point)
    return sRT@point


point = np.array([5, 5])
translated_point = np.array([1, 1])
deg_to_rotate = 90
scale_factor = 2
print("Translation", translate(point, translated_point))
print("Rotation", rotate(point, deg_to_rotate))
print("Rotation & Translation", rotate_translate(point, translated_point, deg_to_rotate))
print("Rotation, Translation & Scale", rot_tra_scale(point, translated_point, deg_to_rotate, scale_factor))
