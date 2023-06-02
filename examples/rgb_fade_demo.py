from PyLightDMX import *
import PortFinder as port_finder
import time

if __name__ == '__main__':
    dmx_port = port_finder.find_serial_number("VEGLIH5YA")

    dmx = PyLightDMX(dmx_port, refresh_rate=60)

    fade_duration = 3  # Duration of the fade in seconds
    fade_start_time = time.time()

    while time.time() - fade_start_time < fade_duration:
        elapsed_time = time.time() - fade_start_time
        brightness = int(100 - (elapsed_time / fade_duration) * 100)

        dmx.set_rgb(channels=1, values=[255, 0, 255], brightness=brightness)
        dmx.send()

    del dmx
