import math
import numpy as np
import time
import unittest

import utils


class UtilsTest(unittest.TestCase):

    def test_project_point(self):
        ###########################
        # Case 1 - Point above line
        ###########################
        waypoint_1 = [0, 1]
        waypoint_2 = [3, 4]

        line_vec = [waypoint_1, waypoint_2]
        position_x = [1, 4]
        exp_pos_on_vec = np.asarray([2.0, 3.0])

        pos_on_vec = utils.project_point(line_vec,
                                         position_x)
        np.testing.assert_allclose(pos_on_vec,
                                   exp_pos_on_vec)

        ###########################
        # Case 2 - Point below line
        ###########################
        waypoint_1 = [5, 1]
        waypoint_2 = [2, 6]

        line_vec = [waypoint_1, waypoint_2]
        position_x = [2, 3]
        exp_pos_on_vec = np.asarray([3.25, 3.79])

        pos_on_vec = utils.project_point(line_vec,
                                         position_x)
        np.testing.assert_allclose(pos_on_vec,
                                   exp_pos_on_vec,
                                   rtol=1e-01)

        ########################################
        # Case 3 - Edge case - Point behind line
        ########################################
        waypoint_1 = [1, 2]
        waypoint_2 = [4, 3]

        line_vec = [waypoint_1, waypoint_2]
        position_x = [-1, 1]
        exp_pos_on_vec = np.asarray(waypoint_1)

        pos_on_vec = utils.project_point(line_vec,
                                         position_x)
        np.testing.assert_allclose(pos_on_vec,
                                   exp_pos_on_vec)

        ########################################
        # Case 3 - Edge case - Point beyond line
        ########################################
        waypoint_1 = [1, 2]
        waypoint_2 = [4, 3]

        line_vec = [waypoint_1, waypoint_2]
        position_x = [6, 1]
        exp_pos_on_vec = np.asarray(waypoint_2)

        pos_on_vec = utils.project_point(line_vec,
                                         position_x)
        np.testing.assert_allclose(pos_on_vec,
                                   exp_pos_on_vec)

    def test_next_carrot(self):

        waypoint_1 = [0, 1]
        waypoint_2 = [2, 4]

        line_vec = [waypoint_1, waypoint_2]
        pose_2d = [2, 2]
        lookahead_dis = 5.0

        exp_carrot = [3.85, 6.77]

        carrot = utils.next_carrot(line_vec, pose_2d,
                                   lookahead_dis)

        np.testing.assert_allclose(carrot,
                                   exp_carrot,
                                   rtol=1e-01)

    def test_calculate_delta(self):
        #########################
        # Case 1 - First quadrant
        #########################
        position = [2, 2, 0]

        carrot = [3, 4]
        # Limit the steering bound by 90 degrees
        delta_max = math.radians(90)

        exp_delta_degrees = 63.43

        delta = utils.calculate_delta(position,
                                      carrot,
                                      delta_max)

        self.assertAlmostEqual(math.degrees(delta),
                               exp_delta_degrees,
                               places=2)

        #######################
        # Case 2 - 2nd quadrant
        #######################
        position = [2, 2, 0]

        carrot = [1, 5]
        # Limit the steering bound by 180 degrees
        delta_max = math.radians(180)

        exp_delta_degrees = 108.4

        delta = utils.calculate_delta(position,
                                      carrot,
                                      delta_max)

        self.assertAlmostEqual(math.degrees(delta),
                               exp_delta_degrees,
                               places=1)

        #######################
        # Case 3 - 3rd quadrant
        #######################
        position = [2, 2, 0]

        carrot = [1, 1]
        # Limit the steering bound by 60 degrees
        delta_max = math.radians(60)
        # The resulting delta should be negative since we
        # are in the 3rd quadrant.
        exp_delta_degrees = -60

        delta = utils.calculate_delta(position,
                                      carrot,
                                      delta_max)

        self.assertAlmostEqual(math.degrees(delta),
                               exp_delta_degrees,
                               places=1)

        #######################
        # Case 4 - 4th quadrant
        #######################
        position = [2, 2, 0]

        carrot = [3, 1]
        # Limit the steering bound by 60 degrees
        delta_max = math.radians(60)
        # The resulting delta should be negative since we
        # are in the 3rd quadrant.
        exp_delta_degrees = -45

        delta = utils.calculate_delta(position,
                                      carrot,
                                      delta_max)

        self.assertAlmostEqual(math.degrees(delta),
                               exp_delta_degrees,
                               places=1)

        #######################
        # Case 5 - Angle wrap
        #######################

        position = [2, 2, 0]

        carrot = [3, 4]
        # Limit the steering bound by 30 degrees
        delta_max = math.radians(30)

        exp_delta_degrees = 30

        delta = utils.calculate_delta(position,
                                      carrot,
                                      delta_max)

        self.assertAlmostEqual(math.degrees(delta),
                               exp_delta_degrees,
                               places=1)

    def test_update_waypoint_trajectory(self):
        w1 = [0, 1]
        w2 = [2, 1]
        w3 = [2, 4]
        waypoints_array = [w1, w2, w3]
        waypoint_counter = 0

        wp1, wp2, update_traj = \
            utils.update_waypoint_trajectory(waypoints_array,
                                             waypoint_counter)

        self.assertEqual(wp1, w1)
        self.assertEqual(wp2, w2)
        self.assertTrue(update_traj)

        waypoint_counter += 1
        wp1, wp2, update_traj = \
            utils.update_waypoint_trajectory(waypoints_array,
                                             waypoint_counter)

        self.assertEqual(wp1, w2)
        self.assertEqual(wp2, w3)
        self.assertTrue(update_traj)

        waypoint_counter += 1
        wp1, wp2, update_traj = \
            utils.update_waypoint_trajectory(waypoints_array,
                                             waypoint_counter)

        self.assertEqual(wp1, w3)
        self.assertEqual(wp2, w1)
        self.assertTrue(update_traj)

        waypoint_counter += 1
        wp1, wp2, update_traj = \
            utils.update_waypoint_trajectory(waypoints_array,
                                             waypoint_counter)

        self.assertFalse(update_traj)

    def test_calculate_distance(self):
        point1 = [0, 0]
        point2 = [2, 2]
        exp_dist = 2.82

        distance = utils.calculate_distance(point1, point2)
        self.assertAlmostEqual(distance, exp_dist, places=1)

        point1 = [10, 10]
        point2 = [0, 6]
        exp_dist = 10.77

        distance = utils.calculate_distance(point1, point2)
        self.assertAlmostEqual(distance, exp_dist, places=1)


if __name__ == '__main__':
    unittest.main()
