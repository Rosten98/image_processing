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


def q_multiply(q1,q2):
    (w1,x1,y1,z1) = q1
    (w2,x2,y2,z2) = q2
    w = (w1*w2 - x1*x2 - y1*y2 - z1*z2)
    x = (w1*x2 + x1*w2 + y1*z2 - z1*y2)
    y = (w1*y2 - x1*z2 + y1*w2 + z1*x2)
    z = (w1*z2 + x1*y2 - y1*x2 + z1*w2)
    qx = [w,x,y,z]
    return qx


def q_asterisk(q):
    q = np.array([q[0],(q[1]*-1),(q[2]*-1),(q[3]*-1)])
    return q


def q_abs(q):
    q = q[0]**2 + q[1]**2 + q[2]**2 + q[3]**2
    return q


def q_inverse(q_abs, q_asterisk):
    (w, x, y, z) = q_asterisk
    q  = np.array([w/q_abs, x/q_abs, y/q_abs, z/q_abs])
    return q


def rotation_vector(qr):
    rad = grades_to_radians(qr[0])
    qr = np.array([np.cos(rad/2),qr[1],qr[2],qr[3]])
    return qr


def quaternion(axis, rad):
    q = np.array([np.cos(rad/2), axis[0], axis[1], axis[2]])
    return q


def rotate3D(point, axis, deg):
    rad = grades_to_radians(deg)
    q = quaternion(axis, rad)
    q_ast = q_asterisk(q)
    q_ab = q_abs(q)
    q_inv = q_inverse(q_ab, q_ast)
    point = np.append(0, point)
    qp = q_multiply(q, point)
    qpq_ = q_multiply(qp, q_inv)
    del qpq_[0]
    return qpq_


point = np.array([5, 5])
translated_point = np.array([1, 1])
deg_to_rotate = 90
scale_factor = 2
print("Translation", translate(point, translated_point))
print("Rotation", rotate(point, deg_to_rotate))
print("Rotation & Translation", rotate_translate(point, translated_point, deg_to_rotate))
print("Rotation, Translation & Scale", rot_tra_scale(point, translated_point, deg_to_rotate, scale_factor))

# Quaternions
# Quaternions
point = np.array([5, 5, 10])
axis = np.array([1, 1, 1])
deg = 180
print('The rotated quaternion is: ', rotate3D(point, axis, deg))
