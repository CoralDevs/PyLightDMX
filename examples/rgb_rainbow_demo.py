from PyLightDMX import *
import PortFinder as port_finder
import time
import colorsys

if __name__ == '__main__':
    dmx_port = port_finder.find_serial_number("VEGLIH5YA")
    dmx = PyLightDMX(dmx_port, refresh_rate=60)

    duration = 5  # Duration of the rainbow loop in seconds
    start_time = time.time()

    while time.time() - start_time < duration:
        elapsed_time = time.time() - start_time
        hue = int(elapsed_time / duration * 360) % 360

        # Convert HSV to RGB
        rgb = colorsys.hsv_to_rgb(hue / 360, 1.0, 1.0)
        r, g, b = [int(val * 255) for val in rgb]

        dmx.set_rgb(channels=1, values=[r, g, b], brightness=100)
        dmx.send()

    del dmx
