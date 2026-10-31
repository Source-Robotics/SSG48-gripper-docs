# Driver setup

The driver commands a self-built gripper is configured with; [Driver configuration](https://docs.source-robotics.com/SSG48-gripper-docs/1.1/build/first-run/)
is the procedure.

| Command | Kind | Argument | What it does | Response |
|---|---|---|---|---|
| `#Kpiq` | Set/Get | float: gain | Kp of the Iq current loop; also sets Kpid. | the current value |
| `#Kiiq` | Set/Get | float: gain | Ki of the Iq current loop; also sets Kiid. | the current value |
| `#Kt` | Set/Get | float: Nm/A | The torque constant, found by calibration. | the current value |
| `#Cal` | Action |  | Runs the calibration routine (see Calibration): it measures R and L, finds the pole pairs, the phase order and the angle offset, and measures Kt, KV and the flux linkage. | the calibration log |
| `#Save` | Action |  | Writes the configuration to the EEPROM. Do it after calibration and after tuning. | `Save` |
| `#Ilim` | Set/Get | int: current in mA | The driver's Iq current limit outside gripper mode; the firmware clamps it to 2800 mA. Gripper moves use Gripcur instead. | the current limit |
| `#Tlim` | Set/Get | int: temperature in °C | The temperature at which the temperature error is raised; 75 by default. | `Temp limit N` |
| `#Default` | Action |  | Writes the factory defaults to the EEPROM, including the serial number, hardware version and batch date, and clears the gripper flag, heartbeat and watchdog. Back those up first. | `Loaded default config!` |
| `#Term` | Set/Get | int: 0 or 1 | Enables the thermistor measurement and the temperature error (off by default). | the setting |
| `#Cbw` | Set/Get | float: bandwidth in Hz | The current loop bandwidth calibration uses to compute Kpiq and Kiiq. | the bandwidth |
| `#CANID` | Set/Get | int: 0 to 13 | The CAN node ID. Use 0 to 13: the firmware accepts 14 and 15, but the bootloader reserves them and a driver on one of those cannot be updated over CAN. Setting the ID also sets the bootloader's board ID. Kept over a power cycle after Save. | the ID, or `Invalid CAN ID` |
