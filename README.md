mkdir -p ros_ws/src
./clone.sh
###spostare i file clonati in ros_ws/src
##sostituire nel file ros_ws/src/turtlebot3_simulations/turtlebot3_gazebo/models/turtlebot3_waffle/model.sdf gli ultimi due plugin

<plugin filename="gz-sim-diff-drive-system" name="gz::sim::systems::DiffDrive">
      <left_joint>wheel_left_joint</left_joint>
      <right_joint>wheel_right_joint</right_joint>
      <wheel_separation>0.287</wheel_separation>
      <wheel_radius>0.033</wheel_radius>
      <topic>/turtlebot3/cmd_vel</topic> 
     </plugin>
    
    <plugin filename="gz-sim-joint-state-publisher-system" name="gz::sim::systems::JointStatePublisher">
      <topic>joint_states</topic>
      <joint_name>wheel_left_joint</joint_name>
      <joint_name>wheel_right_joint</joint_name>
    </plugin>



cd docker_ws
./build.sh
./run.sh
cd ~/ros_workspace/src
ros2 pkg create --build-type ament_cmake mr_26_03_pkg --dependencies rclcpp geometry_msgs sensor_msgs
#crea nel pacchetto le cartelle launch, world. inserisci dentro il fila launch e il mondoprova1 rispettivamente
modifica il file setup.py con quello nel git
colcon build --symlink-install
source install/setup.bash
ros2 launch mr_26_03_pkg simulation.launch.py
#################################################
per testare teleop
./exec.sh

##non si muove con wasd...boh
ros2 run turtlebot3_teleop teleop_keyboard

ros2 run turtlebot3_teleop teleop_keyboard --ros-args -r cmd_vel:=/teleop/cmd_vel

ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/cmd_vel
#################################################