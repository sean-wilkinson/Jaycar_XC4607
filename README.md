# Jaycar_XC4607

I purchased an "Arduino Compatible 16x16 LED Dot Matrix Module" (XC4607) from jaycar to mess around with over the Christmas holidays. There is some sample code for the XC4607 on the jaycar website but there is no documentation available, so it took me a few days to figure out how to get it working. I am using a raspberry pi pico to drive the display. This code is written in micropython so it's pretty self explanatory but i'll breifly explain how it works.

The display is updated one column at a time, serial data for the n'th column is shifted out using bit banging of the clock and data GPIO pins, once the 16 bits for the 16 LED's in the column have been shifted out the latch is toggled low then high to indicate we have finished transferring the two bytes. The four column select output pins are set to represent a 4 bit binary value then the enable pin is briefly enabled to flash the column LED's. This process is repeated for all columns. The LED columns on this display are multiplexed and takes advantage of persistance of vision so the display needs to be updated continuously in a loop.

I hope this discription, code and pinout help's somebody else trying to get started with this module.

Pin Out

| Description | RPI Pico | XC4607 |
| ----------- | -------- | ------ |
| +5 volts | VBUS | +5 |
| Ground | GND | GND |
| Latch | 2 | LAT |
| Clock | 3 | CLK | 
| Data | 4 | DI | 
| Enable | 5 | G |
| Column Select 1 | 6 | A |
| Column Select 2 | 7 | B |
| Column Select 3 | 8 | C |
| Column Select 4 | 9 | D |
