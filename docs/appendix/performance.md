# Performance tests

Thermal tests of the SSG-48 gripper under different conditions. The thermal limit is 75 °C at the thermistor in
the motor windings.

!!! warning
    A gripper built without a thermistor in the windings has no temperature protection and can damage its motor
    in normal operation.

## Several days of cycling

- Open and close every 2.5 s, no load: the current near 0
- 7 days without interruption
- Motor temperature: 42 °C
- Ambient temperature: 33 °C

## Holding at a constant current

- Hold an object at 300 mA for 24 hours
- Stable motor temperature: 62 °C
- Ambient temperature: 33 °C

## The current that trips the thermal limit

- Hold an object at 1600 mA
- The temperature error trips after 4 minutes
- Ambient temperature: 33 °C

What this means for use: a hold at 300 mA (about 15 N) runs indefinitely; a grip at 1500 mA (about 72 N) is for
seconds, not minutes. Between the two, the motor heats in proportion to the square of the current.
