# What you need

## The gripper: buy it, or build it

The SSG-48 is sold assembled, calibrated and configured in the [Source Robotics shop](https://source-robotics.com/products/compliant-gripper).
A bought gripper ships with the current Spectral firmware release and the bootloader installed, its driver
configured for gripper mode and its motor calibrated. It works out of the box; the gripper calibration (finding
the end stops) runs after every power-up and is part of normal use.

### Build your own { #build-your-own }

**The SSG-48 is open source, and that is important to us.** Everything the gripper is made of is published in the
[product repository](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper) under the Apache 2.0
licence: the STEP files, the printable parts of both hardware versions, the bill of materials with a link for every
item, the assembly manual and video, the fin-ray and pinch fingers, and the URDF and MJCF models. The driver's
firmware and the software that drives the gripper are open source too. A gripper you build is the same gripper as
the one from the shop, and this manual applies to it; and you can design your own fingers on the jaw plate
template, or a coupler connector for a robot the gripper was not designed for.

| Step | Where |
|---|---|
| 1. Print the parts: the `V2` set (the large-bearing version, see [Hardware versions](hardware-versions.md)), the two jaws, the guide cover and the coupler connector for your robot. PETG for the body; a flexible filament for the fin-ray fingers | [Gripper STL parts](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Gripper%20STL%20parts) |
| 2. Source the rest: the GBM5208-75 gimbal motor, the Spectral Micro driver, the encoder magnet, the MGN7 rail and two carriages, the shaft coupler, the M8 connector and the internal cables, the brass inserts and the screws | [BOM](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/blob/main/BOM/BOM.md); the motor's datasheet is in the [Assembly manual](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Assembly%20manual) folder |
| 3. Configure the driver before the pinion goes in: the motor calibration, gripper mode, the thermistor | [Driver configuration](../05-setup/driver-configuration.md) |
| 4. Assemble | [Assembly manual](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/blob/main/Assembly%20manual/Gripper_assembly_manual.pdf), [assembly video](https://www.youtube.com/watch?v=127zXHKuqIg) |
| 5. Cable it, calibrate, make the first moves | [The cable](../04-installation/cable.md), [Calibrate, activate, move](../05-setup/first-moves.md) |

!!! warning
    A self-built gripper is yours to make safe: the thermistor in the windings, the current within what the motor
    stands, and the [Safety](../02-safety.md) chapter apply to it as to a bought one.

If the calibration of a self-built gripper does not find both end stops, the mechanism is too stiff: loosen the
rail, check the pinion's depth in the racks, grease.

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
serial port and works with Motor GUI, the Python library and the ROS 2 drivers. Any adapter that `python-can` supports works
with the library.

## Software

- **Motor GUI**, [motorgui.com](https://motorgui.com/), in the browser over the CANvas adapter: the recommended
  tool to test and set up a gripper, with a gripper panel for the SSG-48 and the MSG; see
  [Motor GUI](../05-setup/motor-gui.md). The earlier [SSG-gripper-GUI](https://github.com/Source-Robotics/SSG-gripper-GUI),
  a Python program, is legacy.
- **Python**: `pip install Spectral-BLDC`, the library the ROS 2 drivers are built on; see
  [With Python](../06-operation/python.md).
- **ROS 2**: the [ssg48_adaptive_electric_gripper_ros2](https://github.com/Lass6230/ssg48_adaptive_electric_gripper_ros2)
  package, or the MSG gripper's driver, which speaks the same protocol; see [With ROS 2](../06-operation/ros2.md).
- **PAROL6 and PAR6**: the robots' own software drives the gripper; see [On PAROL6 and PAR6](../06-operation/robots.md).
- **For a self-built gripper**: a 3.3 V USB-to-serial adapter ([serial adapter](https://source-robotics.com/products/usb-to-serial-adapter))
  for the driver's UART port, to configure the driver with Motor GUI or a terminal; see
  [Driver configuration](../05-setup/driver-configuration.md).

## Optional

- **Fingers** for your objects: the fin-ray and pinch fingers in the repository, or your own on the jaw plate
  template; see [Jaws](../04-installation/jaws.md).
