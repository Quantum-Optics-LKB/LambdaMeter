import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from LambdaMeter.WavelengthMeterClient import WavelengthMeterClient

## Create a client
## host and port are the default values
client = WavelengthMeterClient(host="localhost", port=1234)

## Test the get_wavelength method
for i in range(1):
## Print the wavelength on channel i
    print(client.get_wavelength(1))
    # print(client.get_exposureMode(2))
    
