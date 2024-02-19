import time
import board
import busio
from adafruit_seesaw.seesaw import Seesaw
import neopixel
print("Libraries loaded")


# Set up the NeoPixel strip using the SPI connection
pixel_pin = board.GP16  # Change this to the correct pin for your board
num_pixels = 8  # Change this to the number of pixels on your NeoPixel stick
neopixel_strip = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False)

# For input calibration
min_abs_moisture = 350.0
max_abs_moisture = 1150.0

# setup variables for sampling
sleep_timer = 2.0
deep_sleep = 6
retries = 4
samples = 1

# setup for soil sensor
i2c = busio.I2C(scl=board.GP27, sda=board.GP26)
ss = Seesaw(i2c, addr=0x36)

# Functions
#====================================
def avg_soil(sleep_timer, samples):
    print("Testing Soil.  Takes 6+ seconds (or sleep_timer x samples)")
    count = 0
    total = 0
    while count < samples:
        total = total + ss.moisture_read()
        time.sleep(sleep_timer)
        count += 1
    soil = total / samples
    return (round(soil, 1))

def update_leds(moisture):
    if moisture <= 0.0:
        neopixel_strip[0] = (35, 0, 0)
        neopixel_strip[1] = (15, 0, 0)
        neopixel_strip[2] = (0, 0, 0)
        neopixel_strip[3] = (0, 0, 0)
        neopixel_strip[4] = (0, 0, 0)
        neopixel_strip[5] = (0, 0, 0)
        neopixel_strip[6] = (0, 0, 0)
        neopixel_strip[7] = (0, 0, 0)
        
    elif moisture <= 0.1:
        neopixel_strip[0] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 0)
        neopixel_strip[1] = (0, 0, 0)
        neopixel_strip[2] = (0, 0, 0)
        neopixel_strip[3] = (0, 0, 0)
        neopixel_strip[5] = (0, 0, 0)
        neopixel_strip[6] = (0, 0, 0)
        neopixel_strip[7] = (0, 0, 0)
        
    elif moisture <= 0.2:
        neopixel_strip[0] = (0, 0, 35)
        neopixel_strip[1] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 0)
        neopixel_strip[2] = (0, 0, 0)
        neopixel_strip[3] = (0, 0, 0)
        neopixel_strip[5] = (0, 0, 0)
        neopixel_strip[6] = (0, 0, 0)
        neopixel_strip[7] = (0, 0, 0)
        
    elif moisture <= 0.3:
        neopixel_strip[0] = (0, 0, 35)
        neopixel_strip[1] = (0, 0, 35)
        neopixel_strip[2] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 0)
        neopixel_strip[3] = (0, 0, 0)
        neopixel_strip[5] = (0, 0, 0)
        neopixel_strip[6] = (0, 0, 0)
        neopixel_strip[7] = (0, 0, 0)
        
    elif moisture <= 0.4:
        neopixel_strip[0] = (0, 0, 35)
        neopixel_strip[1] = (0, 0, 35)
        neopixel_strip[2] = (0, 0, 35)
        neopixel_strip[3] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 0)
        neopixel_strip[5] = (0, 0, 0)
        neopixel_strip[6] = (0, 0, 0)
        neopixel_strip[7] = (0, 0, 0)
        
    elif moisture <= 0.5:
        neopixel_strip[0] = (0, 0, 35)
        neopixel_strip[1] = (0, 0, 35)
        neopixel_strip[2] = (0, 0, 35)
        neopixel_strip[3] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 25)
        neopixel_strip[5] = (0, 0, 0)
        neopixel_strip[6] = (0, 0, 0)
        neopixel_strip[7] = (0, 0, 0)
        
    elif moisture <= 0.6:
        neopixel_strip[0] = (0, 0, 35)
        neopixel_strip[1] = (0, 0, 35)
        neopixel_strip[2] = (0, 0, 35)
        neopixel_strip[3] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 25)
        neopixel_strip[5] = (25, 0, 25)
        neopixel_strip[6] = (0, 0, 0)
        neopixel_strip[7] = (0, 0, 0)
        
    elif moisture <= 0.7:
        neopixel_strip[0] = (0, 0, 35)
        neopixel_strip[1] = (0, 0, 35)
        neopixel_strip[2] = (0, 0, 35)
        neopixel_strip[3] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 25)
        neopixel_strip[5] = (25, 0, 25)
        neopixel_strip[6] = (25, 0, 25)
        neopixel_strip[7] = (0, 0, 0)
        
    elif moisture <= 0.8:
        neopixel_strip[0] = (0, 0, 35)
        neopixel_strip[1] = (0, 0, 35)
        neopixel_strip[2] = (0, 0, 35)
        neopixel_strip[3] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 25)
        neopixel_strip[5] = (25, 0, 25)
        neopixel_strip[6] = (25, 0, 25)
        neopixel_strip[7] = (25, 0, 25)
        
    elif moisture <= 0.9:
        neopixel_strip[0] = (25, 0, 25)
        neopixel_strip[1] = (0, 0, 35)
        neopixel_strip[2] = (0, 0, 35)
        neopixel_strip[3] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 25)
        neopixel_strip[5] = (25, 0, 25)
        neopixel_strip[6] = (25, 0, 25)
        neopixel_strip[7] = (25, 0, 25)

    else:
        neopixel_strip[0] = (25, 0, 25)
        neopixel_strip[1] = (25, 0, 25)
        neopixel_strip[2] = (0, 0, 35)
        neopixel_strip[3] = (0, 0, 35)
        neopixel_strip[4] = (0, 35, 25)
        neopixel_strip[5] = (25, 0, 25)
        neopixel_strip[6] = (25, 0, 25)
        neopixel_strip[7] = (25, 0, 25)
        

    # Write the color data to the NeoPixel strip
    neopixel_strip.show()

def calibrate_moisture(avg_moisture, min_moisture, max_moisture):
    output = (avg_moisture - min_moisture)/(max_moisture - min_moisture)
    clamped = min(1, max(0, output))
    return clamped

def main():
    while True:
        avg_moisture = avg_soil(sleep_timer, samples)
        try:
            print("Moisture:{}".format(avg_moisture))
        
        except (ValueError, RuntimeError) as e:
            print("Failed to get data, retrying\n", e)
        
        calibrated_moisture = calibrate_moisture(avg_moisture, min_abs_moisture, max_abs_moisture)
        print("Moisture:",calibrated_moisture)
        update_leds(calibrated_moisture)
    
if __name__ == '__main__':
    main()
