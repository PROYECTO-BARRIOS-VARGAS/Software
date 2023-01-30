

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
    
    def is_stimulating(self):
        return self.status.stimulating
    def is_communicating(self):
        return self.status.communicating

    def set_status(self,  ipg_st : IPG_status):
            self.status = ipg_st

    def get_status(self) ->  IPG_status:
            return self.status

        

class BurnInBoard():

    IPG_in_board = 2
    
    def __init__(self,id):
        self.idNum = id
        self.IPGs = [IPG(id) for id in range(self.IPG_in_board)]
        
   
        
class BoardManager():

    NUM_OF_BOARDS = 1
    
    def __init__(self, ):
        self.Borards = [BurnInBoard(id) for id in range(self.NUM_OF_BOARDS)]

    def update_board_status(self, board, raw_bytes : bytes):
        for ipg in self.Borards[board].IPGs:
            ipg_status = IPG_status()
            ipg_status.parse_byte(raw_bytes[ipg.idNum])
            ipg.set_status(ipg_status)

    def get_board(self, board_num):
        return self.Borards[board_num]
    # def get_board_status

        
class InterfaceManager():
    def __init__(self, interface, boardManager):
        self.Borards = [BurnInBoard(id) for id in range(self.NUM_OF_BOARDS)]
        self.UI = interface


