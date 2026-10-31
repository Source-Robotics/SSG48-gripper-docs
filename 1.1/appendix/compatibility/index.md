# Versions and compatibility

Which Spectral firmware release works with which bootloader, gripper hardware, Python library and ROS 2 driver.
One row per firmware release, newest first; the last column names the version of this site, a gripper release, that
describes it.

| Firmware (Spectral) | Released | Bootloader | SSG-48 gripper | Python library (Spectral-BLDC) | ROS 2 driver | Docs (gripper release) |
|---|---|---|---|---|---|---|
| 107 | 2026-08-26 | required (installed on grippers shipped with 105 or newer) | V1.1 | 1.20 or newer | ssg48_adaptive_electric_gripper_ros2, msg_gripper_ros2 | 1.1 |
| 106 | 2026-07-06 | required | V1.1 | 1.19 or newer | ssg48_adaptive_electric_gripper_ros2 | not published |
| 105 | 2026-07-05 | required (the first release that needs it) | V1.1 | 1.19 or newer | ssg48_adaptive_electric_gripper_ros2 | not published |
| 104 | 2026-06-19 | none (flashed with a programming adapter); the last release of the main branch | V1.1 | 1.19 or newer | ssg48_adaptive_electric_gripper_ros2 | the Spectral Micro site, version 101 |
| 101 | 2025-09-29 | none (flashed with a programming adapter) | V1.1 | 1.17 or newer | ssg48_adaptive_electric_gripper_ros2 | the Spectral Micro site, version 101 |

Send_Respond_Device_Info returns the firmware release a gripper runs; `#Info` prints it over UART.
