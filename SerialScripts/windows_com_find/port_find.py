from serial.tools.list_ports_windows import comports

def get_available_ports():
    return comports()

def print_available_ports():
    ports = []
    ports = get_available_ports()
    for port in ports: 
        print(f'{port.name}: {port.description}')
        
def get_port_name(description : str):
    ports = get_available_ports()
    for port in ports:
        if ( port.description.startswith(description)):
            return port.name
