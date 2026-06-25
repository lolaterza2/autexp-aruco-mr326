FROM ros:jazzy

# --- PACCHETTI BASE (Sintassi del Prof) ---
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

# --- PACCHETTI AGGIUNTIVI PER IL VOSTRO PROGETTO ---
# Computer Vision e Utility
RUN apt update -y && apt install -y ros-jazzy-cv-bridge
RUN apt update -y && apt install -y ros-jazzy-vision-opencv
RUN apt update -y && apt install -y python3-pip
RUN apt update -y && apt install -y git
RUN apt update -y && apt install -y nano

# Installazione librerie Python
RUN pip3 install --break-system-packages "opencv-contrib-python<4.10.0.0" transforms3d

# --- WORKSPACE ---
WORKDIR /root/ros_workspace
RUN apt update -y && apt install -y python3-colcon-common-extensions
RUN apt update -y && apt install -y ros-jazzy-test-msgs

# --- DOWNLOAD MODELLI ARUCO PER GAZEBO HARMONIC ---
RUN mkdir -p /root/.gz/sim/models && \
    cd /root/.gz/sim/models && \
    git clone https://github.com/pal-robotics/aruco_ros && \
    if [ -d "aruco_ros/aruco_description/models" ]; then mv aruco_ros/aruco_description/models/* .; fi && \
    rm -rf aruco_ros

# --- VARIABILI D'AMBIENTE E SETUP FINALE ---
ENV ROS_DOMAIN_ID=30
ENV TURTLEBOT3_MODEL=waffle
ENV GZ_SIM_RESOURCE_PATH=/root/.gz/sim/models

RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc && \
    echo "if [ -f /root/ros_workspace/install/setup.bash ]; then source /root/ros_workspace/install/setup.bash; fi" >> /root/.bashrc

CMD ["/bin/bash"]