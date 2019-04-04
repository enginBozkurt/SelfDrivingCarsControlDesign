import numpy as np

from math import pi
from numpy import linalg as LA


def project_point(vector, point):
    """Given a line vector and a point, projects the point
    on the line, resulting to a point that is closest to
    the given point.

    Args:
        vector: A 2D array of points in the form [[x1, y1], [x2, y2]]
        point: A 2D point in the form [x, y]

    Returns:
        closest_point: A 2D point in the form [x, y] that lies on
            given vector.
    """

    p0 = vector[0]
    p1 = vector[1]

    v1 = np.subtract(point, p0)
    v2 = np.subtract(p1, p0)

    distance = np.dot(v1, v2) / np.power(LA.norm(v2), 2)

    if distance < 0.0:
        closest_point = p0
    elif distance > 1.0:
        closest_point = p1
    else:
        closest_point = p0 + distance * v2

    return closest_point


def next_carrot(vector, pose_2d, lookahead_dis):
    """Given a line vector, position and look-ahead distance,
    determine the next carrot point.

    Args:
        vector: A 2D array of points in the form [[x1, y1], [x2, y2]]
        pose_2d: A 2D point in the form [x, y]
        lookahead_dis: A float distance determining how far ahead
            we want to look.

    Returns:
        carrot: A 2D point in the form [x, y].
    """
    p0 = vector[0]
    p1 = vector[1]

    projected_point = project_point(vector, pose_2d)

    # Calculate unit vector of trajectory
    vec_diff = np.subtract(p1, p0)
    unit_vec = vec_diff / LA.norm(vec_diff)

    carrot = projected_point + lookahead_dis * unit_vec
    return carrot


def calculate_delta(position, carrot, delta_max):
    """Given a 2D position and carrot pose, determine the steering
    angle delta.
    This angle should be constrained by `delta_max`, determined based
    on the model. For instance for a car, this will depend on the properties
    of the car (for instance using Ackermann steering geometry you can
    calculate the center of the turning circle).

    Args:
        position: A 2D array of points in the form [[x1, y1], [x2, y2]]
        carrot: A 2D point in the form [x, y]
        delta_max: A float distance determining how far ahead we want to look.

    Returns:
        delta: A float representing the steering angle in unit radians.
    """

    theta = position[2]

    # Calculate the angle between position and carrot
    x = carrot[0] - position[0]
    y = carrot[1] - position[1]
    angle_of_vec = np.arctan2(y, x)

    # Limit delta to pi and -pi
    delta = -(theta - angle_of_vec)
    delta = np.mod(delta + pi, 2 * pi) - pi

    # Limit delta to steering angle max
    if delta > delta_max:
        delta = delta_max
    elif delta < -delta_max:
        delta = -delta_max

    return delta


def update_waypoint_trajectory(waypoints, waypoint_counter):
    """Given a list of waypoints, and waypoint_counter, determine
    the next set up waypoints.

    Args:
        waypoints: An array of waypoints in the format [wp1, wp2, ..., wpn]
            where each wp is a 2D point in the form [x, y].
        waypoint_counter: A counter representing a pointer to the current
            waypoint. This should not exceed the total size of waypoint_counter.

    Returns:
        wp1 : First waypoint of the updated trajectory.
        wp2: Second waypoint of the updated trajectory.
        update_trajectory: A flag to determine whether we should continue.
    """

    update_trajectory = True
    if waypoint_counter >= len(waypoints):
        print('Ran out of waypoints.')
        update_trajectory = False
        wp1 = wp2 = None

    elif waypoint_counter == len(waypoints) - 1:
        # Grab the last waypoint and the initial to get back
        # to the starting point
        wp1 = waypoints[waypoint_counter]
        wp2 = waypoints[0]

    else:
        wp1 = waypoints[waypoint_counter]
        wp2 = waypoints[waypoint_counter + 1]

    return wp1, wp2, update_trajectory


def calculate_distance(point1, point2):
    """Given two 2D points, calculate the distance.

    Args:
        point1: A 2D array in the form [x, y]
        point2: A 2D array in the form [x, y]

    Returns:
        distance: A float representing the distance between
            the points.
    """

    distance = np.sqrt(np.power((point2[1] - point1[1]), 2) +
                       np.power((point2[0] - point1[0]), 2))
    return distance
