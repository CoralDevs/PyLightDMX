from PyLightDMX import *
import PortFinder as port_finder
import time

if __name__ == '__main__':
    dmx_port = port_finder.find_serial_number("VEGLIH5YA")

    dmx = PyLightDMX(dmx_port, refresh_rate=60)

    loop_duration_seconds = 1
    start_time = time.time()

    while time.time() - start_time < loop_duration_seconds:
        dmx.set_data(1, 255)  # Channel 1, Value = 255
        dmx.set_data(2, 255)  # Channel 2, Value = 255
        dmx.send()

    start_time = time.time()

    while time.time() - start_time < loop_duration_seconds:
        dmx.set_data(3, 255)
        dmx.send()  # This will still send previously set values (i.e. for channels 1, 2)

    dmx.send_zeros()  # Set values for all channels to 0 and send the data

    start_time = time.time()

    while time.time() - start_time < loop_duration_seconds:
        dmx.set_data(3, 255)
        dmx.send()

    del dmx
