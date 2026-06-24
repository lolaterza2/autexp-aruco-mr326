# Autonomous Exploration and Aruco Markers Mapping
Objective:
To develop an autonomous exploration system based on ROS2 that enables a mobile robot to navigate and explore an unknown simulated environment while detecting and localizing ArUco markers distributed throughout the map.
The robot will autonomously explore the environment using frontier-based exploration techniques, avoid obstacles through the ROS2 Navigation Stack, and continuously build knowledge of the environment. Whenever an ArUco marker enters the camera field of view, the robot will detect it using OpenCV-based computer vision algorithms, estimate its pose with respect to the camera frame, and record its position within the map.
The final system will produce a list (and optionally a visualization) of all detected markers and their estimated locations in the environment.

