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
    assert(4 == len(q1)), 'The argument taken is not a 3D point'
    assert(4 == len(q2)), 'The argument taken is not a 3D point'
    (w1,x1,y1,z1) = q1
    (w2,x2,y2,z2) = q2
    w = (w1*w2 - x1*x2 - y1*y2 - z1*z2)
    x = (w1*x2 + x1*w2 + y1*z2 - z1*y2)
    y = (w1*y2 - x1*z2 + y1*w2 + z1*x2)
    z = (w1*z2 + x1*y2 - y1*x2 + z1*w2)
    qx = [w,x,y,z]
    return qx


def rotation_vector(qr):
    assert(4 == len(qr)), 'The argument taken is not a valid point'
    assert(qr[0] >= -360 or qr[0] <= 360), 'The degree to convert is not valid'
    rad = grades_to_radians(qr[0])
    qr = np.array([np.cos(rad/2),qr[1],qr[2],qr[3]])
    return qr


def quaternions(qx,qr,qp):
    assert(4 == len(qp)), 'The argument taken is not a valid point'
    assert(4 == len(qx)), 'The argument taken is not a valid point'
    q_asterisk = np.array([qx[0],(qx[1]*-1),(qx[2]*-1),(qx[3]*-1)])
    q_abs = np.array([qx[0]**2,qx[1]**2,qx[2]**2,qx[3]**2])
    qi = q_asterisk / q_abs
    qpq_ = qr * qp * qi
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
q1 = np.array([1,3,5,7])
q2 = np.array([2,4,6,8])
qx = q_multiply(q1,q2)
print('q1 * q2: ',qx)
qr = np.array([90,5,5,5])
qr = rotation_vector(qr)
print('The rotation vector is: ',qr)
qp = np.array([5,5,5,5])
print('The point quaternion is: ',quaternions(qx,qr,qp))

# q1 * q2:  [-96, 8, 20, 20]
# The rotation vector is:  [0.70710678 5.         5.         5.        ]
# The rotated quaternion is:  [-0.03682848 -3.125      -1.25       -1.25      ]
