# Import necessary libraries
import RPi.GPIO as GPIO
import time

# Set up GPIO pins
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    
    # Turn on LED
    GPIO.output(18, GPIO.HIGH)
    
    # Wait for 5 seconds
    time.sleep(5)
    
    # Turn off LED
    GPIO.output(18, GPIO.LOW)
    
    # Clean up GPIO pins
    GPIO.cleanup()
    
except Exception as e:
    print("An error occurred: ", e)

# Add comments to explain the purpose and functionality of each section of the code.
# Import necessary libraries
# Import the RPi.GPIO library to control the GPIO pins on the Raspberry Pi and the time library to add delays in the code.

# Set up GPIO pins
# Set the mode of the GPIO pins to BCM and set up pin 18 as an output.

# Turn on LED
# Set the output of pin 18 to HIGH to turn on the LED.

# Wait for 5 seconds
# Add a delay of 5 seconds using the time.sleep() function.

# Turn off LED
# Set the output of pin 18 to LOW to turn off the LED.

# Clean up GPIO pins
# Clean up the GPIO pins using the GPIO.cleanup() function to reset the pins to their default state.