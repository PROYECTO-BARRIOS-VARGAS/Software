# from asyncore import write
import serial
import serial.rs485
import SerialScripts.RS485_serial_module.RS485_serial as rs485
import time
from SerialScripts.windows_com_find.port_find import get_port_name, print_available_ports


    # def __init__(self, baudrate, bytesize, parity, stopbits, *args,**kwargs):
    #     super().__init__(baudrate=baudrate, 
    #                     bytesize=bytesize, 
    #                     parity=parity, 
    #                     stopbits=stopbits, 
    #                     *args, 
    #                     **kwargs)

serial_interface_name = 'USB-SERIAL CH340'



class Serial():

    def __init__(self, *args):
        self._tx_buffer = bytearray()
        self._rx_buffer = bytearray()
        self._ser = rs485.RS485_serial(19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
        self._ser.set_port(get_port_name(serial_interface_name))
        self._ser.open()
        
    def command_get_status(self,Board_num : int):
        self._tx_buffer.clear()
        self._tx_buffer.append(0xAA)
        self._tx_buffer.append(0x01)
        self._ser.write(self._tx_buffer)
        self._ser.flushOutput()
        return ' '.join(hex(byte) for byte in bytes(self._ser.read(2)))

    def command_start_burn_in(self):
        self._tx_buffer.clear()
        self._tx_buffer.append(0xAA)
        self._tx_buffer.append(0x02)
        self._ser.write(self._tx_buffer)
        self._ser.flushInput()
        self._ser.flushOutput()

    def command_stop_burn_in(self):
        self._tx_buffer.clear()
        self._tx_buffer.append(0xAA)
        self._tx_buffer.append(0x03)
        self._ser.write(self._tx_buffer)
        self._ser.flushInput()
        self._ser.flushOutput()

    def read_n_bytes(self, n : int):
        return bytes(self._ser.read(n))


if __name__ == "__main__":

    ser = Serial()
    while True:
        # send_read_cmd()
        # _ser.write(tx_buffer)
        option = input('OPCIONES:\n  (1) get status\n  (2) start burnin\n  (3) stop burnin\n  (4) salir\n   -> ')
        if option == '1':
            ser.command_get_status(1)
            print('Status')
            print(' '.join(hex(byte) for byte in ser.read_n_bytes(2)))
            print('')
        elif option == '2':
            ser.command_start_burn_in()
            print('Sending START command')
            print('')
        elif option == '3':
            ser.command_stop_burn_in()
            print('Sending STOP command')
            print('')
        elif option == '4':
            break
        else:
            print('\nWRONG OPTION!\n')
            
        time.sleep(1)