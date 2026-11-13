# Connector and pinout

The gripper has one connector, an M8 4-pin male on the side of the body, and one cable: 24 V and the CAN bus.

![The M8 connector on the gripper body and its four signals: CANL, CANH, GND, 24V](https://docs.source-robotics.com/SSG48-gripper-docs/2/assets/GRPCON.webp){ width="700" }
![The M8 connector on the gripper body and its four signals: CANL, CANH, GND, 24V](https://docs.source-robotics.com/SSG48-gripper-docs/2/assets/GRPCON_dark.webp){ width="700" }

## Pin numbers

![M8 male on the gripper, as it sits in the gripper: the numbered signals](https://docs.source-robotics.com/SSG48-gripper-docs/2/assets/gripper-m8-face.svg){ width="650" }
![M8 male on the gripper, as it sits in the gripper: the numbered signals](https://docs.source-robotics.com/SSG48-gripper-docs/2/assets/gripper-m8-face_dark.svg){ width="650" }

The drawing shows the connector's staggered contact layout. Look **into the male connector on the gripper**, with
its pins visible: the mating face, where the cable plugs in. The female cable connector has the mirrored contact
view. Use the numbers moulded into the connector, rather than matching wire colours or the installed housing's
rotation.

| Gripper pin | Signal | Connection |
|---|---|---|
| **1** | **CANL** | CAN low |
| **2** | **CANH** | CAN high, 1 Mbit/s with CANL |
| **3** | **+24 V** | positive motor supply |
| **4** | **GND** | power-supply return |

These are the numbers of the mating face, the side you connect to.

!!! note "Building the gripper: the solder side"
    Page 17 of the [assembly manual](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/blob/main/Assembly%20manual/Gripper_assembly_manual.pdf)
    numbers the other side of the same connector, where the wires are soldered when the gripper is built:
    1 24V, 2 CANL, 3 GND, 4 CANH. Use those numbers for soldering only, and the table above for connecting.

They describe the **gripper end**. PAROL6 and PAR6 use different connections at the robot end:
[The cable](https://docs.source-robotics.com/SSG48-gripper-docs/2/04-installation/cable/) gives both diagrams. Check continuity with the supply disconnected.

!!! danger "The wrong cable destroys the driver"
    A reversed supply or 24 V on a CAN pin destroys the driver inside the gripper the moment it is powered; the
    other robot's cable reverses the supply. Use the cable
    made for your robot; check a self-made cable pin by pin against the pinout above and the wiring diagram before you
    plug it in.

## Inside the body

The Spectral Micro driver's own connectors are inside, reachable when the coupler connector is unscrewed: its
UART port (3.3 V, JST SH, 4 pins), used to configure a self-built gripper ([Over UART](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/uart/)),
and its CAN termination switch ([CAN termination](https://docs.source-robotics.com/SSG48-gripper-docs/2/04-installation/can-termination/)). The driver's pinout
is in the [Spectral Micro documentation](https://docs.source-robotics.com/Spectral-BLDC-docs/latest/03-technical-data/connectors/).
