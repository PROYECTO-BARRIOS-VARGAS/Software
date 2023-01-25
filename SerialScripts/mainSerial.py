# from asyncore import write
import serial
import serial.rs485
import RS485_serial_module.RS485_serial as rs485
import time
from windows_com_find.port_find import get_port_name, print_available_ports


    # def __init__(self, baudrate, bytesize, parity, stopbits, *args,**kwargs):
    #     super().__init__(baudrate=baudrate, 
    #                     bytesize=bytesize, 
    #                     parity=parity, 
    #                     stopbits=stopbits, 
    #                     *args, 
    #                     **kwargs)

serial_interface_name = 'USB-SERIAL CH340'

class IPG_status():
    def __init__(self):
        self.burnin_active = False
        self.stimulating = False
        self.communicating = False
    
    def parse_byte(self,  byte):
        self.stimulating =  True if byte & 0b00001000 != 0 else False
        self.communicating =  True if byte & 0b00000100 != 0 else False

class IPG():
    def __init__(self, id):
        self.idNum = id
        self.status = IPG_status()

class BurnInBoard():

    IPG_in_board = 2
    
    def __init__(self):
        self.IPGList = [IPG(id) for id in range(IPG_in_board)]
        
    def set_IPG_status(self, ipg_num : int, ipg_st : IPG_status):
        self.IPGList[ipg_num].status = ipg_st

    def get_IPG_status(self, ipg_num : int) ->  IPG_status:
        return self.IPGList[ipg_num]

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

if __name__ == "__main__":
    ser = Serial()
    while True:
        # send_read_cmd()
        # _ser.write(tx_buffer)
        option = input('OPCIONES:\n  (1) get status\n  (2) start burnin\n  (3) stop burnin\n    -> ')
        if option == '1':
            ser.command_get_status()
            print('Status')
            print(' '.join(hex(byte) for byte in bytes(_ser.read(2))))
            print('')
        elif option == '2':
            ser.command_start_burn_in()
            print('Sending START command')
            print('')
        elif option == '3':
            ser.command_stop_burn_in()
            print('Sending STOP command')
            print('')
        else:
            print('\nWRONG OPTION!\n')
            
        time.sleep(1)
        _ser.flushInput()
        _ser.flushOutput()
