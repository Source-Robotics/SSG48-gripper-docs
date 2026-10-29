# Force and speed

A move command carries a current limit in mA and a speed from 0 to 255. This page says what they mean in
newtons and millimetres per second.

## Grip force

The driver limits the motor's current to the value you command, so the torque the motor produces is limited to
$T = K_t \, I_q$, with $K_t$ the motor's torque constant in Nm/A and $I_q$ the current limit in amperes (the
command is in mA). The pinion turns the torque into the force the jaws press with:

$$
F = \frac{K_t \, I_q}{r}, \qquad K_t = 0.325\ \text{Nm/A}, \quad r = 6\ \text{mm}
$$

$K_t$ is the effective torque constant of the shipped grippers' motors and $r$ the pitch radius of the pinion:
about 54 N per ampere, from about 8 N at 150 mA to 80 N at 1.5 A.

<figure markdown="span">
  ![Grip force against the current limit](../assets/grip_force_light.png#only-light){ width="820" }
  ![Grip force against the current limit](../assets/grip_force_dark.png#only-dark){ width="820" }
  <figcaption>Figure 3: The grip force against the current limit, from the formula above, up to the 1.5 A a grip uses.</figcaption>
</figure>

The curve is computed from the torque constant. A force gauge on a shipped gripper reads a little under it, about
48 N per ampere; a self-built gripper with another motor has another $K_t$, which `#Kt` over UART prints, and a
measurement is the only exact calibration. Below about 150 mA the motor does not move reliably.

The force is a limit, not a controlled value: a hard object takes the full force the moment the jaws touch it; a
soft object is squeezed until the force is reached.

!!! danger "Heat"
    The firmware does not clamp the gripper's current. A hold at 300 mA runs for days ([Performance tests](../appendix/performance.md));
    a hold at 1600 mA trips the 75 °C thermistor limit after four minutes. Use high currents for the grip and a
    low current for the hold.

## Payload

The grip force is not the weight the gripper can lift. An object held by friction between the two jaws is held
by $2\,\mu F$, with $\mu$ the friction coefficient between the fingers and the object, and a safety factor $S$
covers what the robot adds:

$$
W = \frac{2\,\mu\,F}{S}
$$

With a conservative $\mu$ = 0.3 (a hard printed finger on steel or smooth plastic; a flexible fin-ray finger on a
dry object gives more) and $S$ = 2, the gripper at 80 N holds about 24 N, 2.4 kg. That is the weight held at
rest: a robot accelerating at 1 g doubles the load, and an emergency stop decelerates harder than any programmed
move. The friction coefficient is the big unknown; measure it with your fingers on your object, or close on the
object's shape (a form-fit grip) and let friction be the reserve.

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
