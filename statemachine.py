import time
import datetime
import RPi.GPIO as GPIO
from gpiozero import LED, Button
import smbus2
import serial

# Setup GPIO
GPIO.setmode(GPIO.BCM)

# Set GPIO Pins
button_toggle = Button(25)  # Button to toggle heating/cooling
button_up = Button(12)      # Button to increase temperature set point
button_down = Button(16)    # Button to decrease temperature set point
led_red = LED(17)           # Red LED for heating
led_blue = LED(27)          # Blue LED for cooling

# Initialize UART (for simulating data sent to server)
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

# Initialize I2C (AHT20 temperature sensor)
bus = smbus2.SMBus(1)
AHT20_ADDRESS = 0x38

# Set initial thermostat state and set point
state = "off"
set_point = 72
current_temperature = 0

# Function to read temperature from AHT20 sensor
def read_temperature():
    bus.write_i2c_block_data(AHT20_ADDRESS, 0xAC, [0x33, 0x00])
    time.sleep(0.1)
    data = bus.read_i2c_block_data(AHT20_ADDRESS, 0x00, 6)
    raw_temp = ((data[3] & 0x0F) << 16) + (data[4] << 8) + data[5]
    temperature = (raw_temp / 1048576.0) * 200.0 - 50.0
    return round(temperature, 2)

# Function to update the LEDs based on state
def update_leds():
    global current_temperature
    if state == "heating":
        if current_temperature < set_point:
            led_red.blink(on_time=0.5, off_time=0.5)
            led_blue.off()
        else:
            led_red.on()
            led_blue.off()
    elif state == "cooling":
        if current_temperature > set_point:
            led_blue.blink(on_time=0.5, off_time=0.5)
            led_red.off()
        else:
            led_blue.on()
            led_red.off()
    else:
        led_red.off()
        led_blue.off()

# Function to handle state toggle
def toggle_state():
    global state
    if state == "off":
        state = "heating"
    elif state == "heating":
        state = "cooling"
    else:
        state = "off"
    print(f"State changed to: {state}")

# Function to handle temperature adjustments
def adjust_set_point(increase):
    global set_point
    if increase:
        set_point += 1
    else:
        set_point -= 1
    print(f"Set point adjusted to: {set_point}")

# Function to send data over UART
def send_data():
    now = datetime.datetime.now()
    output_string = f"{state},{current_temperature},{set_point}"
    ser.write(output_string.encode('utf-8'))
    print(f"Sent data: {output_string}")

# Main loop
try:
    while True:
        current_temperature = read_temperature()
        update_leds()
        send_data()
        
        # Button handlers
        button_toggle.when_pressed = toggle_state
        button_up.when_pressed = lambda: adjust_set_point(True)
        button_down.when_pressed = lambda: adjust_set_point(False)

        # LCD display simulation
        now = datetime.datetime.now()
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Current Temp: {current_temperature}°F, Set Point: {set_point}°F, State: {state}")

        time.sleep(30)

except KeyboardInterrupt:
    GPIO.cleanup()
    ser.close()
