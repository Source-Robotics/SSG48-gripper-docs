# Hardware versions

The SSG-48 exists in two mechanical versions, both in the product repository's
[Gripper STL parts](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/tree/main/Gripper%20STL%20parts):

| Version | Folder | What differs |
|---|---|---|
| V1 | `V1` | the original body, lid, gear and magnet shaft |
| V2 | `V2` | the "large bearing" body, lid, gear and magnet shaft: a larger bearing on the pinion for a stiffer, longer-lasting mechanism |

The electronics, the motor, the rail, the jaw plates, the coupler connectors and everything about control are the
same in both; a gripper from the shop is a V2. The product release V1.1 (2024) is the version tested with PAROL6.

The jaw plates, the coupler connectors (`coupler_connector_PAROL6`, `coupler_connector_PAR6`,
`connector_coupler_generic`) and the fingers are common to both versions.
