# Dimensions and CAD

<model-viewer class="hero-model" src="../../assets/models/ssg48.glb" alt="The SSG-48 gripper, turnable in 3D" camera-controls auto-rotate rotation-per-second="18deg" shadow-intensity="1" exposure="1.1" camera-orbit="-35deg 72deg auto" interaction-prompt="auto" loading="lazy"></model-viewer>
<p class="hero-model-caption">Drag to turn the gripper, scroll to zoom. The model is the repository's URDF with the fin-ray fingers half open; the
<a href="https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/SSG48_gripper_description">URDF and MJCF files</a> drive it in ROS 2, Gazebo and MuJoCo.</p>

<figure markdown="span">
  ![Front view](../assets/DIM2.PNG){ width="700" }
  <figcaption>Figure 4: Front view, in millimetres: 104 mm over the jaw plates, 60.7 mm from the coupler face to the top of the jaw plates, 26 mm jaw plates.</figcaption>
</figure>

<figure markdown="span">
  ![Side view](../assets/DIM3.PNG){ width="700" }
  <figcaption>Figure 5: Side view.</figcaption>
</figure>

<figure markdown="span">
  ![Top view](../assets/DIM4.PNG){ width="600" }
  <figcaption>Figure 6: Top view, with the jaw plates and their hole pattern.</figcaption>
</figure>

<figure markdown="span">
  ![With the PAROL6 coupler](../assets/DIM1.PNG){ width="700" }
  <figcaption>Figure 7: The gripper with the PAROL6 coupler connector.</figcaption>
</figure>

<figure markdown="span">
  ![The stroke](../assets/gripper_stroke.png){ width="520" }
  <figcaption>Figure 8: 48 mm of stroke between the jaw plates, 104 mm overall.</figcaption>
</figure>

## CAD

The STEP files of every part are in the product repository, the reference for anything that has to fit:

- [STEPS](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/STEPS): the body parts
  (`Gripper STEP files`), the whole gripper (`3D MODEL`), the jaw plate template, the pinch jaws, the generic
  coupler connector template and the UR5 adapter plate.
- [Gripper STL parts](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Gripper%20STL%20parts):
  the printable parts of both hardware versions and the coupler connectors for PAROL6 and PAR6.
- [gripper jaws](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/gripper%20jaws):
  the fin-ray fingers and their jaw plate.

<figure markdown="span">
  ![The STEP model](../assets/GRIP_MODEL.PNG){ width="600" }
  <figcaption>Figure 9: The STEP model of the gripper.</figcaption>
</figure>

## For simulation

The [SSG48_gripper_description](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/SSG48_gripper_description)
folder has a URDF of the gripper and an MJCF for MuJoCo 3.1.3 and newer, with a scene file.

[CAD and downloads](../cad-files.md) lists everything that can be downloaded.
