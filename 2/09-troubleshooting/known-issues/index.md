# Known issues

The faults in the gripper's firmware and in the software that drives it that are known and not yet fixed, and
what to do until they are. The gripper has no firmware of its own: these are the Spectral Micro driver's, in
gripper mode. The pages that describe each part say the same where it matters; this page collects them in one
place. Which versions work together is in [Versions and compatibility](https://docs.source-robotics.com/SSG48-gripper-docs/2/appendix/compatibility/).

### Spectral driver firmware

Seen in: 110.

| | What happens | What to do | More |
|---|---|---|---|
| KI-1 | A gripper E-stop raises the E-stop error again at every control cycle for as long as the last gripper command carries the E-stop bit, so Send_Clear_Error (or `#Clear`) seems to do nothing. | Send a gripper command with the E-stop bit at 0 and the action bit at 0 (or `#Gripstop 0`), then clear. | [Errors and recovery, clearing](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/errors/#clearing) |
| KI-2 | The answer to a full Send_gripper_data_pack is sent before the gripper acts on the command, so it carries the state from before it. | Ignore that answer, and follow the move with empty frames. On firmware 109 and older, also give a move about 100 ms before you trust its object detection. | [Over CAN, host checklist](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/can/#host-checklist) |
| KI-4 | The action status in the gripper's answer is the action bit of the last command; the firmware never clears it, neither at the end of a move nor in the calibration. | Follow a move by its object detection and the position, not by the action status. | [The gripper's state byte](https://docs.source-robotics.com/SSG48-gripper-docs/2/reference/errors/#the-grippers-state-byte) |
| KI-6 | With braking in idle switched on (Send_Settings, parameter 18, or `#Brake 1`), the current that turning the motor drives through its shorted phases is not limited. Until firmware 110 the setting was not saved either (KI-14). | Leave the default, coasting, unless you need the brake, and do not force the jaws by hand while it brakes. | [Send_Idle](https://docs.source-robotics.com/SSG48-gripper-docs/2/reference/can/system/#send_idle) |

### PAROL6 Python API (parol6)

Seen in: 0.9.1.

| | What happens | What to do | More |
|---|---|---|---|
| KI-8 | In `rbt.tool.status()`, `engaged` is always true (it is read from the speed field, which the robot always reports as 1), and `part_detected` reads bits 3 and 2 of the gripper's state byte, the temperature and timeout errors, not the object detection in bits 5 and 4. | To know that a part is held, check the position the jaws stopped at, or use a sensor. | [On PAROL6 and PAR6, driving it](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/robots/#driving-it) |
| KI-9 | `rbt.tool.calibrate()` counts the calibration done after a fixed 2 s without reading the calibrated bit, and the SSG-48 takes about 3 s, longer when the jaws start far from the open end. The API has no action to clear a gripper error. | Wait for the calibration before the first move, as the example on the PAROL6 page does; clear an error in the commander's Gripper tab or with Motor GUI, then calibrate. | [On PAROL6 and PAR6, driving it](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/robots/#driving-it) |

### Fixed

| | What happened | Fixed in | More |
|---|---|---|---|
| KI-3 | A full gripper command or a clear sent during the gripper calibration ends it, and the gripper stays uncalibrated. The routine's counters are not reset, so the next calibration starts where the stopped one was (it can skip the opening) and counts the time already spent towards its 30 s limit. | 110: a new calibration starts from the beginning, with its whole 30 s; a command or a clear still ends a running one, and the gripper keeps the calibration it had before | [Over CAN, host checklist](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/can/#host-checklist) |
| KI-5 | The motor calibration (`#Cal`) sets the driver's current limit to 1600 mA and leaves it there, and `#Save` stores it. Gripper moves are not affected, they use each command's current; the driver's own modes, such as the current and position modes of the teleoperation guide, run with up to 1600 mA. | 109: calibration puts back the current limit that was in force when it started | [Driver setup and first run, current limit](https://docs.source-robotics.com/SSG48-gripper-docs/2/build/first-run/#current-limit) |
| KI-7 | `gripper_object_detection` has its two bits swapped: the library reports 1 where the gripper sends 2 (object found while opening) and 2 where it sends 1 (object found while closing); 0 and 3 are right. | 1.21: `gripper_object_detection` reads the two bits the right way round | [With Python](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/python/) |
| KI-10 | A status poll (an empty Send_gripper_data_pack) or a repeat of the command that reaches the driver within one control cycle (about 0.2 ms) of a new move command cancels it as new. The move then runs in position mode, and object detection reads 3 while the jaws press on an object. | 109: only a new command marks itself new, so a poll or a repeat no longer cancels the move | [Over CAN, host checklist](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/can/#host-checklist) |
| KI-11 | After a move the current took a second or more to settle, and some of it stayed while the gripper held the position. The velocity loop carried the current of the move into the hold and unwound it slowly through the mechanism's friction. | 110: the integral is dropped on arrival, the last stretch is slower and the hold has a small dead zone; a few mA are left after a move | [How the gripper works, the states](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/how-it-works/#the-states) |
| KI-12 | The gripper calibration read the two ends while it pushed into the stops at 500 mA, so positions 0 and 255 lay inside the stops. A full open or close with less current stopped short, kept pressing on the stop with the grip current, and often reported an object (1 or 2) instead of 3; a gripper a few ticks short of 255 reported 254. | 110: each end is read under a light 100 mA push; 0 lies 32 encoder ticks inside the open stop, 255 16 ticks from the closed one; the position is rounded to the nearest step | [How the gripper works, the states](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/how-it-works/#the-states) |
| KI-13 | Gripper moves set the driver's current limit (`#Ilim`, parameter 16) to the current of each command, and the gripper calibration set it to 500 mA. A Send_Save_config or `#Save` then stored that as the driver's limit. | 110: the gripper and its calibration push with their own current; the driver's limit stays as set | [Driver setup and first run, current limit](https://docs.source-robotics.com/SSG48-gripper-docs/2/build/first-run/#current-limit) |
| KI-14 | Brake or coast when idle (parameter 18) was not saved. After every power-up the driver coasted, whatever was set before Send_Save_config. | 110: Send_Save_config keeps it; a driver that never saved it coasts, as before | [System, parameters a gripper uses](https://docs.source-robotics.com/SSG48-gripper-docs/2/reference/can/system/#parameters-a-gripper-uses) |
| KI-15 | With the watchdog's action set to hold or descend, a watchdog that ran out while the gripper was idle started the hold or the descend later, when the next gripper command arrived, for the whole fallback time. | 110: hold and descend start only when the watchdog runs out in gripper mode | [System, Send_Watchdog](https://docs.source-robotics.com/SSG48-gripper-docs/2/reference/can/system/#send_watchdog) |

## Something that is not here

Check [Troubleshooting](https://docs.source-robotics.com/SSG48-gripper-docs/2/09-troubleshooting/) first. If it is still not explained, [Report a problem](https://docs.source-robotics.com/SSG48-gripper-docs/2/support/report-a-problem/)
says what to include so it can be reproduced. A fixed issue stays on this page, under "Fixed", with the version
that fixes it.
