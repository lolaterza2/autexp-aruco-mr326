import sys
import rclpy
from rclpy.node import Node
from ros_gz_interfaces.srv import SpawnEntity
from geometry_msgs.msg import Pose

class RobotSpawner(Node):

    def __init__(self):
        super().__init__('robot_spawner')
        
        # Crea un client per il servizio di spawn di Gazebo Harmonic
        self.client = self.create_client(SpawnEntity, '/create')
        
    def spawn_turtlebot(self, x=0.0, y=0.0, z=0.1):
        # Definisce il percorso del file URDF del TurtleBot3 Waffle clonato nel tuo workspace
        urdf_path = '/root/ros_workspace/src/turtlebot3/turtlebot3_description/urdf/turtlebot3_waffle.urdf'
        
        try:
            with open(urdf_path, 'r') as file:
                robot_description = file.read()
        except FileNotFoundError:
            self.get_logger().error(f'Impossibile trovare il file URDF in: {urdf_path}')
            return

        # Prepara la richiesta per il servizio
        request = SpawnEntity.Request()
        request.name = 'turtlebot3_waffle'
        request.xml = robot_description
        request.robot_namespace = ''
        
        # Imposta la posa iniziale
        initial_pose = Pose()
        initial_pose.position.x = x
        initial_pose.position.y = y
        initial_pose.position.z = z
        request.initial_pose = initial_pose

        self.get_logger().info(f'Invio richiesta di spawn per {request.name} a coordinate ({x}, {y}, {z})...')
        
        # Chiamata asincrona al servizio
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        
        if future.result() is not None:
            self.get_logger().info('Spawn completato con successo!')
        else:
            self.get_logger().error('Fallimento durante lo spawn del robot.')

def main(args=None):
    rclpy.init(args=args)
    spawner = RobotSpawner()
    
    # Puoi cambiare le coordinate di spawn direttamente da qui
    spawner.spawn_turtlebot(x=0.0, y=0.0, z=0.1)
    
    spawner.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()