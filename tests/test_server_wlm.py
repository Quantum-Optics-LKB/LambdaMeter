import signal
import sys
import time

from LambdaMeter import WavelengthMeter

wlm = WavelengthMeter(debug=False)
for i, wvl in enumerate(wlm.wavelength):
    print(f"Channel {i + 1} / Wavelength is {wvl} nm")
for i, freq in enumerate(wlm.frequency):
    print(f"Channel {i + 1} / Wavelength is {freq} THz")


def signal_handler(sig, frame):
    print("You pressed Ctrl+C!")
    wlm.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
while True:
    time.sleep(0.1)
