from PyLightDMX import *
import PortFinder as port_finder
import time

if __name__ == '__main__':
    dmx_port = port_finder.find_serial_number("VEGLIH5YA")

    dmx = PyLightDMX(dmx_port, refresh_rate=60)

    dmx.set_data_list([(1, 255), (2, 255), (3, 255)])
    dmx.send()
    time.sleep(1)

    dmx.set_data_list([(2, 0), (3, 0)])
    dmx.send()
    time.sleep(1)

    del dmx
