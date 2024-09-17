# LambdaMeter

## Version 1

This is a minimal fork of [`py-ws7`](https://github.com/stepansnigirev/py-ws7) relying on Telnet for the server / client communication.

This directly implements a server thread running continuously in the Wavemeter class allowing any client to connect and query the
wavelength / frequency as long as one instance is running.

For the Telnet server it relies on [`TelnetServer`](https://github.com/OliverLSanz/python-telnetserver).

## Installation

## How to test it
- go to Tests folder and open `TestClientWlm.py` and change the IP address and port to the one of the server
- run `python TestClientWlm.py`

## Future features ?


