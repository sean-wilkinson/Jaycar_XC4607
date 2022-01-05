from machine import Pin
import time
import random

# Setup output pins
lat = Pin(2, Pin.OUT)
clk = Pin(3, Pin.OUT)
dat = Pin(4, Pin.OUT)
en = Pin(5, Pin.OUT)
colsel1 = Pin(6, Pin.OUT)
colsel2 = Pin(7, Pin.OUT)
colsel3 = Pin(8, Pin.OUT)
colsel4 = Pin(9, Pin.OUT)

# Generate some random test data
def gendata():
    data = []
    for i in range(16):
        data.append([])
        for j in range(16):
            r = random.randint(0,10)
            if r < 9:
                data[i].append(1)
            else:
                data[i].append(0)
    return data
        
# sent the column data to the display
def sendColmns(data):

    # Loop over all columns
    for i in range(16):
        
        # shift out / bit banging the column serial data for the i'th column and latch to indicate when complete
        for j in range(16):    
            clk.low()
            dat.value(data[i][j])
            clk.high()
        lat.low() 
        lat.high()
        
        # Set output column select pins         
        colsel1.value(i & 1)
        colsel2.value(i & 2)
        colsel3.value(i & 4)
        colsel4.value(i & 8)
        
        # Flash the column for a short period of time
        en.low()
        time.sleep_us(500)
        en.high()
    

lastTime = 0
interval = 100
data = gendata()

# Main Loop
while True:
    
    # Get delta time
    dt = time.ticks_ms() - lastTime
   
    # Generate new data if interval has elapsed
    if dt >= interval:
        data = gendata()
        lastTime = time.ticks_ms()
    
    # sent the columns data to the display
    sendColmns(data)
    
