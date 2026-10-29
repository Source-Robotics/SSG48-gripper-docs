# Force and speed

A move command carries a current limit in mA and a speed from 0 to 255. This page says what they mean in
newtons and millimetres per second.

## Grip force

The driver limits the motor's current to the value you command, and the force the jaws press with is
proportional to it. The curve below was measured on a gripper from the shop:

<figure markdown="span">
  ![Grip force against current](../assets/Grip_force.PNG){ width="700" }
  <figcaption>Figure 2: The grip force in newtons against the motor current in amperes, measured on a shipped gripper: about 48 N per ampere, from about 5 N at 0.1 A to 72 N at 1.5 A.</figcaption>
</figure>

As a formula, the torque is the torque constant times the current and the pinion turns it into a force on the
racks:

$$
T = K_t \, I_q, \qquad F = \frac{T}{r}, \qquad r = 6\ \text{mm}
$$

with $K_t$ = 0.325 Nm/A, the effective constant fitted to the shipped grippers' motors, and $I_q$ in amperes. For a
self-built gripper with another motor the constant differs: `#Kt` over UART prints what the driver measured for
its motor, and a force measurement is the only reliable calibration.

The force is a limit, not a controlled value: a hard object takes the full force the moment the jaws touch it; a
soft object is squeezed until the force is reached. Below about 150 mA the motor does not move reliably.

!!! danger "Heat"
    The firmware does not clamp the gripper's current. A hold at 300 mA runs for days ([Performance tests](../appendix/performance.md));
    a hold at 1600 mA trips the 75 °C thermistor limit after four minutes. Use high currents for the grip and a
    low current for the hold.

## Speed

The speed byte of a move is mapped by the firmware to the motor's speed in encoder ticks per second, linearly
from 40 at speed 0 to 80000 at speed 255:

$$
\text{ticks/s} = 40 + \frac{80000 - 40}{255}\, C
$$

The motor's encoder has 16384 ticks per revolution, so the angular speed is $\omega = \text{ticks/s} / 16384 \times 2\pi$
and each jaw moves at

$$
v = \omega \, r
$$

| Speed byte | Motor speed | Each jaw moves at | The jaws close at |
|---|---|---|---|
| 0 | 40 ticks/s | 0.1 mm/s | 0.2 mm/s |
| 20 (the power-up default) | 6300 ticks/s, 0.4 rev/s | 15 mm/s | 29 mm/s |
| 30 | 9400 ticks/s, 0.6 rev/s | 22 mm/s | 43 mm/s |
| 128 | 40200 ticks/s, 2.5 rev/s | 92 mm/s | 185 mm/s |
| 255 | 80000 ticks/s, 4.9 rev/s | 184 mm/s | 370 mm/s |

Both jaws move, so the gap closes at twice the speed of one jaw. At speed 255 the 48 mm stroke takes well under a
quarter of a second. The gripper calibration runs at speed 40 and 500 mA.

## Position

The position byte is linear over the stroke: 0 is the fully open end stop found by the gripper calibration, 255
the fully closed one. One step of the byte is 48 mm divided by 255, 0.19 mm. The driver considers the position
reached within 5 encoder ticks, about 0.01 mm.
