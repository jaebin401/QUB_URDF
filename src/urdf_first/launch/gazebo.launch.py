import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    # 1. 패키지 경로 및 URDF 파일 설정
    package_name = 'urdf_first'
    urdf_file_name = 'URDF.urdf'

    pkg_path = get_package_share_directory(package_name)
    urdf_path = os.path.join(pkg_path, 'urdf', urdf_file_name)

    # 2. URDF 파일 읽기
    with open(urdf_path, 'r') as infp:
        robot_desc = infp.read()

    # 3. Gazebo 실행 프로세스
    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    # 4. 로봇 소환 (Spawn Entity) 노드
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description',
                   '-entity', 'my_humanoid_robot'], # Gazebo에 표시될 이름
        output='screen'
    )

    # 5. Robot State Publisher 노드 (TF 트리를 발행)
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True, 'robot_description': robot_desc}],
        arguments=[urdf_path]
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_entity,
    ])