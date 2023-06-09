# PyLightDMX

PyLightDMX is a Python library for controlling DMX devices using a serial connection (RS-485). <br> It is based on the code by [YoshiRi](https://github.com/YoshiRi/PyDMX)

## Basic usage

Import PyLightDMX. <br> You may also import the included PortFinder.py, which automatically finds the port where a device is connected:

```python
from PyLightDMX import *
import PortFinder as port_finder
```

Create a connection:
```python
dmx_port = port_finder.find_serial_number("VEGLIH5YA")

dmx = PyLightDMX(dmx_port, refresh_rate=60)
```

Set the data for a channel and send it with the `send()` method:
```python
dmx.set_data(1, 255)  # Channel 1, Value = 255
dmx.send()
```

## Additional methods

`set_data_list()`: You can set multiple values at once by passing a list of tuples to this method:
```python
dmx.set_data_list([(1, 255), (2, 255), (3, 255)])
```

`set_rgb()`: This method makes it easier to work with RGB lights (with 3 channels for each color):
```python
set_rgb(channels=1, values=[255, 128, 255], brightness=100)
```

#### Parameters

- `channels`: The channel(s) of the light. Either a list of 3 integers `[r, g, b]` or a single int for `r`, which is incremented for channels `g, b` (e.g. [i, i+1, i+2]).
- `values`: A list of r, g, b values.
- `brightness`: An integer from 0-100, which adjust the percentage of all RGB values accordingly to make it easier to ajust the brightness. Can be omitted, default is `100`

`send_zeros()`: Set the values of all channels to 0 and send the data.
```python
send_zeros()
```
