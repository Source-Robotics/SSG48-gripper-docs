# Versions and compatibility

Which Spectral firmware release works with which bootloader, gripper hardware, Python library and ROS 2 driver.
One row per firmware release, newest first; the last column names the version of this site, a gripper release, that
describes it.

| Firmware (Spectral) | Released | Bootloader | SSG-48 gripper | Python library (Spectral-BLDC) | ROS 2 driver | Docs (gripper release) |
|---|---|---|---|---|---|---|
| 110 | 2026-11-13 | required | V2, V1.1 | 1.22 or newer (names for parameters 90 to 93; 1.21 reads them by their numbers) | ssg48_adaptive_electric_gripper_ros2, msg_gripper_ros2 | 2 |
| 109 | 2026-11-10 | required | V2, V1.1 | 1.21 or newer (1.20 swaps object detection 1 and 2) | ssg48_adaptive_electric_gripper_ros2, msg_gripper_ros2 | 2 |
| 107 | 2026-08-26 | required (installed on grippers shipped with 105 or newer) | V2, V1.1 | 1.20 or newer | ssg48_adaptive_electric_gripper_ros2, msg_gripper_ros2 | 2 |
| 106 | 2026-07-06 | required | V1.1 | 1.19 or newer | ssg48_adaptive_electric_gripper_ros2 | not published |
| 105 | 2026-07-05 | required | V1.1 | 1.19 or newer | ssg48_adaptive_electric_gripper_ros2 | not published |
| 104 | 2026-06-19 | required (the first release built for the bootloader, from Bootloader_main) | V1.1 | 1.19 or newer | ssg48_adaptive_electric_gripper_ros2 | the Spectral Micro site, version 101 |
| 101 | 2025-09-29 | none (flashed with a programming adapter) | V1.1 | 1.17 or newer | ssg48_adaptive_electric_gripper_ros2 | the Spectral Micro site, version 101 |

Send_Respond_Device_Info returns the firmware release a gripper runs; `#Info` prints it over UART.
