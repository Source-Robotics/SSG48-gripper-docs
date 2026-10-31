# With ROS 2

Two ROS 2 packages drive the gripper; both are built on the Python library and a `python-can` adapter.

## The SSG-48 package

[ssg48_adaptive_electric_gripper_ros2](https://github.com/Lass6230/ssg48_adaptive_electric_gripper_ros2), written
for this gripper by Lasse Stubbe Ebbesen, with example nodes. Its README has the installation, the topics and
the parameters.

## The MSG gripper's package

[msg_gripper_ros2](https://github.com/Source-Robotics/source_robotics_msg_gripper_ros2), a ROS 2 Humble driver
written for the MSG gripper by the UCLA Biomechatronics Lab and Ben Forbes. The SSG-48 speaks the same protocol,
so it works with it as well:

| Direction | Topic or action | Type |
|---|---|---|
| Command | `/gripper/command_joint_states` | `sensor_msgs/JointState`, the position in the gripper's own units, 0 to 255 |
| Feedback | `/gripper/feedback_joint_states` | `sensor_msgs/JointState`, the position in the same units and the effort in mA |
| Action | `/gripper_command` | `control_msgs/GripperCommand` |

Ubuntu 22.04 with ROS 2 Humble, Python 3.10 or newer, and a USB-to-CAN adapter that speaks slcan, such as the
CANvas:

```bash
pip install Spectral_BLDC python-can
cd ~/ros2_ws/src
git clone https://github.com/Source-Robotics/source_robotics_msg_gripper_ros2.git
cd ~/ros2_ws
colcon build --packages-select msg_gripper_ros2
source install/setup.bash
ros2 launch msg_gripper_ros2 msg_gripper_launch.py
```

The only setting that depends on your machine is the adapter's port, `channel` in `config/default.yaml`:
`/dev/ttyACM0` or `/dev/ttyUSB0` on Linux, `/dev/tty.usbmodem*` on macOS, `COM3` on Windows. On Linux, add
yourself to the `dialout` group to open the port without `sudo`.

## The description files

The URDF and the MJCF of the gripper for ROS 2, Gazebo and MuJoCo are in the product repository's
[SSG48_gripper_description](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/SSG48_gripper_description).
