FROM ros:jazzy
 
# --- PACCHETTI BASE ---
RUN apt update -y && apt install ros-jazzy-turtlesim* -y
RUN apt update -y && apt install -y ros-jazzy-rqt-graph
RUN apt update -y && apt install -y wget
RUN apt update -y && apt install -y ros-jazzy-urdf-tutorial
RUN apt update -y && apt install -y liburdfdom-tools
# install gazebo
RUN apt update -y && apt install -y ros-jazzy-ros-gz
# install navigation stuff
RUN apt update -y && apt install -y ros-jazzy-navigation2 \
    ros-jazzy-nav2-bringup ros-jazzy-cartographer \
    ros-jazzy-cartographer-ros
 
# Installazione pacchetti visione e utility
RUN apt update -y && apt install -y ros-jazzy-cv-bridge ros-jazzy-vision-opencv python3-pip git nano
# Installazione librerie Python (con flag per scavalcare il blocco di sistema su Ubuntu 24.04/Jazzy)
RUN pip3 install --break-system-packages "opencv-contrib-python<4.10.0.0" transforms3d
# --- WORKSPACE E DIPENDENZE ---
WORKDIR /root/ros_workspace
RUN apt update -y && apt install -y python3-colcon-common-extensions
RUN apt update -y && apt install -y ros-jazzy-test-msgs
 
# --- CLONAZIONE PACCHETTI TURTLEBOT3 ---
WORKDIR /root/ros_workspace/src
RUN git clone -b jazzy https://github.com/ROBOTIS-GIT/DynamixelSDK.git
RUN git clone -b jazzy https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
RUN git clone -b jazzy https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
RUN git clone -b jazzy https://github.com/ROBOTIS-GIT/turtlebot3.git
 
# Compilazione del workspace
WORKDIR /root/ros_workspace
RUN . /opt/ros/jazzy/setup.sh && colcon build --symlink-install
 
# --- DOWNLOAD MODELLI ARUCO PER GAZEBO ---
RUN mkdir -p /root/.gazebo/models && \
    cd /root/.gazebo/models && \
    git clone https://github.com/pal-robotics/aruco_ros && \
    if [ -d "aruco_ros/aruco_description/models" ]; then mv aruco_ros/aruco_description/models/* .; fi && \
    rm -rf aruco_ros
 
# --- VARIABILI D'AMBIENTE E SETUP FINALE ---
ENV ROS_DOMAIN_ID=30
ENV TURTLEBOT3_MODEL=waffle
ENV ROS_WS=/root/ros_workspace
 
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc && \
    echo "source /usr/share/gazebo/setup.sh" >> /root/.bashrc && \
    echo "source /root/ros_workspace/install/setup.bash" >> /root/.bashrc
 
WORKDIR /root/ros_workspace
CMD ["/bin/bash"]