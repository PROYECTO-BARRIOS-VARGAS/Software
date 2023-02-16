class IPG_status():
    def __init__(self):
        self.stimulating = False
        self.communicating = False

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

    def parse_byte(self,  byte):
        self.status.stimulating =  True if byte & 0b00001000 != 0 else False
        self.status.communicating =  True if byte & 0b00000100 != 0 else False