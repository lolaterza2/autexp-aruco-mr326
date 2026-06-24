import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # 1. Definiamo i pacchetti di riferimento
    pkg_ros_gz_sim = FindPackageShare('ros_gz_sim')
    pkg_my_project = FindPackageShare('prova1') # <--- Il tuo pacchetto

    # 2. Percorso del launch file di Gazebo Sim e del tuo mondo (.sdf)
    gz_launch_path = PathJoinSubstitution([pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'])
    world_path = PathJoinSubstitution([pkg_my_project, 'worlds', 'mondoProva1.sdf'])

    return LaunchDescription([
        # Se hai modelli custom o mesh nella cartella del tuo pacchetto, serve questo:
        SetEnvironmentVariable(
            'GZ_SIM_RESOURCE_PATH',
            PathJoinSubstitution([pkg_my_project, 'worlds'])
        ),

        # Includiamo il simulatore Gazebo con il tuo mondo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_launch_path),
            launch_arguments={
                'gz_args': ['-r ', world_path],
                'on_exit_shutdown': 'True'
            }.items(),
        ),

        # --- IL TUO NODO PYTHON DI SPAWN ---
        Node(
            package='prova1',
            executable='robot_spawner',
            output='screen'
        ),

        # --- ROS GZ BRIDGE ---
        # Questo nodo fa da traduttore tra Gazebo (GZ) e ROS2 Jazzy.
        # Dobbiamo mappare i sensori del TurtleBot3 Waffle e i comandi di movimento.
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[
                # Notazione: /topic_ros@tipo_msg_ros@tipo_msg_gz
                '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan',
                '/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image',
                '/camera/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo',
                '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
                '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
                '/tf@tf2_msgs/msg/TFMessage@gz.msgs.Pose_V',
                '/clock@rosgraph_msgs/msg/Clock@gz.msgs.Clock'
            ],
            remappings=[
                # Se i plugin di TurtleBot o Nav2 cercano i topic standard, 
                # non serve fare grossi remapping, basta lasciarli così.
                # Se Gazebo pubblica su /intel_realsense_r200/image_raw, lo rimappi qui in /camera/image_raw
            ],
            output='screen'
        ),
    ])