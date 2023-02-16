from BoardInterface.IPG import IPG_status
from typing import List

class PacketParser():
    
    STIM_BIT = 0b00001000
    COMM_BIT = 0b00000100

    def parse_IPG_status(byte) -> IPG_status:
        ipg_status = IPG_status()
        ipg_status.stimulating = True if byte & PacketParser.STIM_BIT != 0 else False
        ipg_status.communicating =  True if byte & PacketParser.COMM_BIT != 0 else False
        return ipg_status

    def parse_IPG_status_from_bytes(board_bytes : bytes) -> List[IPG_status]:
        ipg_statuses = []
        for ipg_byte in board_bytes:
            ipg_statuses.append(PacketParser.parse_IPG_status(ipg_byte))
        return ipg_statuses

    def parse_temperature():
        return None