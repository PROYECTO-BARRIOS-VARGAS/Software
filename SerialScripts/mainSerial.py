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

_ser = rs485.RS485_serial(19200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
_ser.set_port(get_port_name('USB-SERIAL CH340'))
_ser.open()

tx_buffer = bytearray()
rx_buffer = bytearray()

def send_read_cmd():
    print('sending READ command ...')
    
    # tx_buffer.append(0xAA)
    # tx_buffer.append(0xCC)
    # _ser.write(tx_buffer)
    # tx_buffer.extend(0xAA,0xBB)
    # tx_buffer.append(0x02)


def send_start_burn_in_cmd():
    print('sending START command ...')
    tx_buffer.clear()
    tx_buffer.extend(0xAA,0xBB)
    # tx_buffer.append(0x02)
    # _ser.write(0xAA)
    # _ser.write(0xBB)
    
def print_read_cmd_response():
    print('waiting for response...')
    


# compu deberia
# preguntar por info
# Esperar 
#imprimir la info


num = 0
if __name__ == "__main__":
    while True:
        # send_read_cmd()
        # _ser.write(tx_buffer)
        option = input('OPCIONES:\n  (1) get status\n  (2) start burnin\n  (3) stop burnin\n    -> ')
        if option == '1':
            tx_buffer.clear()
            tx_buffer.append(0xAA)
            tx_buffer.append(0x01)
            _ser.write(tx_buffer)
            print('Status')
            print(' '.join(hex(byte) for byte in bytes(_ser.read(2))))
            print('')
        elif option == '2':
            tx_buffer.clear()
            tx_buffer.append(0xAA)
            tx_buffer.append(0x02)
            _ser.write(tx_buffer)
            print('Sending START command')
            print('')
        elif option == '3':
            tx_buffer.clear()
            tx_buffer.append(0xAA)
            tx_buffer.append(0x03)
            _ser.write(tx_buffer)
            print('Sending STOP command')
            print('')
        else:
            print('\nWRONG OPTION!\n')
            
        time.sleep(1)
        _ser.flushInput()
        _ser.flushOutput()
        # send_start_burn_in_cmd()
        # print('going to SLEEP')
        # time.sleep(10)
# if __name__ == "__main__":      
#     print_available_ports()
#     for i in range(255):
#         _ser.write(buffer)
#         buffer[0] = buffer[0] + 1
#         buff = _ser.read()
#         print(buff)
#         time.sleep(0.02)
    
