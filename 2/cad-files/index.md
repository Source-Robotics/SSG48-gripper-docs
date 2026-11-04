# CAD and downloads

Everything to download for the SSG-48, at the versions these pages describe. The versions come from one file,
`versions.yml`, so this page changes with them; which versions work together is in
[Versions and compatibility](https://docs.source-robotics.com/SSG48-gripper-docs/2/appendix/compatibility/).

## Firmware, software and models

| What | Version | Download | How to install |
|---|---|---|---|
| Driver firmware (Spectral), the gripper's only firmware: `spectral-bldc-firmware-V<number>.bin` and `firmware.json` | [107](https://github.com/Source-Robotics/Spectral-Micro-BLDC-controller/tree/V107) (2026-08-26) | [The release](https://github.com/Source-Robotics/Spectral-Micro-BLDC-controller/releases/tag/V107), or by Motor GUI, which fetches it | [Firmware](https://docs.source-robotics.com/SSG48-gripper-docs/2/08-firmware/#updating) |
| Python library (`Spectral-BLDC`) | [1.20](https://github.com/Source-Robotics/Spectral-BLDC-Python/tree/v1.20) | `pip install Spectral-BLDC`; the source and examples in [Spectral-BLDC-Python](https://github.com/Source-Robotics/Spectral-BLDC-Python) | [With Python](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/python/#installing) |
| URDF and MJCF (MuJoCo) models: the gripper alone with pinch or fin-ray fingers (`ssg48_urdf.zip`, `ssg48_mujoco.zip`), and PAROL6 and PAR6 with the gripper mounted | [2.18.1](https://github.com/Source-Robotics/robot_descriptions/tree/v2.18.1) (2026-11-03) | [The release](https://github.com/Source-Robotics/robot_descriptions/releases/tag/v2.18.1); the guide: [ssg48.md](https://github.com/Source-Robotics/robot_descriptions/tree/v2.18.1/guides/ssg48.md) | [Data for robot integration](https://docs.source-robotics.com/SSG48-gripper-docs/2/03-technical-data/integration-data/) |
| CAN message definitions (JSON, DBC) for this firmware release | the same release | [CAN frame tool and downloads](https://docs.source-robotics.com/SSG48-gripper-docs/2/reference/can-tools/#downloads) | |
| Motor GUI, the browser tool for the driver and the gripper | the current one | [motorgui.com](https://motorgui.com/) | [Motor GUI](https://docs.source-robotics.com/SSG48-gripper-docs/2/05-setup/motor-gui/) |

The version links open the files at exactly that release. Known faults in each are on
[Known issues](https://docs.source-robotics.com/SSG48-gripper-docs/2/09-troubleshooting/known-issues/).

## CAD and build files

The latest files, on the main branch of the
[product repository](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper).

| What | Where |
|---|---|
| STEP files: the body parts, the whole gripper, the jaw plate and pinch jaws, the coupler connector template, the UR5 adapter plate | [STEPS](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/STEPS) in the product repository |
| Printable parts (STL) of both hardware versions and the coupler connectors for PAROL6 and PAR6 | [Gripper STL parts](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Gripper%20STL%20parts) |
| Fin-ray fingers and their jaw plate | [gripper jaws](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/gripper%20jaws) |
| Bill of materials | [BOM.md](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/blob/main/BOM/BOM.md), and on this site: [Bill of materials](https://docs.source-robotics.com/SSG48-gripper-docs/2/build/bill-of-materials/) |
| Assembly manual (PDF) and the motor's datasheet | [Assembly manual](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Assembly%20manual) |
| Assembly video | [YouTube](https://www.youtube.com/watch?v=127zXHKuqIg) |
| Cable wiring diagrams | [Building_cables.md](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/blob/main/Assembly%20manual/Building_cables.md) |

## More

| What | Where |
|---|---|
| The driver's documentation | [docs.source-robotics.com/Spectral-BLDC-docs](https://docs.source-robotics.com/Spectral-BLDC-docs/) |
| ROS 2 drivers | [ssg48_adaptive_electric_gripper_ros2](https://github.com/Lass6230/ssg48_adaptive_electric_gripper_ros2), [source_robotics_msg_gripper_ros2](https://github.com/Source-Robotics/source_robotics_msg_gripper_ros2) |
| The legacy gripper GUI, a Python program | [SSG-gripper-GUI](https://github.com/Source-Robotics/SSG-gripper-GUI) |
| CANvas USB-to-CAN adapter | [CANvas-adapter](https://github.com/Source-Robotics/CANvas-adapter) |
| This documentation | [SSG48-gripper-docs](https://github.com/Source-Robotics/SSG48-gripper-docs) |
| Shop | [source-robotics.com](https://source-robotics.com/products/compliant-gripper) |
