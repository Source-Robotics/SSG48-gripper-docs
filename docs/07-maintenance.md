# Maintenance

The gripper needs little: every wearing part is printed, so a worn part is replaced by printing a new one, and
the mechanism is a rail, two racks and a pinion that want a little grease now and then. Power the gripper off
before any work on it. Before you open the body, to reach the driver or its termination switch, unplug the
supply and touch earthed metal: static electricity damages the driver.

## Before each session

- The fingers sit tight on their jaw plates and nothing is cracked.
- The cable's M8 nut is tight, the cable has slack for the wrist's full motion and runs clear of the jaws.
- Nothing lies in the jaws' travel, and the gripper calibration finds both end stops.

## When the motion gets rough, and every few months of regular use

- **Grease.** A little lithium grease on the rail and on the rack and pinion. Remove the four screws that hold
  the linear rail to reach the mechanism, wipe off the old grease and the dust, grease, refit, and move the jaws
  over the whole stroke by hand before you power up. A grinding noise, a stiff motion or a calibration that
  stops short of an end are the signs that it is due.
- **Clean** the rail, the racks and the body, as in [Cleaning](#cleaning).
- **Screws**: the finger screws, the rail screws, the lid and the coupler connector; threadlocker where the
  assembly manual uses it.

## Cleaning

Clean the gripper switched off and unplugged. Wipe the body and the fingers with a dry or slightly damp cloth, or with a
little isopropyl alcohol on the cloth for grease; use no other solvents on the printed parts, and never spray or pour anything into the body, where the driver and the motor
are open to it. The gripper is not waterproof or dustproof: keep it out of wet and dusty places, and blow chips
out of the rail rather than wash them out. Grease the rail again if the cleaning took its grease off.

## Replacing worn parts

The fingers, the jaw plates and every other printed part are in the product repository's
[Print files](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Print%20files) folder;
the rail, the carriages and the screws are in the
[BOM](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/BOM). A replacement
finger is the same part as a new one, and the gripper calibration at the next power-up takes care of the end
stops.

A motor or a driver is not serviced but replaced: the motor by the GBM5208-75 of the BOM, after which the motor
calibration of [Driver configuration](build/first-run.md) is run again (the body has to be opened
as in the assembly manual); the driver by a new
[Spectral Micro](https://source-robotics.com/products/spectral-micro-bldc-controller), configured the same way.
