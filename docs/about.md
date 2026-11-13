# About this manual

The SSG-48 Gripper Manual covers the SSG-48 adaptive electric gripper from unpacking to a gripper that works on a robot: mounting and cabling, the
first setup with Motor GUI, control over CAN and UART, from Python, from ROS 2 and from the PAROL6 and PAR6
robots, and firmware updates. It is written for a maker, a student or an engineer who can plug in a cable and run
a Python script. Read [Safety](02-safety.md) before you power anything; [First setup](05-setup/index.md) is the
shortest path to a gripper that moves.

The gripper is a Spectral Micro BLDC driver in gripper mode. The driver itself, from its full command set to its calibration
and its bootloader, is documented on the [Spectral site](https://docs.source-robotics.com/Spectral-BLDC-docs/); this manual links there instead of
repeating it.

## Finding your way

--8<-- "navigation.md"

## Warnings and notes

--8<-- "symbols.md"

## Related documents

<!-- documents-table -->

The driver inside the gripper is documented at [https://docs.source-robotics.com/Spectral-BLDC-docs/](https://docs.source-robotics.com/Spectral-BLDC-docs/). The MSG gripper, the SSG-48's successor on the STEPFOC stepper driver, is at [docs.source-robotics.com/MSG-gripper-docs](https://docs.source-robotics.com/MSG-gripper-docs/). The robots the gripper is
made for: [docs.source-robotics.com/PAROL-docs](https://docs.source-robotics.com/PAROL-docs/) and
[docs.source-robotics.com/par6](https://docs.source-robotics.com/par6/).

## Document history

The manual is versioned by gripper release, the version the product repository tags (the selector in the header);
within a release it follows the Spectral firmware the gripper runs, with a new revision letter per update. The
text and the images are licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), the code
examples [MIT](https://github.com/Source-Robotics/SSG48-gripper-docs/blob/main/LICENSE-CODE); the hardware design is published under the CERN Open Hardware Licence v2, strongly reciprocal (CERN-OHL-S-2.0), in the
[product repository](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper). The Source Robotics name, the product names and the logos are not covered
by any of these.

| Revision | Date | Changes |
|---|---|---|
| 2026.E | draft | Spectral firmware 110: a move ends cleanly, with a few mA left (KI-11); a soft start; 0 and 255 reached without pressing on the stops, each end read under a light push (KI-12); an object reported after 50 ms of standstill; the gripper pushes with its own current and leaves the driver's limit alone (KI-13); the calibration restarts from the beginning and needs 1000 ticks of stroke (KI-3); brake or coast saved (KI-14); a watchdog that runs out while idle starts no hold (KI-15); parameters 90 to 93; `#Estop` over UART |
| 2026.D | 2026-11-10 | Spectral firmware 109: the generated CAN and UART reference; the SSG-48 preset's current gains on 109; a poll right after a move no longer cancels it (KI-10); calibration puts the current limit back (KI-5); the gripper's current clamped at 2800 mA. Python library 1.21, which reads the object detection right (KI-7) |
| 2026.C | 2026-11-05 | The M8 pinout corrected to the one the gripper is built with (1 +24 V, 2 CANL, 3 GND, 4 CANH; page 17 of the SSG-48 assembly manual): the pin table, its drawing and the quick start of 2026.B had all four pins wrong; the bootloader comes with Spectral release 104, the first built for it; the cable warnings: the other robot's cable reverses the supply, it does not put 24 V on the CAN pins; the PAROL6 cable's pin pairs |
| 2026.B | 2026-11-04 | Gripper release 2, with the files as downloads on the release; known issues; data for robot integration (frame, mass, inertia, TCP); check boxes after each step and Windows, Linux and macOS tabs; numbered figure captions; the downloads with their versions; safety at the jaws, static and cleaning; the thermistor and the thermal cement in the BOM; the hardware licence CERN-OHL-S-2.0 |
| 2026.A | 2026-11-03 | First version in this form: the manual chapters, the generated CAN and UART reference; gripper release 1.1, firmware 107 |
