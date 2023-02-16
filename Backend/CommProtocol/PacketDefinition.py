
# command codes
class CMD():
    STATUS_REQUEST  = 0x01
    START_BURN_IN   = 0x02
    STOP_BURN_IN    = 0x03
    GET_TEMPERATURE = 0x04
    
class Packetize():
    
    # requests
    def status_req(target_board_id : int) -> bytes:
        return bytes([target_board_id,  CMD.STATUS_REQUEST])

    def start_burn_in(target_board_id : int) -> bytes:
        return bytes([target_board_id, CMD.START_BURN_IN])

    def stop_burn_in(target_board_id : int) -> bytes:
        return bytes([target_board_id, CMD.STOP_BURN_IN])

    def get_temp(target_board_id : int) -> bytes:
        return bytes([target_board_id, CMD.STOP_BURN_IN])

