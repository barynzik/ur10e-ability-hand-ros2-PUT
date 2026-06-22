cmake_minimum_required(VERSION 3.8)
project(ur10e_with_hand)
find_package(ament_cmake REQUIRED)
install(DIRECTORY urdf launch
  DESTINATION share/${PROJECT_NAME}
)
ament_package()
