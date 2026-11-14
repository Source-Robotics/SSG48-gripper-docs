# Calibrate, activate, move

Every session with the gripper starts the same way: clear what errors there are, calibrate, activate. Then it
moves. This page does it once with Motor GUI, with Python and over UART; [How the gripper works](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/how-it-works/)
explains what happens inside.

!!! danger
    The jaws move over the whole stroke during calibration, and close with the set force afterwards. Nothing in
    reach of them, fingers included.

## 1. Power up

At power-up the gripper reports *Not calibrated* and does not move. Its motor must be calibrated too, which a
bought gripper is from the factory; a self-built gripper gets that during its assembly, [Driver configuration](https://docs.source-robotics.com/SSG48-gripper-docs/2/build/first-run/).

!!! success "Check"
    The gripper answers: Motor GUI's panel fills in, or a status poll returns a frame. If not:
    [The gripper does not answer](https://docs.source-robotics.com/SSG48-gripper-docs/2/09-troubleshooting/#the-gripper-does-not-answer).

## 2. Clear errors

The driver powers up in an error state until its motor is calibrated and it has run through its checks; an
E-stop, an over-temperature or a supply fault leave an error too. A gripper with an error does not move, and
does not calibrate either: clear first.

=== "Motor GUI"
    **Clear errors**, when the panel shows an error.

=== "Python"
    ```python
    gripper.Send_Clear_Error()
    ```

=== "UART"
    ```
    #Clear
    ```

An error whose cause is still present comes straight back; after an E-stop, send a command with the E-stop bit
at 0 before you clear. [Errors and recovery](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/errors/) says what each needs.

!!! success "Check"
    No error is reported: Motor GUI shows none, and the temperature, timeout and E-stop bits of the answer are 0.

## 3. Calibrate

The gripper calibration finds the two end stops: the jaws open fully, then close fully, at low force
(500 mA) and low speed.

Each end is recognised when the jaws have stood still against it for a little over half a
second, and read under a light 100 mA push. Positions 0 and 255 lie just inside the two stops, so a full open or
close does not press on them.

It takes a few seconds; the result is not kept over a power cycle, so this runs at every power-up.

=== "Motor GUI"
    **Calibrate**, and confirm. When the jaws stop, the panel shows *Calibrated*; press nothing else until then.

=== "Python"
    ```python
    gripper.Send_gripper_calibrate()
    time.sleep(6)       # send nothing meanwhile; With Python waits for the calibrated bit instead
    ```

=== "UART"
    ```
    #Gripcal
    ```

If the jaws do not move at all, or move to one end and stop: the gripper is in an error state (clear it first, see
step 2), or the motor is not calibrated.

If the routine runs for 30 seconds and gives up, an end stop was not
found: something blocks the jaws short of the end, or the mechanism is too stiff for 500 mA.

If the jaws barely move, less than 1000 encoder ticks between the two ends, the routine ends without a
calibration: something jams them.

Until the gripper reports *Calibrated*, send nothing but status polls: a move command or a clear during the
calibration ends it. The gripper then keeps the calibration it had before, none after a power-up. Calibrate
again, and the routine starts from the beginning.

!!! success "Check"
    The jaws opened fully, then closed fully, and the gripper reports *Calibrated* (the calibrated bit is 1;
    `#Gripinfo` prints the end stops it found). If not: [Calibration](https://docs.source-robotics.com/SSG48-gripper-docs/2/09-troubleshooting/#calibration).

## 4. Activate

A calibrated gripper carries out a move only while it is activated.

=== "Motor GUI"
    **Activate**. The panel shows *Activated*.

=== "Python"
    The activate bit is part of every move command, its fourth argument; send it as 1. To activate without
    moving, send a command with the action bit, the fifth argument, at 0:

    ```python
    gripper.Send_gripper_data_pack(0, 30, 300, 1, 0, 0, 0)   # position, speed, current, activate = 1, action = 0, E-stop, release direction
    ```

=== "UART"
    `#Grippos` activates by itself; `#Gripact 1` activates without moving.

!!! success "Check"
    The gripper reports *Activated* and the jaws have not moved.

## 5. Move

A move is three numbers: the position (0 open, 255 closed), the speed (0 to 255: linear from 0.1 to 184 mm/s at
each jaw) and the current limit in mA, which is the grip force ([Force and speed](https://docs.source-robotics.com/SSG48-gripper-docs/2/03-technical-data/force-and-speed/)).
Start with speed 30, about 22 mm/s at each jaw, and 300 mA, about 16 N.

=== "Motor GUI"
    Set *Speed* 30 and *Current* 300 with their **Set** buttons, then **Close** and **Open**, or set a *Position*:
    the jaws follow, the plots show the position and the current, and the state says whether the jaws reached
    the position or stopped on something.

=== "Python"
    ```python
    gripper.Send_gripper_data_pack(200, 30, 300, 1, 1, 0, 0)   # position, speed, current, activate, action, E-stop, release direction
    time.sleep(2)
    gripper.Send_gripper_data_pack(20, 30, 300, 1, 1, 0, 0)
    ```

=== "UART"
    ```
    #Gripvel 30
    #Gripcur 300
    #Grippos 200
    #Grippos 20
    ```

Put an object between the jaws and close on it: the jaws stop on it and hold it with 300 mA, and the state reads
*object detected while closing*. Raise the current for a firmer grip, up to 1500 mA for a short grip, and the
speed once the motion is what you want.

!!! success "Check"
    The jaws reach each position and the state reads *at the position*; on an object they stop and the state
    reads *object detected while closing*. If not: [It does not move](https://docs.source-robotics.com/SSG48-gripper-docs/2/09-troubleshooting/#it-does-not-move).

## What the gripper reports

Every move command is answered with the gripper's state, which Motor GUI shows in its panel and the
library puts into attributes: the position, the current, whether it is calibrated and activated, whether a move
is in progress, the object-detection result, and the three error bits. [How the gripper works](https://docs.source-robotics.com/SSG48-gripper-docs/2/06-operation/how-it-works/)
goes through them.
