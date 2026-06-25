import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'mr_26_03_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # --- AGGIUNTE FONDAMENTALI ---
        # Include tutti i file di launch
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        
        # Include i file del mondo di Gazebo (.sdf)
        (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*'))),
        
        # Include le mappe di Nav2 (opzionale adesso, ma vi servirà a brevissimo)
        (os.path.join('share', package_name, 'maps'), glob(os.path.join('maps', '*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='Progetto Mobile Robotics 26_03',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Qui è dove registreremo i vostri script Python futuri (es. OpenCV e Frontiere)
            # 'opencv_node = mr_26_03_pkg.opencv_node:main',
        ],
    },
)