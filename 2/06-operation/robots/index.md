# On PAROL6 and PAR6

The gripper is made for the Source Robotics arms. Both drive it over their own CAN bus; their software calibrates
it, moves it and reads its state, so a program for the robot does not talk CAN itself. The tool centre point, the
mass, the centre of mass and the inertia for the robot's tool settings, on these robots or any other, are on
[Data for robot integration](https://docs.source-robotics.com/SSG48-gripper-docs/2/03-technical-data/integration-data/).

## PAROL6

### Mounting and connecting

1. Fit `coupler_connector_PAROL6` to the gripper ([Mounting on a robot](https://docs.source-robotics.com/SSG48-gripper-docs/2/04-installation/mounting/)). It
   carries a shaft coupler with an 8 mm bore and two M4 clamp screws for the joint 6 shaft, and the homing tab
   that joint 5 homes against: the tab goes on the same side as the gripper's cable connector, with an M3 × 12
   screw in the marked hole, as the last pages of the assembly manual show.
2. Slide the gripper onto the joint 6 shaft, orient it, and tighten the two clamp screws, one on each side, with
   blue threadlocker.
3. Connect the [PAROL6 gripper cable](https://source-robotics.com/products/gripper-cable) between the gripper and
   the M8 connector at the forearm. Only this cable: the PAR6 cable is wired differently and destroys the gripper
   ([The cable](https://docs.source-robotics.com/SSG48-gripper-docs/2/04-installation/cable/)).
4. Keep the gripper's node ID at 0 and switch its termination on; it is the last node on the robot's bus.

### The joint 5 homing offset

Joint 5 homes against the tool, and the SSG-48's coupler sits differently from the pneumatic gripper holder that
the control board firmware's default offset (8900) is for. Set `j5_homing_offset` to `8035` in `main.cpp` of the
control board firmware and upload it, as the PAROL6 documentation describes for the SSG-48. After the first
homing, check joint 5 with the pin through its witness marks, and master the robot if needed.

### Driving it

The gripper calibrates after every power-up and does not move before that. Clear the gripper's errors first, then
calibrate, then wait until the calibration is done, a few seconds: a gripper move or a clear sent while it runs
ends the calibration.

=== "Commander software"
    The **Gripper** tab: after homing the robot, press **Clear gripper error**, then **Calibrate gripper**, and
    wait until the status says calibrated. Then set the position, speed and current with the sliders and press
    **Move GoTo**. In RBTscript: `Gripper_cal()`, `Delay(6)`, then `Gripper(position, speed, current)`, with the
    current in mA.

=== "Python API"
    ```python
    import time

    rbt.select_tool("SSG-48")                              # the parol6 package; pinch fingers: variant_key="pinch"
    rbt.tool.calibrate()                                   # with the robot at rest
    time.sleep(6)                                          # the calibration takes a few seconds
    rbt.tool.set_position(0.8, speed=0.5, current=0.4)     # fractions; current 0.4 is 580 mA
    print(rbt.tool.status())
    ```

    The API allows the calibration 2 s before it sends the next gripper action, which can be too short when the
    jaws start far from the open end; the pause above waits for the calibration to finish.

The Python API's `current` is a fraction of the range 100 to 1300 mA: the gripper gets 100 + 1200 × `current` mA,
so 1.0 is 1300 mA, within the 1500 mA a grip may use. Use a low value for a long hold
([Force and speed](https://docs.source-robotics.com/SSG48-gripper-docs/2/03-technical-data/force-and-speed/)). `position` and `speed` are fractions of the position
and speed bytes: 0.8 is position 204, 0.5 is speed 128.

The [PAROL6 documentation](https://docs.source-robotics.com/PAROL-docs/) covers the robot's side: the gripper
port, the commander software, the API and the tool centre point.

## PAR6

The PAR6 arm's control box runs the gripper on its CAN bus as a tool, with `coupler_connector_PAR6` and the PAR6
gripper cable (different from the PAROL6 one). The [PAR6 documentation](https://docs.source-robotics.com/par6/)
covers the tool configuration, the runtime's gripper commands and the firmware updates the box can do for the
gripper.

## UR5 and other robots

The repository has an adapter plate for the UR5 flange. Any controller with a CAN interface drives the gripper
directly: [Over CAN](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/can/) is the protocol, [With Python](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/python/) and [With ROS 2](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/ros2/) are two ready
implementations, and the [CAN reference](https://docs.source-robotics.com/SSG48-gripper-docs/2/reference/can/) has every byte.
