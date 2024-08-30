from LambdaMeter import WavelengthMeterClient

client = WavelengthMeterClient()
for i in range(100):
    print(client.get_wavelength(2))
