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

## Authors

Borys Ovsiyenko, Pavel Sashko, Abdelrahman Tayel
