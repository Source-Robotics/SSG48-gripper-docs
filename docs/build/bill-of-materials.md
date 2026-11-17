# Bill of materials

!!! note "This is a copy"
    The original is [BOM/README.md](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/blob/main/BOM/README.md) in the gripper's repository; this page is that file as of
    2026-11-17 (commit `c45aa45`), with the reference images shown inline. If a link is broken or a part is wrong,
    [open an issue](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/issues/new) there, and the fix lands here with the next sync. The shop's
    [starter kit](index.md#kits-and-the-shop) covers the driver and everything its setup needs.

This BOM lists all components required to build the SSG48 gripper. Quantities are for **one gripper**. Many of the links are affiliate links to AliExpress and Amazon: if you buy through them, we earn a small commission at no extra cost to you. As an Amazon Associate we earn from qualifying purchases.

!!! note
    If any product links are broken, unavailable, or no longer point to the correct item, please [open an issue](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/issues/new), send us a message on Discord, or contact us via email. You can also use the reference images to find the same or an equivalent part from another supplier.



## Screws and Nuts

| Diameter / Type | Length | Quantity | Description | Link |
|-----------------|--------|----------|-------------|------|
| M2.5 | 8 mm | 4 |  |  |
| M2 | 4 mm | 8 |  |  |
| M3 | 5 mm | 5 | Cheese head screw |  |
| M2 | 10 mm | 1 |  |  |
| M3 | 8 mm | 7 | Cheese head screw |  |
| M4 | 10 mm | 4 |  |  |
| M3 | 12 mm | 4 |  |  |
| M3 | 10 mm | 4 |  |  |



## Brass Inserts

| Thread | Length | Outer Diameter | Quantity | Description | Link |
|--------|--------|----------------|----------|-------------|------|
| M3 | 3 mm | 4.5 mm | 1 | ![brass_insert](../assets/bom/brass_insert.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_DnCPrW9)<br>[amazon.de](https://www.amazon.de/dp/B0CTKHNNDS?tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B0F4JH1K2Z?tag=sourcerobotic-20) |
| M3 | 5 mm | 4.5 mm | 15 | ![brass_insert](../assets/bom/brass_insert.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_DnCPrW9)<br>[amazon.de](https://www.amazon.de/dp/B0CTKH773W?tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B0FDKYTMZ8?tag=sourcerobotic-20) |


## Motors

!!! note
    **If you are having a hard time sourcing motors consider building our [MSG gripper](https://github.com/Source-Robotics/MSG-compliant-AI-stepper-gripper)!**

| Type | Quantity | Description | Link |
|------|----------|-------------|------|
| GBM5208-75 | 1 | ![GBM5208](../assets/bom/GBM5208.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_DmkWskt) //  [Alibaba link](https://www.alibaba.com/product-detail/Flashhobby-GBM5208-75-0-3KG-5208_1601005642241.html)<br>[amazon.com](https://www.amazon.com/dp/B0BYFFX57Q?tag=sourcerobotic-20) |


## Mechanical Components

| Type | Quantity | Description | Link |
|------|----------|-------------|------|
| Shaft coupler | 1 | 8 mm hole shaft, M4 screw holes<br>![shaft_coupler](../assets/bom/shaft_coupler.webp){ width="120" } | [Link](https://www.aliexpress.com/item/4000208248034.html?spm=a2g0o.order_list.order_list_main.521.6af018026rwEsK)<br>[amazon.de](https://www.amazon.de/dp/B0FNWRLWR4?tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B08335MYGW?tag=sourcerobotic-20) |
| MGN7C slider | 2 | ![MGN7C_carriage](../assets/bom/MGN7C_carriage.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_oEZfs3x)<br>[amazon.de](https://www.amazon.de/s?k=MGN7C+slider&tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B08ZS6DFCN?tag=sourcerobotic-20) |
| Linear guide | 1 | 100 mm<br>![MGN7_rail](../assets/bom/MGN7_rail.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_oBSDfjN)<br>[amazon.de](https://www.amazon.de/s?k=MGN7+linear+rail&tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/s?k=mgn7c+linear+rail&tag=sourcerobotic-20) |
| Magnet | 1 | 6 mm diameter, 2.5 mm thickness, diametrically magnetised<br>![magnet_diametrically](../assets/bom/magnet_diametrically.webp){ width="120" } | [Link](https://source-robotics.com/products/6x2-5mm-diametrical-neodymium-magnet) |


## Electronics

| Type | Quantity | Description | Link |
|------|----------|-------------|------|
| Spectral micro BLDC driver | 1 | [source-robotics.com](http://source-robotics.com/)<br>![Spectral_micro](../assets/bom/Spectral_micro.webp){ width="120" } | [Link](https://source-robotics.com/products/spectral-micro-bldc-controller) |
| XH 2.54 mm, 300 mm, 2P, double-ended | 1 | Cable for 24 V<br>![XH_cable](../assets/bom/XH_cable.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_c4XKzTj9)<br>[amazon.de](https://www.amazon.de/dp/B0CBWZLB5C?tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B0D6KSMK1Q?tag=sourcerobotic-20) |
| ZH 1.5 mm, 300 mm, 2P, double-ended | 1 | Cable for CAN bus<br>![ZH_cable](../assets/bom/ZH_cable.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_c4XKzTj9)<br>[amazon.de](https://www.amazon.de/dp/B0FMCW2R5B?tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B0DSPCFH9D?tag=sourcerobotic-20) |
| Male 4-pin connector | 1 | ![M8connectormale4pin](../assets/bom/M8connectormale4pin.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_DCG5Rff)<br>[amazon.com](https://www.amazon.com/dp/B0FKVL6772?tag=sourcerobotic-20) |
| 100K NTC thermistor | 1 | NTC 100K 3950, glued into the motor windings: the driver stops the gripper at 75 °C<br>![Thermistor](../assets/bom/Thermistor.webp){ width="120" } | [Link](https://source-robotics.com/products/100k-ntc-thermistor) |
| Thermal cement | 1 | Holds the thermistor in the windings and conducts the heat to it<br>![Thermal_cement](../assets/bom/Thermal_cement.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_c3dBOwTD)<br>[amazon.de](https://www.amazon.de/dp/B0BR2CK4J8?tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B0C5D8JQ7R?tag=sourcerobotic-20) |


## Cables

Parts for the DIY cable version below:

| Type | Length / Spec | Quantity | Description | Link |
|------|---------------|----------|-------------|------|
| 26 AWG cable | 0.15 mm², 4-wire twisted pair | 0.4 m | Usually 35 cm cable is enough<br>![Twisted_pair_cable](../assets/bom/Twisted_pair_cable.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_DeGUD4Z)<br>[amazon.de](https://www.amazon.de/dp/B0D2QVTCPF?tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B0FHNWRQSB?tag=sourcerobotic-20) |
| M8 4-pin male wire connector | — | 1 | ![M8_male](../assets/bom/M8_male.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_DCG5Rff)<br>[amazon.de](https://www.amazon.de/dp/B0DS7JSG14?tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B0FG3JTF1H?tag=sourcerobotic-20) |
| M8 4-pin female wire connector | — | 1 | ![M8_female](../assets/bom/M8_female.webp){ width="120" } | [Link](https://s.click.aliexpress.com/e/_DCG5Rff)<br>[amazon.de](https://www.amazon.de/dp/B0DS7JSG14?tag=sourcerobotic-20)<br>[amazon.com](https://www.amazon.com/dp/B0FG3JTF1H?tag=sourcerobotic-20) |

Check out the cable building guide [here](https://github.com/Source-Robotics/SSG-48-adaptive-electric-gripper/blob/main/Assembly%20manual/Building_cables.md)


!!! note
    Equivalent parts from other suppliers may be used as long as specifications match.
