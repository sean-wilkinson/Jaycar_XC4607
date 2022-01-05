# Jaycar_XC4607

I purchased a XC4607 module from jaycar to mess around with. There is some sample code for the XC4607 on the jaycar website but there is no documentation available, so it took me a few days to figure out how to get it working. I am using a raspberry pi pico to drive the display. This code is written in micropython so it's pretty self explanatory but i'll breifly explain how it works.

The display is updated one column at a time, serial data for the n'th column is shifted out using bit banging of the clock and data GPIO pins, once the 16 bits have been shifted out the latch is toggled low then high to indicate we have finished transferring the two bytes. The four column select output pins are set then the enable pin is briefly enabled to flash the column LED's. This process is repeated for all columns. The LED's on this display are multiplexed and takes advantage of persistance of vision so the display needs to be updated continuously.

I hope this discription, code and pinout helps somebody else trying to get started with this module.
