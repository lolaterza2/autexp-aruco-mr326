import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Recupera i percorsi base
    pkg_mr_robot = get_package_share_directory('mr_26_03_pkg')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    # Usiamo il pacchetto che contiene il modello clonato in src
    pkg_turtlebot3_gazebo = get_package_share_directory('turtlebot3_gazebo')

    # 2. Percorso del mondo
    world_file = os.path.join(pkg_mr_robot, 'worlds', 'MondoProva1.sdf')

    # 3. Percorso del TUO file SDF patchato (quello che hai modificato dentro src)
    # Segue il percorso standard dei modelli cloni:
    sdf_file = os.path.join(
        pkg_turtlebot3_gazebo, 'models', 'turtlebot3_waffle', 'model.sdf'
    )

    # 4. AVVIO DI GAZEBO
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': f'-r {world_file}'}.items()
    )

    # 5. SPAWN DEL TUO TURTLEBOT PATCHATO
    spawn_turtlebot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'turtlebot3_waffle',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.2', 
            '-file', sdf_file
        ],
        output='screen'
    )

    # 6. IL PONTE (Bridge)
    # Usiamo '/teleop/cmd_vel' per il teleop e lo mappiamo su '/cmd_vel' in Gazebo
    # 6. IL PONTE (Bridge)
    # Mappiamo il topic 'cmd_vel' ricevuto da ROS come Twist, 
    # girandolo a Gazebo che lo riceve come Twist.
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan',
            '/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image',
            '/camera/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo'
        ],
        # Aggiungiamo il parametro per forzare la compatibilità
        parameters=[{'qos_overrides./cmd_vel.reliability': 'reliable'}],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_turtlebot,
        bridge
    ])