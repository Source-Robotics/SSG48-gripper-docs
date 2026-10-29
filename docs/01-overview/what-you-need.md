# What you need

## The gripper

The SSG-48 is sold assembled, calibrated and configured in the [Source Robotics shop](https://source-robotics.com/products/compliant-gripper).
Everything to build one yourself is open: the STEP and STL files, the assembly manual and the bill of materials in
the [product repository](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper), and the
[Build your own](../guides/build.md) guide.

A bought gripper ships with the current Spectral firmware release and the bootloader installed, its driver
configured for gripper mode and its motor calibrated. It works out of the box; the gripper calibration (finding
the end stops) runs after every power-up and is part of normal use.

## A cable and a 24 V supply

The gripper is powered and controlled through one M8 4-pin cable: 24 V, GND, CANH, CANL.

| Where the gripper goes | Cable |
|---|---|
| PAROL6 | the [PAROL6 gripper cable](https://source-robotics.com/products/gripper-cable) from the shop |
| PAR6 | the PAR6 gripper cable (the shop; coming soon), wired differently from the PAROL6 one |
| a bench, or your own robot | a cable you make from an M8 4-pin connector and four wires, see [The cable](../04-installation/cable.md) |

!!! danger "The two robot cables differ"
    PAROL6 and PAR6 put the four signals on different pins. A cable for the wrong robot, or a self-made cable with
    a wrong pin, puts 24 V where the CAN bus belongs and destroys the gripper's driver. Check the pinout before
    you plug in a cable for the first time.

On the bench, a 24 V supply with a current limit (2 A is plenty for one gripper) is the safest source.

## A CAN interface

The gripper talks CAN. On a robot, the robot's control board provides the bus. On a PC, the
[CANvas USB-to-CAN adapter](https://source-robotics.com/products/canvas-usb-to-can-adapter) does; it shows up as a
serial port and works with the gripper GUI, the Python library and the ROS 2 drivers. Any adapter that
`python-can` supports works with the library.

## Software

- **The gripper GUI**, [SSG-gripper-GUI](https://github.com/Source-Robotics/SSG-gripper-GUI): a Windows build in
  its releases, or the Python source for any platform. The quickest way to test a gripper; see
  [The gripper GUI](../05-setup/gripper-gui.md).
- **Python**: `pip install Spectral-BLDC`, the library the GUI and the ROS 2 drivers are built on; see
  [With Python](../06-operation/python.md).
- **ROS 2**: the [ssg48_adaptive_electric_gripper_ros2](https://github.com/Lass6230/ssg48_adaptive_electric_gripper_ros2)
  package, or the MSG gripper's driver, which speaks the same protocol; see [With ROS 2](../06-operation/ros2.md).
- **PAROL6 and PAR6**: the robots' own software drives the gripper; see [On PAROL6 and PAR6](../06-operation/robots.md).
- **For a self-built gripper**: a 3.3 V USB-to-serial adapter ([serial adapter](https://source-robotics.com/products/usb-to-serial-adapter))
  for the driver's UART port, to configure the driver; see [Driver configuration](../05-setup/driver-configuration.md).

## Optional

- **Fingers** for your objects: the fin-ray and pinch fingers in the repository, or your own on the jaw plate
  template; see [Jaws](../04-installation/jaws.md).
