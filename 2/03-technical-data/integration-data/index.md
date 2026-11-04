# Data for robot integration

What a robot's software needs to carry the gripper: the frame it is mounted by, the mass, the centre of mass, the
inertia and the tool centre point (TCP). The numbers come from the gripper's URDF and MJCF (MuJoCo) models in
[robot_descriptions](https://github.com/Source-Robotics/robot_descriptions/tree/v2.18.1), version 2.18.1,
moved into the frame below; the two files give the same values. Both models are on
[CAD and downloads](https://docs.source-robotics.com/SSG48-gripper-docs/2/cad-files/).

## The frame

The origin is the centre of the mounting face, on the coupler side: the plane where the robot's flange meets the
gripper, and the `flange` frame of the URDF and MJCF models. On PAROL6 it is the flange face, 50.5 mm from the
joint 6 centre ([Dimensions and kinematics](https://docs.source-robotics.com/PAROL-docs/latest/03-technical-data/kinematics/)).

- **Z** points out of the mounting face, through the body to the fingers: the approach direction. On the robot it
  is the flange's Z.
- **Y** is the jaw travel: the jaws move apart and together along Y, symmetrically about Z.
- **X** is square to both, across the 31.4 mm width of the jaw plates. The M8 connector on the body points along
  X.

## Mass and inertia

The centre of mass in mm, the inertia in kg·m² about the centre of mass, with axes parallel to the frame, for
fully open jaws.

| Fingers | Mass, measured | Mass in the model | Centre of mass x, y, z | Ixx, Iyy, Izz | Ixy, Ixz, Iyz |
|---|---|---|---|---|---|
| Pinch jaws (the model's Solid jaws, `ssg48_solid`) | 440 g | 440.0 g | 0.06, 0.14, 25.71 | 2.615e-4, 1.220e-4, 2.245e-4 | -6.14e-6, -2.69e-6, 0.86e-6 |
| Fin-ray fingers (`ssg48_fin_ray`) | 440 g | 440.0 g | 0.06, 0.14, 25.71 | 2.615e-4, 1.220e-4, 2.245e-4 | -6.14e-6, -2.69e-6, 0.86e-6 |

The jaws do not move the centre of mass: they travel symmetrically. Closing them brings each finger 23.5 mm
towards the Z axis, which lowers Ixx and Izz by about 0.65e-4 kg·m² at the closed end.

## Tool centre point

| Fingers | x, y, z | Orientation | Opening | The point |
|---|---|---|---|---|
| Pinch jaws | 0, 0, 91.4 mm | the frame's: roll, pitch and yaw 0 | any | the middle between the finger tips, where the tips meet when the jaws close |
| Fin-ray fingers | 0, 0, 114.8 mm | the frame's: roll, pitch and yaw 0 | any, with the fingers unloaded | the middle between the finger tips |

The point stays on the Z axis at every opening, because the jaws move symmetrically. The middle of the gripping
faces is lower: at z = 75.9 mm for the pinch jaws (faces from 60.4 to 91.4 mm) and 87.6 mm for the fin-ray
fingers (60.4 to 114.8 mm). The models have one `tcp` frame for both finger types, at 0, 0, 83.8 mm with the
frame's orientation; the PAROL6 and PAR6 robot models move it (on PAROL6, a6 = 134.3 mm = 50.5 + 83.8 mm).
robot_descriptions keeps it as a control frame, not a measured grasp centre: it is 7.6 mm short of the pinch tips
and 31.0 mm short of the fin-ray tips.

## How accurate the numbers are

The masses are measured: 440 g for the whole gripper, 39.3 g for each moving assembly (carriage, jaw and finger)
and 361.4 g for the rest. The centre of mass and the inertia are not: robot_descriptions
(2.18.1, [MODEL_DETAILS.md](https://github.com/Source-Robotics/robot_descriptions/tree/v2.18.1/docs/maintenance/MODEL_DETAILS.md))
says that the gripper COM and central inertia remain unverified estimates. Both finger types share one set of mass
properties in the model, so the two rows are the same. In both files each finger's centre of mass lies on the
other side of the Z axis from the finger, and 8 to 13 mm closer to the mounting face than the finger meshes'
centres: the open-jaw values above come out close, but the files' own inertia at other openings is not reliable.
The geometry, and with it the frame and the finger tips, is the CAD's.

## Where the numbers go

On PAROL6, `rbt.select_tool("SSG-48")` (with `variant_key="pinch"` for the pinch jaws) sets the Python API's own
TCP for the gripper, and `set_tcp_offset` or `set_tcp_transform` moves it
([Tools and the TCP](https://docs.source-robotics.com/PAROL-docs/latest/programming/02-python-api/tools-and-tcp/));
in a URDF, the frame is a fixed joint from the robot's flange, the mass table an `<inertial>` and the TCP a
`tcp` link, as in the models' `ssg48_description` package.
