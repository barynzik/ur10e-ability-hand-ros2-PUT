# UR10e + Ability Hand (ROS 2 Jazzy)

## Overview

This project integrates the UR10e robotic manipulator with the Ability Hand in ROS 2 Jazzy.

The system includes:

* UR10e robot simulation
* Ability Hand attached to the UR flange
* Gazebo Harmonic simulation
* MoveIt 2 motion planning
* ROS 2 Control integration
* Hand trajectory controller
* Simulation environment with a table and object

## Features

### Robot Simulation

The UR10e robot is simulated in Gazebo Harmonic using ROS 2 Jazzy.

### Ability Hand Integration

The Ability Hand is attached to the robot flange through a Xacro macro and controlled through ROS 2 controllers.

### Motion Planning

MoveIt 2 is used for trajectory planning and execution of the robot arm.

### Hand Control

The hand is controlled through a FollowJointTrajectory action interface.

## Demo

Video demonstration:

[Here](https://youtu.be/CoGPBiiDnmY)

## Repository Structure

```text
ur10e_with_hand/
ur10e_with_hand_moveit_config/
ur_simulation_gz/
```

## Technologies

* ROS 2 Jazzy
* Gazebo Harmonic
* MoveIt 2
* ros2_control
* Xacro
* UR10e
* Ability Hand

## Running the project

### Allow Docker to access the display

```bash
xhost +local:docker
```

## Running the project

### Allow Docker to access the display

```bash
xhost +local:docker
```

### Launch Gazebo

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash

export GZ_SIM_RESOURCE_PATH=$HOME/ros2_ws/src/ability-hand-ros2/src:$HOME/ros2_ws/src/ability-hand-ros2/src/ah_urdf:$GZ_SIM_RESOURCE_PATH

ros2 launch ur_simulation_gz ur_sim_control.launch.py \
description_file:=$HOME/ros2_ws/src/ur_simulation_gz/ur_simulation_gz/urdf/ur_gz_with_hand.urdf.xacro \
world_file:=$HOME/ros2_ws/src/ur_simulation_gz/ur_simulation_gz/worlds/table_world.sdf
```

### Launch MoveIt

```bash
ros2 launch ur10e_with_hand_moveit_config move_group.launch.py use_sim_time:=true
```

### Launch RViz

```bash
ros2 launch ur10e_with_hand_moveit_config moveit_rviz.launch.py
```

## Authors

Borys Ovsiyenko, Pavel Sashko, Abdelrahman Tayel
