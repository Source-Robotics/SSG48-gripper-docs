# Build your own

Everything about the gripper is open: the STEP and STL files, the bill of materials, the assembly manual and
video, and the driver's firmware. This guide is the order to do it in; the details live in the
[product repository](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper).

!!! warning
    A self-built gripper is yours to make safe: the thermistor in the windings, the current within what the motor
    stands, and the [Safety](../02-safety.md) chapter apply to it as to a bought one.

## 1. Print the parts

The [Gripper STL parts](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Gripper%20STL%20parts)
folder has the printable parts of both hardware versions; print the `V2` set (the large-bearing version, see
[Hardware versions](../01-overview/hardware-versions.md)), the two jaws, the guide cover, and the coupler
connector for your robot. PETG for the body; the fin-ray fingers in a flexible filament.

## 2. Source the rest

The [BOM](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/blob/main/BOM/BOM.md) lists every
part with a link: the GBM5208-75 gimbal motor, the Spectral Micro driver, the encoder magnet, the MGN7 rail and
two carriages, the shaft coupler, the M8 connector and the short XH and ZH cables that connect the driver inside,
the brass inserts and the screws. The motor's datasheet is in the
[Assembly manual](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Assembly%20manual)
folder.

## 3. Prepare the driver

Before the pinion goes in: mount the driver on the motor with its magnet, calibrate the motor, set up gripper
mode and the thermistor, and save. [Driver configuration](../05-setup/driver-configuration.md) is the procedure;
the magnet and the driver's mounting are in the
[Spectral Micro documentation](https://docs.source-robotics.com/Spectral-BLDC-docs/latest/04-mounting/). Place the
thermistor bead in the windings with thermal cement and route its leads to the driver's thermistor pads.

## 4. Assemble

Follow the [assembly manual](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/blob/main/Assembly%20manual/Gripper_assembly_manual.pdf)
or the [assembly video](https://www.youtube.com/watch?v=127zXHKuqIg). The rail with its two carriages goes into
the body, the jaws onto the carriages, the motor with the pinion into the body so that the pinion meshes with
both racks, the driver's power and CAN cables to the M8 connector, the lid and the coupler connector on the back.

## 5. The cable

An M8 4-pin cable to your robot or your supply and CAN adapter; [The cable](../04-installation/cable.md) has the
wiring diagrams and the warning about the two robots' cables.

## 6. First power-up

Power up, calibrate the gripper, activate it and move it at a low current, as in
[Calibrate, activate, move](../05-setup/first-moves.md). If the calibration does not find both end stops, the
mechanism is too stiff: loosen the rail, check the pinion's depth in the racks, grease.
