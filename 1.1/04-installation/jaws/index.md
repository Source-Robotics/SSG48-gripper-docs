# Jaws

The gripper's two jaw plates carry a four-hole pattern for fingers. The product repository has fingers to print
and a template for your own.

<figure markdown="span">
  ![The jaw plate template](https://docs.source-robotics.com/SSG48-gripper-docs/1.1/assets/jaw_plate.PNG){ width="520" }
  <figcaption>Figure 13: The jaw plate template, with the four mounting holes.</figcaption>
</figure>

| Fingers | Files | Use |
|---|---|---|
| Fin-ray fingers | `fin_ray_1`, `fin_ray_3`, `Finger_1` and `Jaw_plate_fin_ray` in [gripper jaws](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/gripper%20jaws) | fingers that wrap around round and irregular objects; printed in a flexible filament |
| Pinch jaws | `solid_jaws_pinch` and `solid_jaws_pinch_foam` in [STEPS](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/STEPS) | solid jaws for small and flat objects, with or without a foam pad |
| Your own | `Jaw_plate.STEP`, the template | keep the hole pattern, shape the rest |

## Limits

- Fingers at most **80 mm** tall and **60 mm** wide: longer fingers multiply the lever arm on the jaw plates
  and the rail, and foul the body at full opening.
- The grip force is set at the finger faces. A finger that bends takes some of it.

!!! warning "Custom fingers on a PAR6"
    On a PAR6, custom fingers must keep the size of the original fingers: no longer, no wider and no thicker.
    The PAR6 software works with the gripper's original dimensions (its collision model of the tool and the
    tool centre point), so a larger finger reaches where the robot does not expect it.

## Calibrate after changing the fingers

The gripper calibration finds the end stops with the fingers fitted; fingers that meet earlier or later than the
old ones change where 255 is. Calibrate again after a change, which happens at the next power-up anyway.
