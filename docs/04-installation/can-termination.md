# CAN termination

A CAN bus needs a 120 Ω resistor at each of its two ends. The gripper's driver has one, on a switch. The gripper
is normally the last node on a robot's bus, where the switch must be **ON**.

| The gripper is | Switch |
|---|---|
| the last node on a robot's bus, at the end of the arm | ON |
| alone on a bench bus with the CANvas adapter (which has its own termination) | ON |
| in the middle of a bus, with other nodes after it | off |

To change it, unscrew the coupler connector: the switch is on the Spectral Micro driver inside the body, next to
its CAN connectors; **ON** connects the resistor. The driver's
[connector page](https://docs.source-robotics.com/Spectral-BLDC-docs/latest/03-technical-data/connectors/) shows
where it is on the board.

A bus with the right termination measures about 60 Ω between CANH and CANL with everything unpowered. A missing
or doubled termination shows up as lost frames and a gripper that answers only sometimes.
