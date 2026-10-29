# Driver configuration for a self-built gripper

A gripper from the shop arrives with its driver configured: the motor calibrated, gripper mode on, the
thermistor on, everything saved. A gripper you build has a bare Spectral Micro driver that must be brought to the
same state once, over its UART port. This page is that procedure; the commands are the driver's, and the
[Spectral Micro documentation](https://docs.source-robotics.com/Spectral-BLDC-docs/) explains each in depth.

## What you need

- The driver mounted on the motor with its encoder magnet, before the pinion is engaged in the racks: the motor
  calibration turns the motor several revolutions in both directions, which the racks cannot follow. Do this
  step with the motor out of the body or with the pinion not yet meshing.
- A 3.3 V [USB-to-serial adapter](https://source-robotics.com/products/usb-to-serial-adapter) on the driver's
  UART connector, a terminal at 256000 baud with CR+LF line endings, and 24 V on the driver's power connector.
  [The serial terminal](https://docs.source-robotics.com/Spectral-BLDC-docs/latest/05-setup/terminal/) on the
  Spectral Micro site shows the terminal setup.
- The thermistor, soldered to the driver's thermistor pads and placed in the motor's windings with thermal
  cement.

## With Motor GUI

[Motor GUI](motor-gui.md), connected over **UART** through the serial adapter, has an *SSG-48* preset on its
setup page. It writes the motor's 11 pole pairs, the current limit, the loop gains of a calibrated shop gripper
(`#Kpiq 7.0381`, `#Kiiq 4.2557`), gripper mode, the thermistor and the CAN ID, then saves; its CAN ID is 6, the
PAR6 gripper's, so change it before applying for another robot. Apply it after the motor calibration of
step 1: it does step 2 for you.

## 1. The motor calibration

Restore the defaults first, so that nothing from another motor or junk in the EEPROM goes into the calibration,
then calibrate. The Spectral Micro measures the motor's resistance and inductance and finds its pole pairs by
itself; nothing is entered:

```
#Default
#Cal
```

The motor clicks, then turns, the driver prints each step and ends with `Calibration success!`. The whole routine
and its messages are in [Calibration](https://docs.source-robotics.com/Spectral-BLDC-docs/latest/05-setup/calibration/)
on the Spectral Micro site. `#Default` also resets the serial number the driver reports; note what `#Info` printed
if you need it.

## 2. The gripper settings

```
#Gripper 1
#Term 1
#Tlim 75
#CANID 0
#Save
```

| Command | What it does |
|---|---|
| `#Gripper 1` | gripper mode: the driver runs the gripper state machine and answers the gripper messages |
| `#Term 1`, `#Tlim 75` | the thermistor on, the temperature limit at 75 °C. Without it the motor can burn out under a long grip |
| `#CANID 0` | the node ID on the robot's bus; 0 to 13, see [Over CAN](../06-operation/can.md) |
| `#Save` | nothing above survives a power cycle until it is saved |

The current loop gains the calibration computes for the motor are what the shipped grippers use.

## 3. Assemble and calibrate the gripper

Fit the pinion and assemble the gripper, power it up, and run the gripper calibration (`#Gripcal`, or Motor GUI's
**Calibrate**): the jaws open fully and close fully. Then a first move at a low current, as in
[Calibrate, activate, move](first-moves.md). `#Gripinfo` prints the gripper's state, including the end stops the
calibration found.

## Current limit

The gripper's moves use the current limit of each command, not the driver's `#Ilim`. The firmware does not clamp
it; [Force and speed](../03-technical-data/force-and-speed.md) says what is safe for the motor.
