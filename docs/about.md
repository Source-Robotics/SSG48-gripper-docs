# About this manual

## Scope and audience

The SSG-48 Gripper Manual covers the SSG-48 adaptive electric gripper from unpacking to a gripper that works on
a robot: what the gripper is, how to mount it and cable it, the first setup with the gripper GUI, how it is
controlled over CAN and UART, from Python, from ROS 2 and from the PAROL6 and PAR6 robots, and how its firmware
is updated. The API reference lists the gripper's CAN messages and UART commands for the firmware release named
on the landing page. The Guides cover building a gripper yourself and a teleoperation example.

The gripper is a Spectral Micro BLDC driver in gripper mode. Everything about the driver itself, from its full
command set to its calibration and its bootloader, is in the
[Spectral Micro documentation](https://docs.source-robotics.com/Spectral-BLDC-docs/), and this manual links
there instead of repeating it.

It is written for someone who puts the gripper on a robot or builds one: a maker, a student or an engineer who
can plug in a cable and run a Python script. Read the Safety chapter before you power anything. The
[Quick start](quick-start.md) is the whole first setup on one page; the chapters are in the order you need them and
go deeper.

## Finding your way

--8<-- "navigation.md"

## Warnings and notes

Three kinds of highlighted text appear in this documentation. Read every Danger and Notice before you act on the
step it belongs to.

--8<-- "symbols.md"

## Related documents

<!-- documents-table -->

The driver inside the gripper is documented at
[docs.source-robotics.com/Spectral-BLDC-docs](https://docs.source-robotics.com/Spectral-BLDC-docs/). The MSG
gripper, the SSG-48's successor built on the STEPFOC stepper driver, is documented at
[docs.source-robotics.com/MSG-gripper-docs](https://docs.source-robotics.com/MSG-gripper-docs/). The robots the
gripper is made for are documented at [docs.source-robotics.com/PAROL-docs](https://docs.source-robotics.com/PAROL-docs/)
and [docs.source-robotics.com/par6](https://docs.source-robotics.com/par6/).

## Document history

The SSG-48 Gripper Manual describes one firmware release of the Spectral Micro driver; one revision is kept per
release, and the version selector in the header switches between them.

The text and the images of this documentation are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), the code examples under the [MIT licence](https://github.com/Source-Robotics/SSG48-gripper-docs/blob/main/LICENSE-CODE). The gripper's hardware design is published under the Apache 2.0 licence in the [product repository](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper). The Source Robotics name, the product names and the logos are not covered by any of these.

| Revision | Date | Changes |
|---|---|---|
| 2026.A (draft) | — | First version in this form: the manual chapters, the generated CAN and UART reference, firmware 107 |
