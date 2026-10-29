# Mounting on a robot

The gripper mounts by its coupler connector, the round part on the back of the body. Four exist, and the STEP
template lets you make a fifth.

| Robot | Part | Where |
|---|---|---|
| PAROL6 | `coupler_connector_PAROL6.STL` | [Gripper STL parts](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Gripper%20STL%20parts) |
| PAR6 | `coupler_connector_PAR6.STL` | the same folder |
| UR5 | `UR_coupler_gripper.STEP` | [STEPS/UR5 adapter plate](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/STEPS/UR5%20adapter%20plate) |
| your own | `coupler_connector_generic_STEP.STEP`, the template | [STEPS](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/STEPS) |

<figure markdown="span">
  ![The generic coupler connector](../assets/Capture.PNG){ width="520" }
  <figcaption>Figure 10: The generic coupler connector template: the bolt circle of the gripper on the outside, your flange's pattern in the middle.</figcaption>
</figure>

## PAROL6

The PAROL6 coupler connector carries a shaft coupler with an 8 mm bore and two M4 clamp screws for the robot's
last joint.

1. Fit `coupler_connector_PAROL6` to the gripper.
2. Slide the gripper onto the J6 motor shaft.
3. Tighten the two screws of the shaft coupler, one on each side.
4. Connect the [PAROL6 gripper cable](https://source-robotics.com/products/gripper-cable) to the gripper and to
   the robot's gripper port ([The cable](cable.md)).

<div class="grid" markdown>
![The gripper on the J6 shaft](../assets/gripper_parol1.PNG){ width="400" }
![The coupler screws](../assets/gripper_parol4.png){ width="400" }
</div>

The PAROL6 software needs to know the gripper is there: [On PAROL6 and PAR6](../06-operation/robots.md).

## PAR6

`coupler_connector_PAR6` bolts to the PAR6 wrist; the PAR6 gripper cable, wired differently from the PAROL6 one,
goes to the robot's tool connector.

## Another robot

Adapt the template to your flange, or use the UR5 adapter plate as a starting point. Keep the gripper's connector
reachable, and route the cable so that it cannot be pulled by the robot's motion.

## On the bench

For testing, clamp the body, not the jaw plates or the rail, and leave the whole stroke free: calibration moves
the jaws from one end stop to the other without any command from you.
