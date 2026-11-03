# Dimensions and CAD

<div class="gripper-viewer" data-base="../../assets/models/ssg48/" markdown="0">
  <canvas class="gripper-viewer__canvas" aria-label="The SSG-48 gripper in 3D: drag to turn, scroll to zoom"></canvas>
  <div class="gripper-viewer__controls">
    <label class="gripper-viewer__field">Opening <input type="range" name="opening" min="0" max="100" value="50"></label>
    <label class="gripper-viewer__field">Fingers <select name="jaws"></select></label>
    <label class="gripper-viewer__field">Body <span class="gripper-viewer__swatches" data-target="body"></span><input type="color" name="body" value="#d2d2cf" title="Any colour"></label>
    <label class="gripper-viewer__field">Fingers colour <span class="gripper-viewer__swatches" data-target="jaws"></span><input type="color" name="jaws_color" value="#1a1a1a" title="Any colour"></label>
    <button type="button" name="reset" class="md-button">Reset view</button>
  </div>
  <p class="gripper-viewer__hint">Drag to turn the gripper, scroll to zoom, open and close the jaws, try the fingers and the colours. The model is the
gripper's URDF, the fingers its printed options; the current URDF and MuJoCo models are linked from the repository's <a href="https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/ssg48_description">ssg48_description</a> guide. The shop sells the body in black and grey.</p>
</div>

<figure markdown="span">
  ![Front view](https://docs.source-robotics.com/SSG48-gripper-docs/1.1/assets/DIM2.webp){ width="700" }
  <figcaption>Figure 4: Front view, in millimetres, without a coupler connector: 104 mm over the jaw plates, 75 mm across the body, 26 mm jaw plates, 60.7 mm from the top of the jaw plates to the bottom of the driver board.</figcaption>
</figure>

<figure markdown="span">
  ![Side view](https://docs.source-robotics.com/SSG48-gripper-docs/1.1/assets/DIM3.webp){ width="700" }
  <figcaption>Figure 5: Side view.</figcaption>
</figure>

<figure markdown="span">
  ![Top view](https://docs.source-robotics.com/SSG48-gripper-docs/1.1/assets/DIM4.webp){ width="600" }
  <figcaption>Figure 6: Top view, with the jaw plates and their hole pattern.</figcaption>
</figure>

<figure markdown="span">
  ![With the PAROL6 coupler](https://docs.source-robotics.com/SSG48-gripper-docs/1.1/assets/DIM1.webp){ width="700" }
  <figcaption>Figure 7: The gripper with the PAROL6 coupler connector.</figcaption>
</figure>

<figure markdown="span">
  ![The stroke](https://docs.source-robotics.com/SSG48-gripper-docs/1.1/assets/gripper_stroke.webp){ width="520" }
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
  ![The STEP model](https://docs.source-robotics.com/SSG48-gripper-docs/1.1/assets/GRIP_MODEL.webp){ width="600" }
  <figcaption>Figure 9: The STEP model of the gripper.</figcaption>
</figure>

## For simulation

The product repository's [ssg48_description](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/ssg48_description)
guide links the gripper's models, which are kept in [robot_descriptions](https://github.com/Source-Robotics/robot_descriptions):
standalone URDF and MJCF (MuJoCo) packages of the gripper with solid or fin-ray jaws, with their meshes, collision
shapes and mass properties, and the PAROL6 and PAR6 models with the gripper mounted.

[CAD and downloads](https://docs.source-robotics.com/SSG48-gripper-docs/1.1/cad-files/) lists everything that can be downloaded.
