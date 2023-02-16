import serial
import serial.rs485

class RS485_serial(serial.Serial):

    def __init__(self, baudrate, bytesize, parity, stopbits, *args,**kwargs):
        super().__init__(baudrate=baudrate, 
                        bytesize=bytesize, 
                        parity=parity, 
                        stopbits=stopbits,
                        timeout=9.0, 
                        *args, 
                        **kwargs)
        self.rs485_mode = serial.rs485.RS485Settings(rts_level_for_tx=True,
                                                     rts_level_for_rx=False, 
                                                     loopback=False, 
                                                     delay_before_tx=None, 
                                                     delay_before_rx=None)

    def set_port(this, port):
        this.port = port

    def write_bytes(address: bytes, data: bytes):
        super().write(address)
        super().write(data)

    
