import telnetlib


class WavelengthMeterClient(telnetlib.Telnet):
    def __init__(self, host="localhost", port=1234):
        super().__init__(host=host, port=port)

    def get_wavelength(self, channel: int = 1) -> float:
        """Query the wavelength on the server.

        Args:
            channel (int, optional): The channel to read. Defaults to 1.

        Returns:
            float: The wavelength in nm.
        """
        assert channel in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
        ], "Channel should be integer between 1 and 8"
        self.write(f"wavelength,{channel}".encode())
        ret = self.read_until("\n\r".encode())
        try:
            ret = float(ret)
        except ValueError:
            print("Warning ! Received error: {ret}")
        return ret

    def get_frequency(self, channel: int = 1) -> float:
        """Query the frequency on the server.

        Args:
            channel (int, optional): The channel to read. Defaults to 1.

        Returns:
            float: The frequency in THz.
        """
        assert channel in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
        ], "Channel should be integer between 1 and 8"
        self.write(f"frequency,{channel}".encode())
        ret = self.read_until("\n\r".encode())
        try:
            ret = float(ret)
        except ValueError:
            print("Warning ! Received error: {ret}")
        return ret
