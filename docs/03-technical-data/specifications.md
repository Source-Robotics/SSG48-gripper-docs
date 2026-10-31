# Specifications

## Electrical

| | Value |
|---|---|
| Supply voltage | 24 V DC; the driver tolerates 12 to 29 V, the force and speed figures assume 24 V |
| Idle power | 0.5 W |
| Motor current | set per move: up to 1500 mA for a grip, 300 mA for a long hold; see [Force and speed](force-and-speed.md) |
| Interface | CAN 2.0, 1 Mbit/s, 11-bit identifiers; node ID 0 as shipped |
| Connector | M8, 4 pins: 24 V, GND, CANH, CANL |
| CAN termination | 120 Ω, switchable; the switch is on the driver inside the body |
| Service port | the driver's UART, 3.3 V, 256000 baud, inside the body |
| Driver | Spectral Micro BLDC controller, field-oriented control, 14-bit encoder on the motor |
| Temperature protection | thermistor in the motor windings, 75 °C limit (changeable with `#Tlim`) |

## Mechanical

| | Value |
|---|---|
| Stroke | 48 mm |
| Grip force | ideal combined force up to about 80 N at 1500 mA; see the model assumptions in [Force and speed](force-and-speed.md) |
| Jaw speed | up to about 180 mm/s per jaw at speed 255; see [Force and speed](force-and-speed.md) |
| Position resolution | 1/255 of the stroke: 0.19 mm per step of the position byte |
| Mass | 400 g |
| Width | 104 mm over the jaw plates; body 60.7 mm tall |
| Drive | GBM5208-75 gimbal motor, pinion (6 mm pitch radius) on two racks, MGN7 linear rail |
| Grasps | external (closing on the object) and internal (opening inside a hollow object) |
| Mounting | coupler connectors for PAROL6 and PAR6, a UR5 adapter plate, a template for your own |
| Fingers | on the jaw plates' four-hole pattern; at most 80 mm tall and 60 mm wide |
| Body material | PETG, printed |

## Environmental

| | Value |
|---|---|
| Operating temperature | −5 to 65 °C |
| Protection | none: not waterproof or dustproof |
