cmake_minimum_required(VERSION 3.8)
project(QUB_visual_URDF)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# ROS2 빌드 시스템
find_package(ament_cmake REQUIRED)

# 설치 규칙 (install rules)
# launch, meshes, urdf, rviz 폴더를 설치 디렉토리로 복사합니다.
install(
  DIRECTORY launch meshes urdf rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()