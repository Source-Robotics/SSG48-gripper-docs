# Build guide

**The SSG-48 is open source, and that is important to us.** Everything the gripper is made of is published in the
[product repository](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper) under the Apache 2.0
licence: the STEP files, the printable parts of both hardware versions, the bill of materials with a link for every
item, the assembly manual and video, the fin-ray and pinch fingers, and the URDF and MJCF models. The driver's
firmware and the software that drives the gripper are open source too. A gripper you build is the same gripper as
the one from the shop, and this manual applies to it; design your own fingers on the jaw plate template, or a
coupler connector for a robot the gripper was not designed for. This guide is the order to do it in.

!!! warning
    A self-built gripper is yours to make safe: the thermistor in the windings, the current within what the motor
    stands, and the [Safety](../02-safety.md) chapter apply to it as to a bought one.

## The steps

1. [Bill of materials](bill-of-materials.md): the repository's BOM, with the reference images.
2. [Printing the parts](printing.md): PETG, the V2 set, the fingers in a flexible filament.
3. [Mechanical assembly](mechanical-assembly.md): the manual, page by page, the video, the cable.
4. [Driver setup and first run](first-run.md): the motor calibration and gripper mode during the assembly, then
   the first moves.

## Kits and the shop

You do not have to source everything yourself:

| | What is in it | You add |
|---|---|---|
| [Spectral Micro BLDC starter kit](https://source-robotics.com/products/spectral-micro-bldc-starter-kit) | the Spectral Micro driver, the CANvas USB-to-CAN adapter, the USB-to-serial adapter, an ST-Link with the programming adapter, the UART, power and CAN cables, the 6 × 2.5 mm encoder magnet, the 100K thermistor | the GBM5208-75 motor, the rail and its carriages, the shaft coupler, the M8 connector, the screws and inserts, the printed parts |
| [Spectral Micro driver](https://source-robotics.com/products/spectral-micro-bldc-controller) alone | the driver | the rest, and the adapters its setup needs |
| [Assembled SSG-48 gripper](https://source-robotics.com/products/compliant-gripper) | the gripper, built, calibrated and configured, in black or grey | the fingers, the [cable](https://source-robotics.com/products/gripper-cable), the shaft coupler for PAROL6 |

The starter kit is the good-value start for a build: it has the driver and everything the driver's setup needs,
the CAN adapter for Motor GUI, the serial adapter for the UART, the magnet, the thermistor and the two internal
cables, for little more than the driver alone. The [PAROL6 gripper cable](https://source-robotics.com/products/gripper-cable)
is in the shop too.
